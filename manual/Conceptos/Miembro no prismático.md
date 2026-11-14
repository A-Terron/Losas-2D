---
tags: [losas-2d, concepto, efm]
---
# Miembro no prismático

**Qué es.** Un miembro cuya inercia cambia a lo largo de su longitud.

![[F12-losa-viga-no-prismatica.svg]]

**Por qué aparece.** Entre el eje de la columna y su cara, la losa-viga es más rígida: $I = I_{sb}/(1 - c_2/\ell_2)^2$. La columna, dentro del nudo, es infinitamente rígida.

**Consecuencia.** Las constantes clásicas de un miembro prismático dejan de valer:

| Constante | Prismático | No prismático |
|---|---|---|
| Factor de rigidez $k$ ($K = kEI/L$) | 4.00 | > 4 |
| Factor de transporte FT | 0.50 | > 0.5 |
| Coeficiente de empotramiento $m$ ($M = m\,wL^2$) | 0.0833 | > 0.0833 |

**Cómo se obtienen.** Por flexibilidades: se integran $\int (1-\xi)^2/EI$, $\int \xi(1-\xi)/EI$ y $\int \xi^2/EI$ por tramos y se invierte la matriz de 2 × 2. La hoja lo hace numéricamente; a mano se usan las tablas de constantes de PCA (Notes on ACI 318, apéndice del capítulo 20).

**En la HT1.** Claro F–I: $k$ = 4.128, FT = 0.509, $m$ = 0.0843. Columna: $k_c$ = 5.97.

Se usa en: [[Rigidez de la losa-viga Ksb]] · [[Rigidez de la columna Kc]]
