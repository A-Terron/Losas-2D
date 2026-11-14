---
tags: [losas-2d, concepto, ddm]
---
# Porcentajes de la franja de columna

**Qué es.** La parte del momento del marco que se asigna a la franja de columna.

![[F09-reparto-transversal.svg]]

| Sección | $\alpha_{f1}\ell_2/\ell_1$ | $\beta_t$ | $\ell_2/\ell_1$ = 0.5 | 1.0 | 2.0 |
|---|---|---|---|---|---|
| Negativo interior | 0 | — | 75 | 75 | 75 |
| | ≥ 1 | — | 90 | 75 | 45 |
| Negativo exterior | 0 | 0 | 100 | 100 | 100 |
| | 0 | ≥ 2.5 | 75 | 75 | 75 |
| | ≥ 1 | 0 | 100 | 100 | 100 |
| | ≥ 1 | ≥ 2.5 | 90 | 75 | 45 |
| Positivo | 0 | — | 60 | 60 | 60 |
| | ≥ 1 | — | 90 | 75 | 45 |

**Cómo.** Interpolación lineal en cada variable (hasta tres interpolaciones en el negativo exterior).

**Por qué.** Sin vigas, la franja de columna toma 60 a 75 % por ser más rígida. Con vigas rígidas, el reparto depende de la forma del tablero: si es alargado en sentido transversal, las vigas transversales se llevan más carga y la franja de columna menos.

**En la HT1.** Eje 6, claro F–I: $\ell_2/\ell_1$ = 0.80 → 90 − 15 × (0.30/0.50) = 81 %.

**Referencia.** ACI 318-14 §8.10.5.1, §8.10.5.2 y §8.10.5.5.

Se usa en: [[S05 Método de Diseño Directo]] · [[S06 Método del Marco Equivalente]] · Relacionado: [[Rigidez torsional beta t]]
