# Registro de cambios

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Cada versión tiene su etiqueta y su [release](https://github.com/A-Terron/Losas-2D/releases) con la hoja y el manual para descargar.

## [Sin publicar]

_Cambios que ya están en `main` pero aún no tienen versión._

## [v1.1] · 2026-11-16

Nueva hoja **Losas 2D U** (losa universal de un tablero) con su propio manual. La hoja y el manual de Losas 2D no cambian.

### Hoja de cálculo Losas 2D U
- Un tablero rectangular con el apoyo de cada borde (viga, muro de concreto, muro de mampostería, sin viga o borde libre), su continuidad y hasta dos tableros vecinos por lado.
- Detecta si la losa trabaja en una o en dos direcciones y, en dos direcciones, los mismos casos de Losas 2D: posición, sistema de piso, tabla de espesor y caso del claro extremo.
- Dos direcciones: Método de Diseño Directo, Marco Equivalente y envolvente, sobre el marco que forman el tablero y sus vecinos (extremo lejano empotrado según ACI 318-14 §8.11.2.5 cuando no se describe).
- Una dirección: ACI 318-19 Cap. 7 con los coeficientes de §6.5, acero de retracción y temperatura y control de agrietamiento.
- Punzonamiento en columnas sin viga (22.6), con transferencia de momento y el acero mínimo de 8.6.1.2.
- 14 secciones paso a paso, vistas de planta, momentos y sección con armado, unidades intercambiables.
- Los 9 tableros de la HT1 precargados y comparados con el modelo completo: momentos, acero, espesor y deflexiones coinciden en DDM, EFM y envolvente.

### Manual técnico Losas 2D U
- 6 notas generales, 14 notas de sección (S01–S14) con diagrama de flujo, 19 notas de concepto y 11 figuras.
- Los conceptos compartidos enlazan al manual de Losas 2D.

### Repositorio
- La hoja se publica en `/u/` y su manual en `/manual-u/`; el flujo de Pages construye los dos manuales.

## [v1.0] · 2026-11-13

Primera versión publicada.

### Hoja de cálculo
- 12 secciones: materiales, sistema y geometría, cargas, rigidez de vigas y espesor mínimo, DDM, EFM, momentos de diseño y comparación, flexión, cortante en una dirección, deflexiones, detallado y verificación FEM/ETABS.
- Losa apoyada en vigas (de borde e interiores) o sin vigas interiores.
- Unidades de datos y resultados intercambiables sin alterar el cálculo.
- Separación de barras en múltiplos de 2.5 cm.
- Datos de la HT1 (parqueo) y ejemplo de validación de StructurePoint.

### Manual técnico
- Notas S01–S12 (una por sección de la hoja), cada una con su diagrama de flujo.
- 58 notas de concepto, 33 figuras SVG, diagrama de flujo general, notación, verificación de fórmulas contra ACI 318-19 y 318-14, y resultados de la HT1.
- Versión web generada automáticamente desde la bóveda de Obsidian.

[Sin publicar]: https://github.com/A-Terron/Losas-2D/compare/v1.1...HEAD
[v1.1]: https://github.com/A-Terron/Losas-2D/releases/tag/v1.1
[v1.0]: https://github.com/A-Terron/Losas-2D/releases/tag/v1.0
