---
tags: [losas-2d, concepto, deflexiones]
---
# Deflexión a largo plazo

**Qué es.** La flecha adicional que aparece con los años por flujo plástico y contracción del concreto bajo cargas **sostenidas**.

**Fórmula.**

$$\lambda_\Delta=\frac{\xi}{1+50\rho'}\qquad \Delta_{LP}=\lambda_\Delta\,\Delta_{i,sost}$$

| Duración de la carga | $\xi$ |
|---|---|
| 3 meses | 1.0 |
| 6 meses | 1.2 |
| 12 meses | 1.4 |
| 5 años o más | 2.0 |

**Variables.** $\rho'$ cuantía de acero de compresión en el centro del claro; $\Delta_{i,sost}$ flecha inmediata por carga sostenida $w_D+\psi\,w_L$.

**Por qué.** El concreto comprimido sigue acortándose bajo carga constante; el acero de compresión frena ese efecto, por eso divide. Una losa no lleva acero de compresión: $\rho'$ = 0 y $\lambda_\Delta=\xi$ = 2.

**Qué cambia según el caso.** $\psi$ depende del uso: 0.25 en parqueos, viviendas, oficinas y aulas (criterio de clase); más alto en bodegas o archivos. En ETABS esto equivale a la combinación 2·D + 2·SCM + (1 + 2ψ)·L = 2D + 1.5L.

**Error típico.** Multiplicar por $\lambda_\Delta$ la flecha total. Solo se amplifica la parte sostenida.

**En la HT1 (T6).** $\Delta_{i,sost}$ = 0.27 cm → $\Delta_{LP}$ = 2 × 0.27 = **0.53 cm**.

**Referencia.** ACI 318-19 §24.2.4.1.1 y Tabla 24.2.4.1.3.

Se usa en: [[S10 Deflexiones]] · [[Límites de deflexión]]
