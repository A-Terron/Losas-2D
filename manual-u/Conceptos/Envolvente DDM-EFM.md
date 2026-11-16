---
tags: [losas-2d-u, concepto, momentos]
---
# Envolvente DDM–EFM

**Qué es.** Diseñar cada sección con el mayor de los momentos que dan el Método de Diseño Directo y el Marco Equivalente.

**Por qué los dos métodos difieren.**

| El DDM… | El EFM… |
|---|---|
| Usa coeficientes fijos, iguales para cualquier columna | Usa la rigidez real de columnas y vigas de borde |
| Toma el momento en la cara, con el claro libre | Resuelve en ejes y baja a la cara |
| Iguala los negativos de un apoyo tomando el mayor | Equilibra el nudo según rigideces |
| No ve los patrones de carga viva | Los revisa cuando $L/D>0.75$ |

**Qué suele pasar.** Con columnas flexibles (altas, sin columna superior) el EFM da menos momento negativo exterior y más negativo en el primer apoyo interior y más positivo. En la HT1 el EFM gobierna en el eje I y el DDM en el eje F y en los bordes.

**Cuándo usar cada opción.**

- **Envolvente** (por defecto): cubre los dos análisis; es lo que usa el modelo de la HT1.
- **EFM:** cuando el tablero no cumple las limitaciones del DDM (menos de tres claros, claros muy distintos, relación mayor que 2 sin vigas).
- **DDM:** para comparar con un cálculo a mano.

**En la hoja.** Sección 8. Ver [[S08 Momentos de diseño]].
