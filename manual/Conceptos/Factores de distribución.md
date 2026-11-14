---
tags: [losas-2d, concepto, efm]
---
# Factores de distribución

**Qué es.** La fracción del momento desequilibrado de un nudo que toma cada miembro que llega a él.

![[F17-factores-de-distribucion.svg]]

**Fórmula.**

$$FD_i = \frac{K_i}{\sum K} = \frac{K_i}{K_{sb,izq} + K_{sb,der} + K_{ec}}$$

**Por qué.** Al soltar un nudo, todos los miembros giran lo mismo; cada uno toma momento en proporción a su rigidez.

**Cómo.** En cada nudo los FD suman 1. El FD de la columna equivalente indica cuánto momento se va a las columnas.

**En la HT1 (eje 6).** Nudo E: losa 0.711, columna 0.289. Nudo F: 0.469 / 0.340 / 0.191. Nudo I: 0.390 / 0.390 / 0.219. Nudo K: 0.640 / 0.360.

Se usa en: [[Distribución de momentos (Hardy Cross)]] · [[S06 Método del Marco Equivalente]]
