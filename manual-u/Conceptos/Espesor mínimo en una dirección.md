---
tags: [losas-2d-u, concepto, espesor, una-direccion]
---
# Espesor mínimo en una dirección

**Qué es.** El espesor con el que una losa maciza en una dirección no necesita cálculo de deflexiones.

**Tabla 7.3.1.1.**

| Condición de apoyo | $h_{mín}$ |
|---|---|
| Simplemente apoyada | $\ell/20$ |
| Un extremo continuo | $\ell/24$ |
| Ambos extremos continuos | $\ell/28$ |

$\ell$ es el claro entre ejes de apoyo.

**Correcciones.**

- Acero distinto de Grado 60: multiplicar por $0.4+f_y/100\,000$ (7.3.1.1.1).
- Concreto liviano de 90 a 115 lb/ft³: multiplicar por el mayor de $1.65-0.005w_c$ y 1.09 (7.3.1.1.2).

**Por qué solo depende del claro.** En una dirección la losa se comporta como una viga ancha: la flecha depende de $\ell^4/h^3$, así que limitar $\ell/h$ limita la flecha relativa.

**Diferencia con dos direcciones.** Allí cuenta también la rigidez de las vigas ($\alpha_{fm}$) y la relación de claros; ver [Espesor mínimo de losa](https://a-terron.github.io/Losas-2D/manual/Conceptos/Espesor%20m%C3%ADnimo%20de%20losa/).

**En la hoja.** Sección 5. Si $h<h_{mín}$ se debe cumplir la sección de deflexiones (7.3.2).
