---
tags: [losas-2d-u, concepto, franjas]
---
# Franjas del tablero

**Qué es.** La forma en que los momentos de los marcos se convierten en momentos por metro dentro de un tablero.

![[U01-planta-apoyos-franjas.png]]

**Geometría.** En cada dirección el tablero tiene:

- Dos **medias franjas de columna**, una pegada a cada borde paralelo a la dirección, de ancho un cuarto del menor de $\ell_1$ y $\ell_2$.
- Una **franja central** entre ellas.

Cada media franja de columna pertenece al marco de su borde. La franja central es la suma de media franja central de un marco y media del otro.

**Momento por metro.**

$$m_{u,col}=\frac{M_{losa\ en\ franja\ de\ columna}}{b_{fc}-b_w}\qquad m_{u,cen}=\frac{f_1M_{cen,1}+f_2M_{cen,2}}{b_{cen}}$$

$f_i$ es la fracción de la franja central del marco $i$ que cae dentro del tablero: 1 en un marco de borde, y la proporción de anchos en un marco interior.

**En el apoyo.** El acero superior sobre un apoyo continuo cubre los dos tableros; se arma con el mayor momento por metro de los dos lados.

**Diferencia con Losas 2D.** Ninguna en el resultado: allí se calculan los cuatro marcos de cada dirección y luego se arma cada tablero; aquí solo los dos marcos que tocan el tablero.

**En la hoja.** Sección 8 y vista «Apoyos y franjas» de la planta. Ver [Franja de columna y franja central](https://a-terron.github.io/Losas-2D/manual/Conceptos/Franja%20de%20columna%20y%20franja%20central/).
