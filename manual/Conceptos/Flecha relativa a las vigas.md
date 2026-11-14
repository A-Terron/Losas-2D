---
tags: [losas-2d, concepto, deflexiones]
---
# Flecha relativa a las vigas

**Qué es.** Lo que baja el centro de la losa respecto a las vigas en que se apoya. Es la deformación propia de la losa, sin contar lo que bajan sus apoyos.

![[F25-flecha-relativa.svg]]

**Fórmula.**

$$\Delta_{rel}=\Delta_{centro}-\frac{\Delta_{viga,1}+\Delta_{viga,2}}{2}$$

En el método de las franjas cruzadas esto es directamente la flecha de la franja central, $\Delta_{mx}$ o $\Delta_{my}$: la franja central en X se apoya en las vigas paralelas a Y, y viceversa. La hoja evalúa las dos direcciones y se queda con la más desfavorable, comparándola con el límite calculado con el claro de esa franja.

**Por qué.** Es el criterio de clase para leer ETABS: la flecha que da el programa en el centro del tablero es absoluta e incluye el descenso de las vigas. Se toman tres puntos (las dos vigas y el centro) y se resta el promedio de los apoyos.

**Cuándo se usa.** Solo si el tablero tiene vigas en sus cuatro lados. En una losa sin vigas no hay «apoyos» de la franja y se usa la flecha del centro del tablero respecto a las columnas.

**En la HT1 (tablero T6, franja X).** Hoja: 1.04 cm para D + L. FEM elástico con secciones brutas: 0.23 cm. La diferencia es el agrietamiento, que el FEM elástico no considera.

**Referencia.** Criterio de clase; ACI 318-19 Tabla 24.2.2 (el límite se aplica al miembro que se deforma).

Se usa en: [[S10 Deflexiones]] · [[Comparación con ETABS]]
