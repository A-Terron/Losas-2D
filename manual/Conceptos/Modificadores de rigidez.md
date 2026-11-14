---
tags: [losas-2d, concepto, verificacion]
---
# Modificadores de rigidez

**Qué son.** Factores que reducen la inercia bruta de losas, vigas y columnas para representar el agrietamiento en un modelo elástico.

| Elemento | Secciones brutas | ETABS de clase |
|---|---|---|
| Losa (flexión) | 1.00 | 0.25 |
| Vigas (inercia) | 1.00 | 0.35 |
| Columnas (inercia) | 1.00 | 0.70 |
| Torsión de vigas | 1.00 | 0.10 |
| Sección de la viga | T compuesta con la losa | Rectangular, sin acción compuesta |

**Por qué hay dos juegos.** El DDM y el EFM usan secciones brutas, así que para comparar **momentos** con ellos el FEM debe usar 1.00. Para comparar con el modelo de ETABS de clase, y para estimar flechas con agrietamiento, se usan los valores reducidos.

**Qué efecto tienen.** Los momentos dependen de las rigideces **relativas**: bajar la losa a 0.25 y las vigas a 0.35 hace a las vigas relativamente más rígidas y les lleva más momento. Las flechas dependen de las rigideces **absolutas**: con 0.25 en la losa crecen casi cuatro veces.

**Cuándo usar cada uno.** Botón «Secciones brutas» para verificar DDM y EFM; botón «Como ETABS de clase» antes de llenar la tabla de comparación con ETABS.

**Referencia.** ACI 318-19 §6.6.3.1.1 (Tabla 6.6.3.1.1(a): 0.25 $I_g$ losas planas, 0.35 $I_g$ vigas, 0.70 $I_g$ columnas) y criterio de clase.

Se usa en: [[S12 Verificación FEM y ETABS]] · [[Comparación con ETABS]]
