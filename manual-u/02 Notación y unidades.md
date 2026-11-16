---
tags: [losas-2d-u, notacion]
---
# Notación y unidades

## Bordes y direcciones

![[U10-bordes-y-vecinos.svg]]

| Símbolo | Significado |
|---|---|
| $\ell_x$, $\ell_y$ | Claros del tablero entre ejes de apoyo |
| Izquierdo / derecho | Bordes en $x=0$ y $x=\ell_x$; son los **apoyos A y B** de la dirección X |
| Inferior / superior | Bordes en $y=0$ y $y=\ell_y$; apoyos A y B de la dirección Y |
| Dirección X | Franjas y barras paralelas a X; sus marcos corren sobre los bordes inferior y superior |
| $\ell_1$ | Claro en la dirección que se analiza |
| $\ell_2$ | Ancho del marco, perpendicular a $\ell_1$ |
| $\ell_n$ | Claro libre entre caras de apoyo |
| $h$, $d$ | Espesor de la losa y peralte efectivo |
| $c_x$, $c_y$ | Lados de la columna |
| $b_w$, $h_b$ | Ancho del alma y peralte total de una viga (incluye la losa) |

## Momentos y franjas

| Símbolo | Significado |
|---|---|
| $M_o$ | Momento estático total del marco |
| $M^-_A$, $M^+$, $M^-_B$ | Momento negativo en el apoyo A, positivo en el centro y negativo en el apoyo B |
| $m_u$ | Momento último **por unidad de ancho** de losa |
| Franja de columna | Banda de un cuarto del claro menor a cada lado del eje del marco |
| Franja central | Lo que queda entre las dos franjas de columna del tablero |
| $\alpha_f$, $\beta_t$ | Rigidez relativa viga–losa a flexión y a torsión |
| $K_{sb}$, $K_c$, $K_t$, $K_{ec}$ | Rigideces de la losa-viga, la columna, el miembro a torsión y la columna equivalente |

## Unidades

La hoja calcula todo internamente en pulgadas, kip y ksi, que son las unidades de las ecuaciones de ACI 318. Lo que se muestra se convierte al sistema que elijas (MKS, SI o inglés), y cada resultado puede cambiar su unidad por separado tocándola. **Cambiar unidades nunca cambia el cálculo.**

Los artículos 8.10 y 8.11 que aparecen en la hoja son de **ACI 318-14**: allí están las reglas del DDM y el EFM que ACI 318-19 §6.2.4.1 sigue permitiendo.
