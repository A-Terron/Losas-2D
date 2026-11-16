---
tags: [losas-2d-u, concepto, clasificacion]
---
# Posición del tablero

**Qué es.** Dónde está el tablero dentro del piso, deducido de cuántos bordes son discontinuos.

| Bordes discontinuos | Posición |
|---|---|
| Ninguno | Interior |
| Uno | De borde |
| Dos adyacentes | De esquina |
| Dos opuestos | Con dos bordes opuestos discontinuos |
| Tres | Extremo de una fila |
| Cuatro | Aislado |

**Qué decide.**

- **Espesor mínimo:** un tablero exterior sin viga de borde rígida ($\alpha_f<0.8$) necesita más espesor.
- **DDM:** en la dirección perpendicular a un borde discontinuo el claro es extremo y usa la Tabla 8.10.4.2.
- **Refuerzo de esquina:** solo donde se cruzan dos bordes discontinuos.
- **Punzonamiento:** tipo de columna (interior, de borde o de esquina).

**En la hoja.** Sección 4. En Losas 2D la posición sale del índice del tablero en la retícula (T5 es el interior).
