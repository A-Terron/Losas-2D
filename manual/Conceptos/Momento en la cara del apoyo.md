---
tags: [losas-2d, concepto, efm]
---
# Momento en la cara del apoyo

**Qué es.** El momento negativo con el que se diseña: no el del eje de la columna, sino el de la sección crítica.

![[F16-momento-en-la-cara.svg]]

**Fórmulas.** Con los momentos en los ejes y la carga $w$ del claro:

$$V_{izq} = \frac{w\,\ell_1}{2} + \frac{M_{der} - M_{izq}}{\ell_1}\qquad M(x) = M_{izq} + V_{izq}\,x - \frac{w\,x^2}{2}$$

$$x_{cara} = \frac{c_1}{2}\ \ (\text{apoyo interior: } \le 0.175\,\ell_1)\qquad x_{M^+} = \frac{V_{izq}}{w}$$

**Por qué.** Dentro del apoyo la sección es mucho más peraltada y no falla ahí; la sección crítica está donde termina el apoyo.

**Cuándo.** Solo en el EFM (y en el FEM, para comparar en la misma sección). El DDM ya da momentos en la cara porque usa $\ell_n$.

**En la HT1.** Eje 6, claro F–I, apoyo I: 20.98 en el eje → 16.92 tonf·m en la cara.

**Referencia.** ACI 318-19 §8.4.2.1; ACI 318-14 §8.11.6.1 y §8.11.6.2.

Se usa en: [[S06 Método del Marco Equivalente]] · [[Extensión de bastones]] (puntos de inflexión del mismo diagrama)
