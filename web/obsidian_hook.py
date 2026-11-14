"""Hook de MkDocs: convierte la sintaxis de Obsidian a Markdown estándar al construir la web.

La carpeta manual/ se edita en Obsidian tal cual; este hook solo actúa en la copia que
MkDocs procesa, así que la bóveda nunca se modifica.

  [[Nota]]                 -> [Nota](ruta/relativa/Nota.md)
  [[Nota#Encabezado|Texto]] -> [Texto](ruta/relativa/Nota.md#encabezado)
  ![[Figura.svg]]          -> ![Figura](ruta/relativa/Figura.svg)
  ![[Nota]]                -> enlace a la nota (las notas incrustadas no se expanden)

Los bloques de código (```...```) y el código en línea no se tocan.
"""
from __future__ import annotations

import logging
import posixpath
import re
from urllib.parse import quote

from markdown.extensions.toc import slugify

log = logging.getLogger("mkdocs.hooks.obsidian")

_index: dict[str, str] = {}  # nombre (sin .md, en minúsculas) -> src_uri

WIKILINK = re.compile(r"(!?)\[\[([^\[\]]+?)\]\]")
FENCE = re.compile(r"^(```|~~~)", re.M)
IMG_EXT = (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp")


def on_files(files, config):
    _index.clear()
    for f in files:
        name = posixpath.basename(f.src_uri)
        _index.setdefault(name.lower(), f.src_uri)
        if name.lower().endswith(".md"):
            _index.setdefault(name[:-3].lower(), f.src_uri)
    return files


def _convert(text: str, page_uri: str) -> str:
    here = posixpath.dirname(page_uri)

    def repl(m: re.Match) -> str:
        embed, body = m.group(1), m.group(2).replace("\\|", "|")
        target, _, alias = body.partition("|")
        target, _, heading = target.partition("#")
        target = target.strip()
        src = _index.get(target.lower()) or _index.get((target + ".md").lower())
        if src is None:
            log.warning("Enlace de Obsidian sin destino en %s: [[%s]]", page_uri, body)
            return alias or target
        rel = quote(posixpath.relpath(src, here or "."))
        if embed and target.lower().endswith(IMG_EXT):
            label = alias if alias and not alias.isdigit() else posixpath.splitext(target)[0]
            return f"![{label}]({rel})"
        anchor = f"#{slugify(heading, '-')}" if heading else ""
        label = alias or (f"{target} › {heading}" if heading else target)
        return f"[{label}]({rel}{anchor})"

    # Convierte solo fuera del código en línea.
    parts = re.split(r"(`[^`\n]*`)", text)
    return "".join(p if p.startswith("`") else WIKILINK.sub(repl, p) for p in parts)


def on_page_markdown(markdown: str, page, config, files):
    out, inside = [], False
    for chunk in re.split(r"(^(?:```|~~~).*$)", markdown, flags=re.M):
        if FENCE.match(chunk):
            inside = not inside
            out.append(chunk)
        elif inside:
            out.append(chunk)
        else:
            out.append(_convert(chunk, page.file.src_uri))
    return "".join(out)


# Orden del menú lateral: primero las notas sueltas (00–04), luego Secciones y al final
# Conceptos. Las notas nuevas aparecen solas en su carpeta, sin tener que listarlas.
_ORDEN = {"secciones": 1, "conceptos": 2}


def on_nav(nav, config, files):
    nav.items.sort(key=lambda it: (_ORDEN.get((it.title or "").lower(), 0)))
    return nav
