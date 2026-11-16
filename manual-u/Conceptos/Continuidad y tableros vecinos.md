---
tags: [losas-2d-u, concepto, geometria]
---
# Continuidad y tableros vecinos

**Qué es.** La información sobre lo que hay al otro lado de cada borde: si la losa sigue y cuánto mide el tablero siguiente.

**Para qué se usa cada dato.**

| Dato | Efecto |
|---|---|
| ¿Continúa la losa? | Define si el borde es interior o exterior: posición del tablero, coeficientes del DDM, espesor mínimo, apoyo exterior del marco |
| Claro del vecino **perpendicular al marco** | Ancho del marco: $\ell_2=\ell_t/2+\ell_{vecino}/2$ |
| Claro del vecino **en la dirección del marco** | Momento que el vecino lleva al apoyo compartido; claro del marco equivalente; área tributaria de la columna |
| Después del vecino | Cómo termina el marco (ver [[Marco del tablero]]) |

Un mismo vecino cumple los dos papeles: el tablero de la derecha es un claro más del marco en X y, a la vez, no afecta el ancho de los marcos en Y.

**Por qué importa.** En un apoyo compartido los dos claros deben equilibrarse. El DDM manda diseñar con el mayor de los dos momentos negativos (§8.10.4.5 de 318-14); el EFM lo resuelve con las rigideces. Sin el vecino no hay forma de saber cuál gobierna.

**Suposición.** Los apoyos de los tableros vecinos son iguales al del borde compartido (misma viga o mismo muro).

**En la hoja.** Sección 2. Ver [[S02 Tablero, apoyos y continuidad]].
