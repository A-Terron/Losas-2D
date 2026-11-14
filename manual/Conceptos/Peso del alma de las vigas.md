---
tags: [losas-2d, concepto, cargas]
---
# Peso del alma de las vigas

**Qué es.** El peso de la parte de la viga que cuelga bajo la losa: $w_{alma} = b_w\,(h_b - h)\,\gamma_c$ por metro.

**Dos formas de tratarlo.**

| Opción | Efecto |
|---|---|
| Directo a la viga | No entra en el momento que se reparte a la losa. La viga resiste, además de su parte del marco, lo que le llega directamente. |
| Repartido en el marco | Se divide entre $\ell_2$ y se suma a la carga por área. Aumenta los momentos de la losa (conservador). |

**Por qué existe la duda.** El Código dice que las vigas resisten además los momentos de las cargas aplicadas directamente sobre ellas, incluido el peso del alma (318-14 §8.10.5.7.2). Los ejemplos de PCA y StructurePoint lo reparten por simplicidad.

**En la HT1.** 0.35 × 0.45 × 2400 = 378 kgf/m por viga; repartido en 5.36 m serían 70 kgf/m² más.

Se usa en: [[S03 Cargas]] · [[S10 Deflexiones]] (ahí siempre se incluye, porque es carga real del marco)
