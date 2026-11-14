---
tags: [losas-2d, concepto, efm]
---
# Rigidez de la columna Kc

**Qué es.** La rigidez a giro del extremo de la columna que llega al nudo.

![[F13-columna-con-zona-rigida.svg]]

**Fórmula.**

$$K_c = \frac{k_c\,E_{cc}\,I_c}{\ell_c}\qquad I_c = \frac{c_2\,c_1^3}{12}$$

**Variables.** $\ell_c$ altura entre ejes de losas (o hasta el empotramiento); $c_1$ lado paralelo al marco.

**Zona rígida.** Dentro del nudo la columna es infinitamente rígida: desde el eje de la losa hasta el fondo de la viga más peraltada ($h_b - h/2$), o $h/2$ sin vigas. Por eso $k_c$ > 4.

**Según el caso.**

- Columna arriba y abajo: se suman las dos, $\sum K_c$.
- Extremo lejano articulado: rigidez reducida, $K = K_{AA} - K_{AB}^2/K_{BB}$.
- Extremo en otra losa: zona rígida de $h/2$ también allí.

**En la HT1.** $I_c$ = 520 833 cm⁴; zona rígida 52.5 cm; $k_c$ = 5.970; $K_c$ = 14 328 tonf·m (solo columna inferior, empotrada).

**Referencia.** ACI 318-14 §8.11.4.

Se usa en: [[Columna equivalente Kec]]
