---
tags: [losas-2d, concepto, efm]
---
# Momentos de diseño y envolvente

**Qué es.** La elección del momento con que se arma cada sección cuando hay más de un análisis.

**Opciones de la hoja.**

| Opción | Momento de cada sección |
|---|---|
| Envolvente | $\max(M_{DDM},\ M_{EFM})$ |
| DDM | El del Diseño Directo |
| EFM | El del Marco Equivalente (ya es la envolvente de sus patrones de carga) |

**Por qué envolvente.** Ambos métodos son válidos y dan repartos algo distintos entre negativo y positivo; tomar el mayor en cada sección cubre los dos. No es obligatorio: el Código acepta cualquiera de los dos por separado.

**Qué no entra.** El FEM de la hoja no participa en el diseño; solo verifica.

**Apoyos interiores.** El bastón se arma con el mayor momento por metro de los dos claros que llegan.

Se usa en: [[S07 Momentos de diseño y comparación]] · [[S08 Diseño por flexión]]
