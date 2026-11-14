---
tags: [losas-2d, concepto, efm]
---
# Distribución de momentos (Hardy Cross)

**Qué es.** Un método iterativo para resolver marcos sin plantear ecuaciones: se empotran todos los nudos y se van soltando uno por uno.

**Pasos.**

1. **Momentos de empotramiento** en cada extremo: $M_{emp} = m\,w\,\ell_1^2$ (negativo a la izquierda, positivo a la derecha, con la convención horario positivo).
2. **Desequilibrio** de cada nudo: suma de los momentos de los extremos que llegan a él.
3. **Distribución:** cada extremo recibe $-FD \times$ desequilibrio.
4. **Transporte:** cada momento distribuido pasa FT × su valor al extremo opuesto del mismo miembro.
5. Repetir 2 a 4 con los momentos transportados hasta que sean despreciables.
6. **Sumar** cada columna de la tabla: momentos finales en los ejes.

**Por qué funciona.** Cada ciclo corrige el error del anterior; como FD < 1 y FT ≈ 0.5, los valores se reducen rápidamente.

**Detalles.** La parte que toma la columna equivalente no regresa al marco. Con miembros no prismáticos se usan sus propios FT y $m$ (ver [[Miembro no prismático]]).

**En la HT1.** Converge en 21 ciclos; la hoja muestra los cinco primeros y el total, que coincide con la solución matricial.

Se usa en: [[S06 Método del Marco Equivalente]] · Relacionado: [[Factores de distribución]]
