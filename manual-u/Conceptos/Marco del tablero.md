---
tags: [losas-2d-u, concepto, efm]
---
# Marco del tablero

**Qué es.** El marco plano que la hoja arma sobre cada borde del tablero para analizarlo: el claro del tablero más los vecinos descritos.

![[U11-marco-del-tablero.svg]]

**Cómo se arma.** A cada lado del tablero puede haber hasta dos claros vecinos. El extremo del marco queda de una de estas formas:

| Lo que indicas | Extremo del marco |
|---|---|
| Borde discontinuo | Apoyo exterior del propio tablero |
| Vecino «es el último» | Apoyo exterior después del vecino (columna con su viga de borde a torsión) |
| Vecino «último, borde no restringido» | Apoyo exterior con giro libre y momento nulo |
| «Hay más tableros» y das el 2.º vecino | Se agrega ese claro; termina en apoyo exterior o empotrado según indiques |
| «Hay más tableros» sin 2.º vecino | **Empotrado** en el apoyo lejano del vecino |

**Por qué se puede empotrar.** ACI 318-14 §8.11.2.5 permite analizar un tramo por separado suponiendo la losa-viga empotrada en un apoyo situado a dos tableros de distancia, siempre que la losa continúe más allá. El efecto de un claro lejano sobre el apoyo en estudio se amortigua rápido.

**Cuánto cambia.** En la HT1, quitar el segundo vecino y empotrar cambia los momentos del EFM hasta 5 %. Con el segundo vecino la hoja reproduce el marco completo sin diferencia.

**En el DDM.** El marco solo sirve para dos cosas: contar los claros (limitación de tres) y saber qué coeficiente trae el vecino al apoyo compartido (0.65 si es interior, 0.70 si es extremo, 0.75 si su borde no está restringido).

**En la hoja.** Secciones 4 (composición del marco) y 7. Ver [[S07 Método del Marco Equivalente]].
