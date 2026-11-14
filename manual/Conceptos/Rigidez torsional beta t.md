---
tags: [losas-2d, concepto, ddm]
---
# Rigidez torsional beta t

**Qué es.** La rigidez a torsión de la viga de borde frente a la rigidez a flexión de la losa del marco.

**Fórmula.**

$$\beta_t = \frac{E_{cb}\,C}{2\,E_{cs}\,I_s}$$

**Variables.** $C$ de la [[Constante torsional C]] de la viga de borde transversal al marco; $I_s = \ell_2 h^3/12$ del marco.

**Por qué.** En el apoyo exterior, la losa de la franja central solo puede transmitir su momento a la columna a través de la viga de borde, que se tuerce. Si esa viga es flexible a torsión ($\beta_t$ ≈ 0), casi todo el momento exterior se concentra en la franja de columna (100 %). Si es rígida ($\beta_t$ ≥ 2.5), se reparte como en un apoyo interior.

**Cuándo.** Solo en la sección de momento negativo exterior.

**En la HT1.** Eje 6: 582 362 / (2 × 150 750) = 1.93 → 78.5 % a la franja de columna.

**Referencia.** ACI 318-14 §8.10.5.2.

Se usa en: [[Porcentajes de la franja de columna]]
