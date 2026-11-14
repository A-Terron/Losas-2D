---
tags: [losas-2d, concepto, efm]
---
# Rigidez de la losa-viga Ksb

**Qué es.** El momento necesario para girar una unidad el extremo de la losa-viga con el otro extremo empotrado.

**Fórmula.**

$$K_{sb} = \frac{k\,E_{cs}\,I_{sb}}{\ell_1}$$

**Variables.** $I_{sb}$: inercia bruta de la sección completa del marco (losa de ancho $\ell_2$ más el alma de la viga, respecto a su centroide); $k$ del [[Miembro no prismático]].

**Por qué bruta.** El Código permite usar el área bruta del concreto para las rigideces del análisis (318-14 §8.11.3.1).

**Según el caso.** Sin viga: $I_{sb} = \ell_2 h^3/12$.

**En la HT1.** Eje 6: $I_{sb}$ = 1 601 835 cm⁴; $K_{sb}$ = 25 017 tonf·m en F–I y 34 579 tonf·m en E–F (claro más corto, más rígido).

**Referencia.** ACI 318-14 §8.11.3.

Se usa en: [[S06 Método del Marco Equivalente]] · [[Factores de distribución]]
