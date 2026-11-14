---
tags: [losas-2d, concepto, efm]
---
# Miembro a torsión Kt

**Qué es.** La franja transversal al marco (viga transversal o tira de losa) que conecta la losa-viga con la columna y trabaja a torsión.

**Fórmula.**

$$K_t = \sum \frac{9\,E_{cs}\,C}{\ell_2\left(1 - \dfrac{c_2}{\ell_2}\right)^3}\qquad K_{ta} = K_t\,\frac{I_{sb}}{I_s}\ \text{(si hay viga paralela al marco)}$$

**Variables.** $C$: [[Constante torsional C]]; $\ell_2$ y $c_2$ transversales al marco; la suma recorre los brazos a cada lado de la columna (dos en marco interior, uno en marco de borde).

**Por qué.** El momento de la losa lejos de la columna llega a ella torciendo este miembro; si es flexible, la columna «se entera» menos del giro de la losa.

**Por qué la amplificación.** Cuando hay una viga a lo largo del marco, la carga llega a la columna más concentrada y el miembro a torsión trabaja menos: se representa aumentando su rigidez por $I_{sb}/I_s$.

**En la HT1.** Nudo interior del eje 6: $K_t$ = 71 062 tonf·m; $I_{sb}/I_s$ = 10.63; $K_{ta}$ = 755 085 tonf·m.

**Referencia.** ACI 318-14 §8.11.5 y R8.11.5.

Se usa en: [[Columna equivalente Kec]]
