---
tags: [losas-2d, ejemplo, ht1]
---
# Ejemplo HT1 · resultados

Todos los números que da la hoja con los datos de la HT1, reunidos para que puedas comprobar tus cálculos a mano. Unidades MKS (tonf, m, cm, kgf/cm²). Las cifras intermedias están redondeadas; la hoja trabaja con todos los decimales.

![[F01-planta-HT1.svg]]

## Datos de entrada

| Dato | Valor | Dato | Valor |
|---|---|---|---|
| $f'_c$ | 4000 psi (281 kgf/cm²) | Claros en X | 4.90 · 6.70 · 6.70 m |
| $f_y$ | 60 ksi (4218 kgf/cm²) | Claros en Y | 5.36 · 5.36 · 5.36 m |
| $E_s$ | 29 000 ksi | Losa $h$ | 15 cm |
| $\gamma_c$ | 2400 kgf/m³ | Recubrimiento | 2 cm |
| Sobrecarga muerta | 50 kgf/m² | Columnas | 50 × 50 cm, 5.50 m, empotradas |
| Carga viva | 250 kgf/m² | Vigas (todas) | 35 × 60 cm |
| Barras | #3 arriba y abajo | Capa exterior | Barras paralelas a Y |

## S01 · Materiales

| Resultado | Valor |
|---|---|
| $E_c$ | 253 456 kgf/cm² (3605 ksi) |
| $f_r$ | 33.35 kgf/cm² (474 psi) |
| $n$ | 8.04 |
| $\beta_1$ | 0.85 |
| $\varepsilon_{ty}$ | 0.00207 |

## S03 · Cargas

| Resultado | Valor |
|---|---|
| Peso propio | 360 kgf/m² |
| $w_D$ | 410 kgf/m² |
| $w_L$ | 250 kgf/m² |
| $1.4D$ | 574 kgf/m² |
| $1.2D + 1.6L$ | **892 kgf/m²** (gobierna) |
| $L/D$ | 0.61 → sin patrones de carga viva |

## S04 · Rigidez de vigas y espesor

| Viga | $b_f$ (cm) | $I_b$ (cm⁴) | $\ell_2$ (m) | $I_s$ (cm⁴) | $\alpha_f$ |
|---|---|---|---|---|---|
| ∥ X, ejes 5 y 8 (borde) | 80 | 901 254 | 2.93 | 82 406 | 10.94 |
| ∥ X, ejes 6 y 7 | 125 | 1 071 318 | 5.36 | 150 750 | 7.11 |
| ∥ Y, eje E (borde) | 80 | 901 254 | 2.70 | 75 937 | 11.87 |
| ∥ Y, eje F | 125 | 1 071 318 | 5.80 | 163 125 | 6.57 |
| ∥ Y, eje I | 125 | 1 071 318 | 6.70 | 188 437 | 5.69 |
| ∥ Y, eje K (borde) | 80 | 901 254 | 3.60 | 101 250 | 8.90 |

| Tablero | $\ell_{n,x}$ (m) | $\ell_{n,y}$ (m) | $\beta$ | $\alpha_{fm}$ | $h_{mín}$ (cm) |
|---|---|---|---|---|---|
| T1, T7 | 4.55 | 5.01 | 1.10 | 9.12 | 12.00 |
| T4 | 4.55 | 5.01 | 1.10 | 8.16 | 12.00 |
| T2, T8 | 6.35 | 5.01 | 1.27 | 7.57 | **14.73** |
| T3, T9 | 6.35 | 5.01 | 1.27 | 8.16 | 14.73 |
| T5 | 6.35 | 5.01 | 1.27 | 6.62 | 14.73 |
| T6 | 6.35 | 5.01 | 1.27 | 7.20 | 14.73 |

Todos con la expresión (d) de la Tabla 8.3.1.2 ($\alpha_{fm}$ > 2). Se usa $h$ = 15 cm.

## S05 · Diseño Directo, marco del eje 6 (dirección X)

