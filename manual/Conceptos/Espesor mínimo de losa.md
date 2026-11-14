---
tags: [losas-2d, concepto, sistema]
---
# Espesor mínimo de losa

**Qué es.** El espesor que, sin calcular deflexiones, el Código acepta como suficiente.

**Fórmulas.** Con $\ell_n$ = claro libre largo y $f_y$ en psi:

$$\alpha_{fm} > 2:\quad h \ge \frac{\ell_n(0.8 + f_y/200\,000)}{36 + 9\beta}\ \ge 3.5\text{ in}$$

$$0.2 < \alpha_{fm} \le 2:\quad h \ge \frac{\ell_n(0.8 + f_y/200\,000)}{36 + 5\beta(\alpha_{fm}-0.2)}\ \ge 5\text{ in}$$

$$\alpha_{fm} \le 0.2\ \text{o sin vigas en los cuatro lados}:\quad h \ge \frac{\ell_n}{30\ \text{a}\ 33}\ \ge 5\text{ in}\quad (f_y = 60\text{ ksi})$$

**Por qué.** Limitar la esbeltez controla las flechas. Con vigas rígidas la losa puede ser más delgada.

**Cuándo no basta.** Cargas sostenidas inusualmente altas o concreto de módulo bajo: hay que calcular deflexiones (R8.3.1).

**Según el caso.** Borde discontinuo con viga de borde de $\alpha_f$ < 0.8: +10 %. Si $h < h_{mín}$ se puede seguir solo demostrando que las deflexiones cumplen (8.3.2).

**En la HT1.** 14.73 cm (tablero T2) → se usa 15 cm.

**Referencia.** ACI 318-19 §8.3.1.1, §8.3.1.2, §8.3.1.2.1 y §8.3.2.

Se usa en: [[S04 Rigidez de vigas y espesor mínimo]] · Relacionado: [[Relación de claros beta]] · [[Rigidez relativa alfa f]]
