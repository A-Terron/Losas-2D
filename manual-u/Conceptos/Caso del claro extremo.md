---
tags: [losas-2d-u, concepto, ddm]
---
# Caso del claro extremo

**Qué es.** La fila de la Tabla 8.10.4.2 (ACI 318-14) que reparte $M_o$ en un claro con un borde discontinuo.

| Caso | $M^-$ exterior | $M^+$ | $M^-$ interior | Cuándo lo elige la hoja |
|---|---|---|---|---|
| Borde no restringido | 0 | 0.63 | 0.75 | Borde exterior sobre muro de mampostería |
| Vigas entre todos los apoyos | 0.16 | 0.57 | 0.70 | El marco tiene viga y todos sus apoyos tienen viga transversal |
| Sin vigas interiores, sin viga de borde | 0.26 | 0.52 | 0.70 | No se cumple lo anterior y el borde exterior no tiene viga |
| Sin vigas interiores, con viga de borde | 0.30 | 0.50 | 0.70 | No se cumple lo anterior y el borde exterior sí tiene viga |
| Totalmente restringido | 0.65 | 0.35 | 0.65 | Borde exterior sobre muro de concreto |

**Por qué.** Cuanto más restringe el borde exterior el giro de la losa, más momento negativo aparece allí y menos positivo queda en el claro.

**Claro interior.** Si los dos extremos son continuos no hay caso que elegir: 0.65 / 0.35 / 0.65.

**Forzarlo.** Los selectores «Caso del claro extremo · X / Y» de la sección 6 sustituyen la detección automática.

**En la hoja.** Secciones 4 y 6. Explicación de los coeficientes: [Coeficientes longitudinales del DDM](https://a-terron.github.io/Losas-2D/manual/Conceptos/Coeficientes%20longitudinales%20del%20DDM/).