$\ell_2$ = 5.36 m · $\alpha_f$ = 7.11 · caso «losa con vigas entre todos los apoyos».

| Claro | $\ell_n$ (m) | $M_o$ | $M^-_{izq}$ | $M^+$ | $M^-_{der}$ | % franja de columna |
|---|---|---|---|---|---|---|
| E–F | 4.40 | 11.57 | 1.85 | 6.60 | 14.93 | 78.5 / 72.2 / 72.2 |
| F–I | 6.20 | 22.97 | 14.93 | 8.04 | 16.08 | 81.0 / 81.0 / 81.0 |
| I–K | 6.20 | 22.97 | 16.08 | 13.09 | 3.68 | 81.0 / 81.0 / 85.3 |

Momentos en tonf·m. En los apoyos F e I ya se tomó el mayor de los dos claros (8.10.4.5). $\beta_t$ = 1.93 en los apoyos exteriores.

Reparto del claro F–I (tonf·m):

| Sección | Marco | Franja de columna | Viga (85 %) | Losa de franja de columna | Franja central |
|---|---|---|---|---|---|
| $M^-$ eje F | 14.93 | 12.10 | 10.28 | 1.81 | 2.84 |
| $M^+$ | 8.04 | 6.51 | 5.54 | 0.98 | 1.53 |
| $M^-$ eje I | 16.08 | 13.03 | 11.07 | 1.95 | 3.06 |

Franja de columna: 2.68 m (2.33 m de losa sin el alma). Media franja central: 1.34 m a cada lado.

## S06 · Marco Equivalente, marco del eje 6 (dirección X)

| Cantidad | Valor |
|---|---|
| $I_{sb}$ | 1 601 835 cm⁴ |
| $I_{sb}/(1-c_2/\ell_2)^2$ | 1 948 386 cm⁴ |
| Claro E–F: $k$, FT, $m$, $K_{sb}$ | 4.173 · 0.512 · 0.0846 · 34 579 tonf·m |
| Claros F–I e I–K: $k$, FT, $m$, $K_{sb}$ | 4.128 · 0.509 · 0.0843 · 25 017 tonf·m |
| $I_c$ | 520 833 cm⁴ |
| Zona rígida de la columna | 52.5 cm |
| $k_c$ y $K_c$ | 5.970 · 14 328 tonf·m |
| $C$ (interior / borde) | 622 356 / 582 362 cm⁴ |
| $K_t$ (ejes F, I / E, K) | 71 062 / 66 495 tonf·m |
| $I_{sb}/I_s$ | 10.63 |
| $K_{ta}$ (ejes F, I / E, K) | 755 085 / 706 562 tonf·m |
| $K_{ec}$ (ejes F, I / E, K) | 14 062 / 14 044 tonf·m |
| Cargas del marco | $w_{u,D}$ = 2.64 · $w_{u,L}$ = 2.14 tonf/m |

| Nudo | FD losa izq. | FD losa der. | FD columna |
|---|---|---|---|
| E | — | 0.711 | 0.289 |
| F | 0.469 | 0.340 | 0.191 |
| I | 0.390 | 0.390 | 0.219 |
| K | 0.640 | — | 0.360 |

| Claro | $M_{emp}$ | $M^-$ eje izq. | $M^-$ cara izq. | $M^+$ máx. | $M^-$ cara der. | $M^-$ eje der. |
|---|---|---|---|---|---|---|
| E–F | 9.72 | 2.52 | 0.37 | 6.34 | 11.41 | 14.82 |
| F–I | 18.10 | 15.60 | 11.95 | 8.61 | 16.92 | 20.98 |
| I–K | 18.10 | 22.19 | 17.77 | 12.82 | 3.62 | 6.90 |

Momentos en tonf·m. La distribución de momentos converge en 21 ciclos. Momento desequilibrado a columnas: 2.52 · 0.78 · 1.22 · 6.90 tonf·m.

## S07 · Comparación

