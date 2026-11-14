---
tags: [losas-2d, concepto, sistema]
---
# Sección efectiva de viga

**Qué es.** La viga más el tramo de losa que trabaja con ella como patín.

![[F03-seccion-efectiva-viga.svg]]

**Fórmula.**

$$p = \min(h_b - h,\ 4h)\qquad b_f = b_w + 2p\ \text{(interior)}\quad b_f = b_w + p\ \text{(borde)}$$

**Variables.** $h_b$ peralte total de la viga; $h$ espesor de losa; $b_w$ ancho del alma; $p$ vuelo de patín a cada lado.

**Por qué.** Viga y losa se cuelan monolíticamente: al flexionarse la viga arrastra parte de la losa. El Código limita cuánta.

**Cómo.** Con $b_f$ se calculan el centroide y la inercia $I_b$ por ejes paralelos, y la constante torsional $C$.

**Según el caso.** Viga de borde: patín a un solo lado (sección L). Viga muy peraltada: manda $4h$.

**En la HT1.** $p$ = mín(45, 60) = 45 cm; $b_f$ = 125 cm (interior) y 80 cm (borde); $I_b$ = 1 071 318 y 901 254 cm⁴.

**Referencia.** ACI 318-19 §8.4.1.8 y Fig. R8.4.1.8.

Se usa en: [[Rigidez relativa alfa f]] · [[Constante torsional C]] · [[S04 Rigidez de vigas y espesor mínimo]]
