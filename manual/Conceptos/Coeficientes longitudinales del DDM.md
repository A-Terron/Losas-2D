---
tags: [losas-2d, concepto, ddm]
---
# Coeficientes longitudinales del DDM

**Qué es.** Las fracciones de $M_o$ que van a cada momento negativo y al positivo.

![[F08-coeficientes-longitudinales.svg]]

**Claro interior.** 0.65 a cada negativo y 0.35 al positivo.

**Claro extremo.**

| Caso | $M^-$ exterior | $M^+$ | $M^-$ interior |
|---|---|---|---|
| Borde exterior no restringido | 0 | 0.63 | 0.75 |
| Vigas entre todos los apoyos | 0.16 | 0.57 | 0.70 |
| Sin vigas interiores, sin viga de borde | 0.26 | 0.52 | 0.70 |
| Sin vigas interiores, con viga de borde | 0.30 | 0.50 | 0.70 |
| Borde exterior totalmente restringido | 0.65 | 0.35 | 0.65 |

**Por qué varían.** Dependen de cuánto restringe el giro el apoyo exterior: un muro de concreto lo empotra (0.65); una losa simplemente apoyada sobre un muro de mampostería no lo restringe (0).

**Cómo elige la hoja.** «Vigas entre todos los apoyos» solo si hay viga a lo largo del marco y en todos los ejes transversales; si no, según exista viga de borde. Se puede forzar el caso a mano.

**Detalle.** En un apoyo interior se diseña con el mayor negativo de los dos claros (8.10.4.5).

**Referencia.** ACI 318-14 §8.10.4.1 y Tabla 8.10.4.2.

Se usa en: [[S05 Método de Diseño Directo]]
