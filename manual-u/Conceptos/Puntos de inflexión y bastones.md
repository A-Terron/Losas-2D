---
tags: [losas-2d-u, concepto, detallado]
---
# Puntos de inflexión y bastones

**Qué es.** El punto donde el momento cambia de signo marca hasta dónde hace falta el acero superior; el bastón se extiende un poco más.

$$\ell_{ext}=\max\left(k\,\ell_n,\ \ x_{PI}+\max(d,\ 12d_b,\ \ell_n/16),\ \ \ell_d\right)$$

medida desde la cara del apoyo, y redondeada hacia arriba al múltiplo elegido.

| Término | Origen |
|---|---|
| $k\,\ell_n$ | Fracción mínima: 0.30 (franja de columna) y 0.22 (franja central) en dos direcciones, Fig. 8.7.4.1.3; con el claro mayor de los dos adyacentes |
| $x_{PI}+\max(d,12d_b,\ell_n/16)$ | Más allá del punto de inflexión (7.7.3.8.4 y criterio de clase) |
| $\ell_d$ | El bastón debe desarrollarse desde la cara |

**De dónde sale $x_{PI}$.**

- **Dos direcciones:** de la envolvente de momentos del Marco Equivalente (todos los patrones) en los dos marcos del tablero; se toma el más alejado de la cara.
- **Una dirección:** de la parábola que pasa por los tres momentos de los coeficientes.

**Diferencia con Losas 2D.** El modelo envuelve los puntos de inflexión de los **cuatro** marcos de cada dirección; esta hoja solo conoce los dos del tablero. La extensión puede variar un múltiplo de redondeo (5 cm).

**Apoyo exterior.** El bastón termina en gancho estándar; la hoja comprueba que $\ell_{dh}$ quepa en el ancho de la viga o columna menos el recubrimiento.

**En la hoja.** Sección de detallado y vistas «Bastones» y «Sección con armado». Ver [Extensión de bastones](https://a-terron.github.io/Losas-2D/manual/Conceptos/Extensi%C3%B3n%20de%20bastones/).
