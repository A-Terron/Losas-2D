---
tags: [losas-2d, concepto, flexion]
---
# Separación de barras

**Qué es.** La distancia entre centros de barras paralelas que da el acero requerido.

![[F20-separacion-de-barras.svg]]

**Fórmulas.**

$$s_{req} = \frac{A_b}{A_s}\qquad s_{máx} = \min(2h,\ 18\text{ in})\ \text{en secciones críticas}\qquad s_{libre} \ge \max(1\text{ in},\ d_b,\ \tfrac43 d_{agg})$$

**Cómo se adopta.** $s = \min(s_{req}, s_{máx})$ redondeada a múltiplos de **2.5 cm**.

> [!warning] Hacia abajo, no al más cercano
> Menos separación = más acero. Redondear **hacia abajo** siempre cumple. Redondear hacia arriba puede dejar menos acero que el requerido: con #3 y $A_{s,mín}$ = 2.70 cm²/m, $s_{req}$ = 26.3 cm; a 27.5 cm quedan 2.58 cm²/m (no cumple) y a 25 cm quedan 2.84 cm²/m (cumple).

**Según el caso.** Fuera de las secciones críticas el máximo es mín(3$h$, 18 in). Si la separación baja de unos 10 cm conviene una barra de mayor diámetro.

**En la HT1.** $s_{máx}$ = 30 cm; resultado #3 @ 25, @ 22.5 y @ 20 cm.

**Referencia.** ACI 318-19 §8.7.2.2 y §25.2.1.

Se usa en: [[S08 Diseño por flexión]]
