---
tags: [losas-2d, concepto, ddm]
---
# Constante torsional C

**Qué es.** Una medida de la rigidez a torsión de una sección formada por rectángulos.

![[F10-constante-torsional.svg]]

**Fórmula.**

$$C = \sum\left(1 - 0.63\,\frac{x}{y}\right)\frac{x^3\,y}{3}$$

**Variables.** $x$ lado corto e $y$ lado largo de cada rectángulo.

**Cómo.** La sección se divide en rectángulos de las dos maneras posibles (alma a toda la altura más vuelos, o patín corrido más alma bajo la losa) y se toma la que dé el **mayor** $C$.

**Qué sección.** La viga transversal con sus patines (8.4.1.8); si no hay viga, una franja de losa de ancho $c_1$ y espesor $h$.

**Por qué.** La viga transversal se tuerce al transmitir el momento de la losa a la columna; su rigidez a torsión decide cuánto momento negativo llega al apoyo exterior.

**En la HT1.** Viga de borde 35 × 60 con vuelo de 45: 542 369 + 39 994 = 582 362 cm⁴ (la otra subdivisión da 407 362). Viga interior: 622 356 cm⁴.

**Referencia.** ACI 318-14 §8.10.5.2 y §8.11.5.

Se usa en: [[Rigidez torsional beta t]] · [[Miembro a torsión Kt]]
