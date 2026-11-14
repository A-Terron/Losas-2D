---
tags: [losas-2d, concepto, ddm]
---
# Reparto entre viga y losa

**Qué es.** La división del momento de la franja de columna entre la viga y la losa que la acompaña.

**Fórmula.**

$$M_{viga} = 0.85\,\min\!\left(\frac{\alpha_{f1}\ell_2}{\ell_1},\ 1\right) M_{fc}\qquad M_{losa,fc} = M_{fc} - M_{viga}$$

**Por qué.** Una viga rígida atrae casi todo el momento de su franja; el 15 % restante lo toma la losa a los lados. Si la viga es flexible ($\alpha_{f1}\ell_2/\ell_1$ < 1) toma menos, en proporción lineal.

**Consecuencia práctica.** En una losa sobre vigas rígidas, la losa de la franja de columna recibe muy poco momento y casi siempre se arma con acero mínimo.

**Además.** La viga resiste los momentos de las cargas aplicadas directamente sobre ella (muros, su propio peso).

**En la HT1.** Eje 6, eje I: franja de columna 13.03 → viga 11.07, losa 1.95 tonf·m.

**Referencia.** ACI 318-14 §8.10.5.7.

Se usa en: [[S05 Método de Diseño Directo]] · Relacionado: [[Peso del alma de las vigas]]
