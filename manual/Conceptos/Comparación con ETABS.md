---
tags: [losas-2d, concepto, verificacion]
---
# Comparación con ETABS

**Qué es.** La tabla de la sección 12 donde se escriben los resultados de ETABS para contrastarlos con la hoja y con el FEM interno.

**Qué preparar en ETABS.**

1. Quitar las vigas secundarias de 30 × 50 cm.
2. Poner la losa de 15 cm (el modelo original tiene 10 cm).
3. Verificar cargas: sobrecarga muerta 50 kgf/m², viva 250 kgf/m².
4. Dividir los tableros en las intersecciones con las vigas y mallar.
5. Correr la combinación 1.2D + 1.6L para momentos y D + L para flechas.

**Qué leer.**

| Resultado | Dónde | Se compara con |
|---|---|---|
| M11 en el centro del tablero | Momento por unidad de ancho en dirección X | $m_x^+$ de la franja central |
| M22 en el centro del tablero | Ídem en dirección Y | $m_y^+$ de la franja central |
| Flecha | Centro menos promedio de las dos vigas de apoyo | [[Flecha relativa a las vigas]] |

Comprobar que el eje local 1 de las losas apunta en X; si no, M11 y M22 están intercambiados.

**Cómo interpretar las diferencias.**

- El FEM reparte más momento a la losa que el DDM y el EFM, sobre todo en la dirección corta: los métodos manuales asignan a las vigas un porcentaje fijo.
- ETABS con modificadores 0.25 / 0.35 da más momento a las vigas que el FEM con secciones brutas.
- Diferencias de 10 a 30 % entre métodos son normales. Lo que importa es que la resistencia colocada cubra el mayor valor.

**En la HT1.** En la dirección Y el FEM da hasta 0.79 tonf·m/m en el centro, por debajo de $\phi m_n$ = 1.22 tonf·m/m del acero mínimo (#3 @ 25 cm).

**Referencia.** Enunciado del proyecto, §5 (el FEM es verificación independiente) y criterio de clase.

Se usa en: [[S12 Verificación FEM y ETABS]] · [[Modificadores de rigidez]]
