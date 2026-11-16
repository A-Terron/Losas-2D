---
tags: [losas-2d-u, concepto, apoyos]
---
# Tipos de apoyo de borde

**Qué es.** Lo que sostiene la losa a lo largo de cada uno de los cuatro bordes del tablero.

| Apoyo | Cómo lo trata la hoja |
|---|---|
| **Viga** ($b_w\times h_b$) | Sección efectiva en T o L; aporta $\alpha_f$, constante torsional $C$ y toma parte del momento de la franja de columna. Si $h_b\le h$ se ignora |
| **Muro de concreto** | Apoyo lineal rígido ($\alpha_f=\infty$), monolítico: en un borde discontinuo equivale a un extremo totalmente restringido; impide el giro en el marco equivalente |
| **Muro de mampostería** | Apoyo lineal rígido pero sin continuidad: borde no restringido, giro libre, momento negativo nulo |
| **Sin viga** | Eje de columnas: la losa descarga directamente en ellas ($\alpha_f=0$) y hay que revisar punzonamiento |
| **Borde libre** | Sin apoyo. Solo se admite en dos lados opuestos, y la losa pasa a ser de una dirección |

**Sistema de piso que resulta.**

| Bordes con viga o muro | Sistema |
|---|---|
| Los cuatro | Losa apoyada en vigas o muros |
| Ninguno | Placa plana |
| Solo los discontinuos | Losa sin vigas interiores, con viga de borde |
| Otra combinación | Mixto: cada marco se analiza con la viga que tiene |

**En la hoja.** Tabla «Bordes del tablero» de la sección 2. Ver también [[Apoyo en muro]].
