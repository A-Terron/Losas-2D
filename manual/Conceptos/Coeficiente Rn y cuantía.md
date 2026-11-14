---
tags: [losas-2d, concepto, flexion]
---
# Coeficiente Rn y cuantía

**Qué es.** El camino directo del momento al acero requerido.

![[F18-flexion-ancho-unitario.svg]]

**Fórmulas.**

$$R_n = \frac{m_u}{\phi\,b\,d^2}\qquad \rho = \frac{0.85f'_c}{f_y}\left(1 - \sqrt{1 - \frac{2R_n}{0.85f'_c}}\right)\qquad A_s = \rho\,b\,d$$

**De dónde sale.** Del equilibrio de la sección: $C = T \Rightarrow 0.85f'_c\,a\,b = A_s f_y$, y $M_n = A_s f_y (d - a/2)$. Al sustituir $a$ y despejar $\rho = A_s/(bd)$ queda una ecuación de segundo grado cuya raíz es la expresión de arriba.

**Variables.** $m_u$ momento último por unidad de ancho; $b$ ancho unitario (1 m, 1 ft o 1 in, coherente con $m_u$); $\phi$ = 0.90.

**Señal de alarma.** Si $1 - 2R_n/(0.85f'_c) < 0$ la sección no alcanza: hay que aumentar $h$.

**En la HT1.** $m_u$ = 1.26 tonf·m/m, $d$ = 11.57 cm → $R_n$ = 10.45 kgf/cm², $\rho$ = 0.00253, $A_s$ = 2.93 cm²/m.

**Referencia.** ACI 318-19 §22.2 y §22.3.

Se usa en: [[S08 Diseño por flexión]] · Relacionado: [[Resistencia de diseño a flexión]]
