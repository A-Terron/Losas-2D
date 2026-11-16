---
tags: [losas-2d-u, indice]
aliases: [Manual Losas 2D U, Inicio U]
---
# Manual técnico · Losas 2D U (losa universal, ACI 318-19)

Este manual explica, paso a paso, todo lo que calcula la hoja **`Losas 2D U - ACI 318-19.html`**: qué fórmula se usa, **por qué**, **cómo** se aplica, **cuándo** corresponde y **qué cambia** según el caso. Está escrito para que puedas repetir cada cálculo a mano.

> [!info] Qué es Losas 2D U
> Es la hoja **universal de un solo tablero**. Tú describes un tablero rectangular, el apoyo de cada uno de sus cuatro bordes y los tableros vecinos; la hoja decide si la losa trabaja en **una** o en **dos direcciones**, identifica el caso y la diseña con el **Método de Diseño Directo (DDM)** y el **Marco Equivalente (EFM)**.
> Su hermana mayor, **Losas 2D**, resuelve la retícula completa de 3 × 3 tableros y agrega la verificación por elementos finitos. Las dos comparten motor de cálculo, unidades y formato.

![[U08-hoja.png]]

## Cómo está organizado

- **Notas de sección (S01 a S14).** Una por cada sección de la hoja, en el mismo orden, con su diagrama de flujo, el procedimiento, las figuras y un ejemplo numérico.
- **Notas de concepto.** Notas cortas con lo que es propio de esta hoja: la clasificación, los vecinos, el marco del tablero, los coeficientes de una dirección, el punzonamiento.
- **Conceptos compartidos.** Lo que ya está explicado en el manual de Losas 2D (rigidez $\alpha_f$, momento estático, columna equivalente, inercia efectiva…) no se repite: cada sección enlaza a esa nota. La lista completa está en [[05 Relación con el manual de Losas 2D]].

## Empieza aquí

1. [[01 Diagrama de flujo general]] — el recorrido completo en una sola vista.
2. [[02 Notación y unidades]] — símbolos, bordes del tablero y sistema de unidades.
3. Las secciones, en orden:

| Hoja | Nota | Qué resuelve |
|---|---|---|
| 1 | [[S01 Materiales]] | $E_c$, $f_r$, $n$, $\beta_1$, $\varepsilon_{ty}$ |
| 2 | [[S02 Tablero, apoyos y continuidad]] | Claros, espesor, apoyo de cada borde, vecinos y columnas |
| 3 | [[S03 Cargas]] | $w_D$, $w_L$, $w_u$ |
| 4 | [[S04 Clasificación del tablero]] | Una o dos direcciones y casos detectados |
| 5 | [[S05 Espesor mínimo]] | $h_{mín}$ con la Tabla 7.3.1.1, 8.3.1.1 u 8.3.1.2 |
| 6 | [[S06 Momentos por DDM o por coeficientes]] | $M_o$ y su reparto (dos direcciones) o coeficientes de §6.5 (una dirección) |
| 7 | [[S07 Método del Marco Equivalente]] | Marco del tablero, rigideces, patrones y envolvente |
| 8 | [[S08 Momentos de diseño]] | DDM frente a EFM y momentos por metro de cada franja |
| 9 | [[S09 Diseño por flexión]] | $A_s$, barra y separación |
| 10 | [[S10 Cortante en una dirección]] | $V_u$ frente a $\phi V_c$ en los dos extremos |
| 11 | [[S11 Punzonamiento]] | $v_u$ frente a $\phi v_c$ en columnas sin viga |
| 12 | [[S12 Deflexiones]] | Inmediata, de largo plazo y límites |
| 13 | [[S13 Detallado del refuerzo]] | $\ell_d$, ganchos, bastones, esquinas |
| 14 | [[S14 Comparación con el modelo completo]] | Los 9 tableros de la HT1 frente a Losas 2D |

En una losa en una dirección las secciones 7, 8 y 11 no aplican y la hoja las oculta; la numeración en pantalla se corre.

4. [[03 Validación]] — contra qué se comprobó la hoja y qué diferencias quedan.
5. [[04 Ejemplos resueltos]] — los números de cada caso precargado, para comprobar tus cálculos.

## Alcance

- Un tablero rectangular de losa maciza con carga de gravedad uniforme, apoyado en vigas, muros o columnas.
- Una dirección: ACI 318-19 Cap. 7 con los coeficientes de §6.5. Dos direcciones: Cap. 8 con DDM y EFM (ACI 318-14 §8.10 y §8.11, que ACI 318-19 §6.2.4.1 sigue permitiendo).
- **No** diseña vigas, muros ni columnas, ni refuerzo de cortante. Tres lados apoyados y uno libre queda fuera del alcance.

> [!warning] Aviso
> Es una herramienta educativa del curso de Estructuras de Concreto Reforzado. Antes de usar los resultados en un diseño real, verifícalos con criterio profesional.