![[F33-momentos-HT1-eje-6.svg]]

Marco del eje 6, dirección X (tonf·m):

| Claro | Sección | DDM | EFM | FEM | Diseño (envolvente) |
|---|---|---|---|---|---|
| E–F | $M^-$ E | 1.85 | 0.37 | 0.26 | 1.85 |
| E–F | $M^+$ | 6.60 | 6.34 | 6.63 | 6.60 |
| E–F | $M^-$ F | 14.93 | 11.41 | 12.57 | 14.93 |
| F–I | $M^-$ F | 14.93 | 11.95 | 13.16 | 14.93 |
| F–I | $M^+$ | 8.04 | 8.61 | 10.12 | 8.61 |
| F–I | $M^-$ I | 16.08 | 16.92 | 18.68 | 16.92 |
| I–K | $M^-$ I | 16.08 | 17.77 | 19.57 | 17.77 |
| I–K | $M^+$ | 13.09 | 12.82 | 14.26 | 13.09 |
| I–K | $M^-$ K | 3.68 | 3.62 | 3.76 | 3.68 |

Marco del eje F, dirección Y (tonf·m), $M_o$ = 15.27 en los tres claros:

| Claro | DDM (izq / + / der) | EFM | FEM |
|---|---|---|---|
| 5–6 | 2.44 / 8.71 / 10.69 | 1.42 / 9.39 / 11.12 | 1.33 / 10.38 / 12.09 |
| 6–7 | 10.69 / 5.35 / 10.69 | 10.50 / 4.78 / 10.50 | 11.46 / 5.70 / 11.46 |
| 7–8 | 10.69 / 8.71 / 2.44 | 11.12 / 9.39 / 1.42 | 12.09 / 10.38 / 1.33 |

## S08 · Flexión

$d$ = 12.52 cm (barras ∥ Y, capa exterior) y 11.57 cm (barras ∥ X). $A_{s,mín}$ = 2.70 cm²/m. $s_{máx}$ = 30 cm.

![[F32-armado-HT1-direccion-X.svg]]

Momentos por unidad de ancho (tonf·m/m) y armado, dirección X:

| Franja | Inferior E–F / F–I / I–K | Superior E / F / I / K | Armado |
|---|---|---|---|
| Central 5–6 y 7–8 | 0.66 / 0.63 / 0.97 | 0.17 / 1.49 / 1.32 / 0.26 | Inferior #3 @ 25 · superior @ 25 / **20** / **22.5** / 25 |
| Central 6–7 | 0.63 / 0.61 / 0.93 | 0.14 / 1.43 / 1.26 / 0.20 | Inferior #3 @ 25 · superior @ 25 / **20** / **22.5** / 25 |
| Columna, ejes 5 y 8 | 0.35 / 0.45 / 0.70 | 0.10 / 0.80 / 0.96 / 0.22 | #3 @ 25 |
| Columna, ejes 6 y 7 | 0.34 / 0.45 / 0.68 | 0.10 / 0.78 / 0.93 / 0.20 | #3 @ 25 |

Dirección Y:

| Franja | Inferior 5–6 / 6–7 / 7–8 | Superior 5 / 6 / 7 / 8 | Armado |
|---|---|---|---|
| Central E–F | 0.78 / 0.45 / 0.78 | 0.18 / 0.96 / 0.96 / 0.18 | #3 @ 25 |
| Central F–I | 0.84 / 0.48 / 0.84 | 0.14 / 0.99 / 0.99 / 0.14 | #3 @ 25 |
| Central I–K | 0.90 / 0.52 / 0.90 | 0.19 / 1.08 / 1.08 / 0.19 | #3 @ 25 |
| Columna (todos los ejes) | 0.43–0.47 / 0.26–0.27 / 0.43–0.47 | 0.12–0.15 / 0.55–0.57 / 0.55–0.57 / 0.12–0.15 | #3 @ 25 |

Sección desarrollada paso a paso (dirección X, franja central 6–7, apoyo I):

