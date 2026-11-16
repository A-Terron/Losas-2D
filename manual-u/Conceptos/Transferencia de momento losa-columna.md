---
tags: [losas-2d-u, concepto, punzonamiento]
---
# Transferencia de momento losa–columna

**Qué es.** El momento desbalanceado $M_{sc}$ que la losa pasa a la columna, repartido entre flexión y excentricidad de cortante.

**Reparto (8.4.2.2.2 y 8.4.4.2.2).**

$$\gamma_f=\frac{1}{1+\tfrac23\sqrt{b_1/b_2}}\qquad \gamma_v=1-\gamma_f$$

$b_1$ es el lado de la sección crítica paralelo al claro y $b_2$ el perpendicular. Con sección cuadrada, $\gamma_f$ = 0.60 y $\gamma_v$ = 0.40.

**La parte de cortante** aumenta el esfuerzo en la cara más cargada:

$$\Delta v=\frac{\gamma_v\,M_{sc}\,c}{J_c}$$

con $J_c$ la propiedad de la sección crítica análoga al momento polar de inercia:

- Interior: $J_c=\dfrac{d\,b_1^3}{6}+\dfrac{b_1d^3}{6}+\dfrac{d\,b_2b_1^2}{2}$, con $c=b_1/2$.
- De borde y de esquina: se calcula respecto al centroide de las caras que existen, y $c$ es la distancia a la cara interior.

**La parte de flexión** $\gamma_fM_{sc}$ debe resistirla el acero colocado dentro de $b_{slab}=c_2+3h$ (1.5$h$ a cada lado de la columna; 8.4.2.2.3).

**Cuánto vale $M_{sc}$** (ACI 318-14 §8.10.7):

- Columna exterior en esa dirección: $0.3\,M_o$.
- Columna interior: $0.07\left[(q_{Du}+0.5\,q_{Lu})\,\ell_2\ell_n^2-q_{Du}'\ell_2'(\ell_n')^2\right]$, el desbalance de cargar con media carga viva solo el claro mayor.

La hoja suma el efecto de las dos direcciones.

**En la hoja.** Sección de punzonamiento. Ver [[S11 Punzonamiento]].
