---
tags: [losas-2d, concepto, materiales]
---
# Factor beta1

**Qué es.** La relación entre la profundidad del bloque rectangular de compresión $a$ y la profundidad real del eje neutro $c$: $a = \beta_1 c$.

**Fórmula.**

$$\beta_1 = 0.85\ \ (f'_c \le 4000\text{ psi});\qquad \beta_1 = 0.85 - 0.05\,\frac{f'_c - 4000}{1000}\ \ge 0.65$$

**Por qué.** El diseño usa un bloque rectangular de esfuerzo $0.85f'_c$ en lugar de la curva real; $\beta_1$ ajusta su altura para que la fuerza y su posición sean equivalentes.

**Cuándo.** Al comprobar $\varepsilon_t$, porque la deformación depende de $c$, no de $a$.

**En la HT1.** 0.85.

**Referencia.** ACI 318-19 Tabla 22.2.2.4.3.

Se usa en: [[Sección controlada por tensión]] · [[S08 Diseño por flexión]]