| Paso | Valor |
|---|---|
| $M_u$ de la franja y ancho | 3.376 tonf·m en 2.68 m |
| $m_u$ | 1.26 tonf·m/m |
| $R_n$ | 10.45 kgf/cm² |
| $\rho$ | 0.00253 |
| $A_{s,req}$ / $A_{s,mín}$ | 2.93 / 2.70 cm²/m |
| $s_{req}$ | 24.2 cm → **22.5 cm** |
| $A_{s,prov}$ | 3.15 cm²/m |
| $a$ / $c$ | 0.56 / 0.66 cm |
| $\varepsilon_t$ | 0.050 (≥ 0.00507) |
| $\phi m_n$ | 1.35 tonf·m/m · D/C = 0.93 |

## S09 · Cortante en una dirección

| Tablero | Dirección X: $V_u$ / $\phi V_c$ (tonf/m) | D/C | Dirección Y: $V_u$ / $\phi V_c$ | D/C |
|---|---|---|---|---|
| T1, T7 | 2.22 / 4.49 | 0.49 | 2.21 / 4.39 | 0.50 |
| T2, T8 | 2.13 / 4.49 | 0.48 | 2.44 / 4.39 | 0.56 |
| T3, T9 | **2.45 / 4.31** | **0.57** | 2.44 / 4.39 | 0.56 |
| T4 | 2.22 / 4.49 | 0.49 | 1.92 / 4.39 | 0.44 |
| T5 | 2.13 / 4.49 | 0.48 | 2.12 / 4.39 | 0.48 |
| T6 | 2.45 / 4.31 | 0.57 | 2.12 / 4.39 | 0.48 |

Caso que gobierna (T3, X): ancho tributario 2.505 m, $d$ = 11.57 cm, coeficiente 1.15, $\rho_w$ = 0.00273, $\lambda_s$ = 1.0, $V_c$ = 5.75 tonf/m.

## S10 · Deflexiones

Flecha relativa a las vigas, en mm. $\lambda_\Delta$ = 2, $\psi$ = 0.25.

| Tablero | Franja | $\Delta_{i,D}$ | $\Delta_{i,sost}$ | $\Delta_{i,D+L}$ | $\Delta_{i,L}$ | $\ell/360$ | $\Delta_{LP}$ | $\Delta_{post}$ | $\ell/240$ | $\Delta_{total}$ | FEM elástico D+L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T1, T7 | Y | 0.66 | 0.74 | 1.08 | 0.42 | 14.9 | 1.48 | 1.90 | 22.3 | 2.56 | 1.15 |
| T2, T8 | X | 1.37 | 1.55 | 2.11 | 0.74 | 18.6 | 3.09 | 3.83 | 27.9 | 5.20 | 1.73 |
| T3, T9 | X | 1.43 | 2.20 | 6.33 | 4.90 | 18.6 | 4.39 | 9.29 | 27.9 | 10.72 | 2.29 |
| T4 | Y | 0.58 | 0.66 | 0.88 | 0.29 | 14.9 | 1.31 | 1.60 | 22.3 | 2.19 | 0.77 |
| T5 | X | 1.26 | 1.43 | 1.93 | 0.68 | 18.6 | 2.85 | 3.53 | 27.9 | 4.78 | 1.60 |
| T6 | X | 1.32 | 2.67 | 10.38 | **9.05** | 18.6 | 5.33 | **14.39** | 27.9 | 15.71 | 2.26 |

Todos cumplen. T3, T6 y T9 son los que se agrietan con la carga viva completa; por eso su flecha crece mucho más que en el FEM elástico.

## S11 · Detallado

