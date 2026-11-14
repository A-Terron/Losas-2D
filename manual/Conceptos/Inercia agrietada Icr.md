---
tags: [losas-2d, concepto, deflexiones]
---
# Inercia agrietada Icr

**Qué es.** La inercia de la sección cuando el concreto en tensión ya no trabaja: solo cuentan el concreto comprimido y el acero, este último convertido a concreto equivalente con la [[Relación modular n]].

**Cómo se calcula (sección T, compresión arriba).**

1. Se busca la profundidad del eje neutro $c$ igualando momentos estáticos:

$$\underbrace{b_f\,\frac{c^2}{2}}_{\text{concreto comprimido}}=\sum n\,A_{s,i}\,(d_i-c)\qquad (\text{si } c\le h_f)$$

2. Con $c$ conocido:

$$I_{cr}=\frac{b_f\,c^3}{3}+\sum n\,A_{s,i}\,(d_i-c)^2$$

Si $c$ cae por debajo del patín se añade el alma: el término de concreto pasa a $b_f h_f (c-h_f/2)+b_w (c-h_f)^2/2$ en el paso 1 y a $b_f h_f^3/12+b_f h_f (c-h_f/2)^2+b_w (c-h_f)^3/3$ en el paso 2.

![[F23-seccion-agrietada.svg]]

**Qué acero entra.** El acero de losa **colocado** dentro del ancho del marco y el acero de la viga. Como las vigas no se diseñan en este proyecto, la hoja estima su acero con el momento último de la viga, sin bajar del mínimo de vigas ($3\sqrt{f'_c}/f_y$ y $200/f_y$).

**Qué cambia según el caso.** En los apoyos la compresión está abajo: la sección es el rectángulo del alma y el acero en tensión es el superior. Sin vigas, la sección es la losa de ancho $\ell_2$.

**En la HT1 (eje 6, claro I–K, centro).** $c$ = 3.58 cm (dentro del patín de 15 cm) e $I_{cr}$ = **141 734 cm⁴**, apenas el 9 % de $I_g$. Con tan poco acero, agrietarse cuesta casi toda la rigidez.

**Referencia.** Mecánica de la sección transformada; ACI 318-19 §24.2.3.5.

Se usa en: [[S10 Deflexiones]] · [[Inercia efectiva Ie]]
