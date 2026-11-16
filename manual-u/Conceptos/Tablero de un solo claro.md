---
tags: [losas-2d-u, concepto, ddm, efm]
---
# Tablero de un solo claro

**Qué es.** Un tablero con los dos extremos de una dirección discontinuos: no tiene vecinos en esa dirección.

**El problema.** El DDM exige al menos tres claros continuos (§8.10.2.1) y su tabla no tiene una fila para un claro con dos bordes exteriores.

**Qué hace la hoja con el DDM.** Como referencia, pone el coeficiente del borde exterior en los dos apoyos y deja el resto del momento estático en el centro, que es lo que exige la estática:

$$M^+=\left(1-\frac{c_A+c_B}{2}\right)M_o$$

Con vigas (0.16 en cada apoyo) queda 0.84$M_o$ al centro; sobre muros de mampostería, 1.00$M_o$, que es la losa simplemente apoyada. La hoja avisa que las limitaciones no se cumplen.

**Qué conviene.** Diseñar con el **EFM**: el marco de un claro con sus dos columnas exteriores se resuelve sin restricciones. Es lo que trae el ejemplo «tablero aislado sobre cuatro vigas».

**En la hoja.** Secciones 6 y 8.
