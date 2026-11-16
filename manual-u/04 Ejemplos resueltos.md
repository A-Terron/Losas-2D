---
tags: [losas-2d-u, ejemplo]
---
# Ejemplos resueltos

Los casos se cargan desde el selector **Caso** de la barra superior. Usa estos números para comprobar tus cálculos a mano.

## HT1 · tablero T5 (interior, 6.70 × 5.36 m)

Losa de 15 cm sobre vigas de 35 × 60 cm, columnas de 50 × 50 cm y 5.50 m de alto, $f'_c$ = 4000 psi, Grado 60, sobrecarga muerta 50 kgf/m² y carga viva 250 kgf/m². Método: envolvente DDM–EFM.

| Paso | Resultado |
|---|---|
| Cargas | $w_D$ = 410 kgf/m², $w_u$ = 892 kgf/m² |
| Clasificación | Dos direcciones · tablero interior · vigas en los cuatro lados |
| $\alpha_f$ (inf., sup., izq., der.) | 7.11, 7.11, 6.57, 5.69 → $\alpha_{fm}$ = 6.62 |
| Espesor | $\beta$ = 6.35/5.01 = 1.267 → $h_{mín}$ = 14.73 cm ≤ 15 cm |
| DDM, dirección X, marco del eje 6 | $\ell_2$ = 5.36 m, $\ell_n$ = 6.20 m, $M_o$ = 22.97 tonf·m → 14.93 / 8.04 / 16.08 |
| EFM, mismo marco | $K_{sb}$ = 25 017, $K_{ec}$ = 14 062 tonf·m → 11.95 / 8.61 / 16.92 en las caras |
| Diseño (envolvente) | 14.93 / 8.61 / 16.92 tonf·m |
| Franja central X | $m_u$ = 1.427 / 0.610 / 1.260 tonf·m/m → #3 @ 20, @ 25 y @ 22.5 cm |
| Franja central Y | $m_u$ = 0.990 / 0.477 / 0.990 tonf·m/m → #3 @ 25 cm |
| Flexión | D/C máx. 0.94 |
| Cortante | X: $V_u$ = 2131 kgf/m, $\phi V_c$ = 4312 kgf/m → D/C 0.49 |
| Deflexión | $\Delta_L$ = 0.068 cm ≤ 1.86 cm · $\Delta_{post}$ = 0.353 cm ≤ 2.79 cm |
| Bastones X | Franja central: 1.45 m (eje F) y 1.80 m (eje I) desde la cara |

Los otros ocho tableros de la HT1 están en [[S14 Comparación con el modelo completo]].

## Ejemplos del selector

| Caso | Clasificación | Espesor | Armado | Verificaciones |
|---|---|---|---|---|
| Losa continua sobre vigas, 3.50 × 8.00 m | Una dirección ∥ X (relación 2.29) | 13 cm ≥ 12.5 cm | Principal #3 @ 30 cm, temperatura #3 @ 30 cm | Flexión 0.84 · cortante 0.34 |
| Losa sobre dos muros de mampostería, 3.50 m | Una dirección ∥ X (dos lados libres) | 18 cm ≥ 17.5 cm | Principal #4 @ 30 cm, temperatura #3 @ 20 cm | Flexión 0.59 · cortante 0.26 |
| Tablero aislado sobre cuatro vigas, 4 × 5 m | Dos direcciones · aislado · se diseña con EFM | 12 cm ≥ 11.02 cm | #3 @ 22.5 cm | Flexión 0.69 · cortante 0.40 |
| Placa plana, tablero interior 6 × 6 m | Dos direcciones · sin vigas | 20 cm ≥ 16.67 cm | #4 @ 17.5 a 35 cm | Flexión 0.98 · punzonamiento 0.81 |
| Placa plana, tablero de esquina 6 × 6 m | Dos direcciones · sin vigas · esquina | 20 cm ≥ 18.33 cm | #4 @ 15 a 35 cm | Flexión 0.99 · punzonamiento 0.92 |

![[U02-una-direccion-muros.png]]

![[U03-placa-plana-esquina.png]]