| Cantidad (#3) | Valor |
|---|---|
| $\ell_d$ | 36.1 cm |
| $\ell_{dh}$ | 15.2 cm (rige el mínimo de 6 in) |
| Tramo recto del gancho, $12d_b$ | 11.4 cm |
| Diámetro de doblez, $6d_b$ | 5.7 cm |
| Empalme clase B | 47 cm |

Bastones, dirección X (extensiones desde la cara del apoyo y largo total, en m):

| Apoyo | Franja central: extensión | Largo | Franja de columna: extensión | Largo |
|---|---|---|---|---|
| E (borde, gancho) | 1.00 | 1.45 | 1.35 | 1.80 |
| F | 1.40 hacia E · 1.45 hacia I | 3.35 | 1.90 · 1.90 | 4.30 |
| I | 1.80 hacia F · 1.70 hacia K | 4.00 | 1.90 · 1.90 | 4.30 |
| K (borde, gancho) | 1.40 | 1.85 | 1.90 | 2.35 |

Bastones, dirección Y:

| Apoyo | Franja central: extensión | Largo | Franja de columna: extensión | Largo |
|---|---|---|---|---|
| 5 y 8 (borde, gancho) | 1.10 | 1.55 | 1.50 | 1.95 |
| 6 y 7 | 1.25 hacia el borde · 1.40 hacia el centro | 3.15 | 1.50 · 1.50 | 3.50 |

Cama inferior: barras de 4.75 m (E–F), 6.55 m (F–I, I–K) y 5.20 m (dirección Y), con entrada de 15 cm en cada apoyo, o corridas con traslapes de 47 cm sobre las vigas.

Refuerzo de esquina: T1 y T7, #3 @ 25 en un cuadrado de 1.10 m; T3 y T9, #3 @ 25 en un cuadrado de 1.35 m; arriba y abajo, en las dos direcciones.

## S12 · Elementos finitos

24 × 24 elementos, 1875 grados de libertad, $D$ = 742.5 tonf·m. Momento positivo por unidad de ancho en las franjas centrales (tonf·m/m):

| Tablero | $m_x^+$ hoja | $m_x^+$ FEM | $m_y^+$ hoja | $m_y^+$ FEM |
|---|---|---|---|---|
| T1 | 0.66 | 0.54 | 0.78 | 0.53 |
| T2 | 0.63 | 0.61 | 0.84 | 0.76 |
| T3 | 0.97 | 0.69 | 0.90 | 0.79 |
| T4 | 0.63 | 0.50 | 0.45 | 0.44 |
| T5 | 0.61 | 0.55 | 0.48 | 0.61 |
| T6 | 0.93 | 0.65 | 0.52 | 0.66 |

T7, T8 y T9 repiten a T1, T2 y T3. La hoja queda por encima del FEM salvo en $m_y^+$ de T5 y T6 (fila central, dirección Y), donde el FEM da hasta 27 % más. En todos los casos la resistencia del acero mínimo (1.22 a 1.32 tonf·m/m) cubre el mayor valor.

## Validación del motor de cálculo

Ejemplo «Two-Way Concrete Floor Slab with Beams» de StructurePoint (ACI 318-14): claros de 17.5 ft, ancho de marco 22 ft, losa de 6 in, vigas 14 × 20 in, columnas 18 × 18 in. Se carga con el botón «Cargar ejemplo de validación» de la hoja.

| Cantidad | Publicado | Hoja |
|---|---|---|
| $K_{ec}$ exterior / $E_c$ | 763 a 764 | 763.5 |
| $K_{ec}$ interior / $E_c$ | 631 | 631.4 |
| Factores de distribución | 0.394 · 0.306 | 0.394 · 0.306 |
| Momento de empotramiento | 148.1 kip·ft | 148.1 |
| Momentos en ejes (carga total) | 93.1 · 167.7 · 153.6 kip·ft | 93.1 · 167.7 · 153.6 |
| Momentos en las caras | 60.2 · 128.4 · 117.6 kip·ft | 60.3 · 128.4 · 117.5 |
| Flecha del marco, carga muerta | 0.0063 in | 0.0063 |
| Flecha franja de columna / central | 0.009 / 0.021 in | 0.009 / 0.021 |

Volver a [[00 Inicio]].
