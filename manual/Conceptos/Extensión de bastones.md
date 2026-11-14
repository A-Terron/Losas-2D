---
tags: [losas-2d, concepto, detallado]
---
# Extensión de bastones

**Qué es.** La distancia que el refuerzo superior se prolonga dentro del claro, medida desde la cara del apoyo.

![[F27-extension-del-baston.svg]]

**Regla de la hoja.** La mayor de tres condiciones, redondeada hacia arriba al múltiplo elegido (5 cm):

$$\ell_{ext}=\max\begin{cases}k\,\ell_n & k=0.22\ \text{(franja central)},\ 0.30\ \text{(franja de columna)}\\[2pt] x_{PI}+\max(d,\ 12d_b,\ \ell_n/16)\\[2pt] \ell_d\end{cases}$$

| Condición | De dónde sale |
|---|---|
| Fracción de $\ell_n$ | Fig. 8.7.4.1.3: longitudes mínimas para losas sin vigas. En losas con vigas la hoja las adopta como mínimo práctico. Si los claros adyacentes difieren se usa el mayor (§8.7.4.1.3b) |
| Punto de inflexión | $x_{PI}$ es la distancia de la cara del apoyo al punto donde el momento del marco equivalente cambia de signo. A partir de ahí la barra ya no es necesaria y se prolonga máx($d$, $12d_b$, $\ell_n/16$) (§7.7.3.3 y §7.7.3.8.4) |
| $\ell_d$ | La barra debe poder desarrollar $f_y$ en la cara del apoyo, donde el momento es máximo |

**Largo total de la barra.** Apoyo interior: extensión izquierda + ancho de la columna + extensión derecha. Apoyo de borde: extensión + la parte dentro del apoyo hasta el recubrimiento exterior, terminada en [[Gancho estándar ldh]].

**Relación con el criterio de clase.** Es el mismo razonamiento visto para vigas: se ubica dónde la barra deja de ser necesaria y se prolonga $d$ o $12d_b$. La regla empírica de $L/4$ a $L/3$ queda como comprobación de orden de magnitud.

**Qué cambia según el caso.** En losas sin vigas, además, al menos la mitad de los bastones de la franja de columna deben extenderse no menos de $5d$ (ACI 318-19, Fig. 8.7.4.1.3), y con patrones de carga viva el punto de inflexión se aleja del apoyo.

**En la HT1 (dirección X, eje F, franja central).** Hacia E: máx(0.22 × 6.20 = 1.36; 1.12 + 0.275 = 1.39; 0.36) → 1.40 m. Hacia I: máx(1.36; 1.06 + 0.39 = 1.44; 0.36) → 1.45 m. Barra: 1.40 + 0.50 + 1.45 = **3.35 m**.

**Referencia.** ACI 318-19 §8.7.4.1, Fig. 8.7.4.1.3, §7.7.3.3 y §7.7.3.8.4.

Se usa en: [[S11 Detallado del refuerzo]]
