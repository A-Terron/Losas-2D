---
tags: [losas-2d, referencia]
---
# Notación y unidades

## Convenciones

- **Dirección de análisis.** «Dirección X» significa franjas y barras **paralelas a X**: los claros son $L_{x}$ y el ancho transversal se mide en Y. Igual para Y.
- **$\ell_1$ y $\ell_2$.** $\ell_1$ es el claro en la dirección que se analiza (entre ejes); $\ell_2$ es el claro transversal. Cambian de papel al cambiar de dirección.
- **Signos.** $M^-$ tensiona la cara **superior** (apoyos) y se arma con bastones; $M^+$ tensiona la cara **inferior** (centro del claro) y se arma con la cama inferior.
- **Tableros.** T1 a T9, numerados de izquierda a derecha y de abajo hacia arriba. **Ejes:** E, F, I, K en X; 5, 6, 7, 8 en Y (como en la HT1).

## Símbolos

| Símbolo | Significado | Nota |
|---|---|---|
| $f'_c$, $f_y$ | Resistencia del concreto y fluencia del acero | [[S01 Materiales]] |
| $E_c$, $E_s$, $n$ | Módulos de elasticidad y relación modular | [[Módulo de elasticidad Ec]] |
| $f_r$ | Módulo de ruptura | [[Módulo de ruptura fr]] |
| $h$ | Espesor de la losa | [[Espesor mínimo de losa]] |
| $b_w$, $h_b$, $b_f$ | Alma, peralte total y patín efectivo de la viga | [[Sección efectiva de viga]] |
| $I_b$, $I_s$, $\alpha_f$ | Inercia de viga, de franja de losa y su relación | [[Rigidez relativa alfa f]] |
| $\alpha_{fm}$, $\beta$ | Promedio de $\alpha_f$ del tablero; relación de claros libres | [[Relación de claros beta]] |
| $\ell_1$, $\ell_2$, $\ell_n$ | Claro, ancho del marco, claro libre | [[Marco de diseño y ancho l2]] · [[Claro libre ln]] |
| $c_1$, $c_2$ | Lado de la columna paralelo a $\ell_1$ y a $\ell_2$ | — |
| $w_D$, $w_L$, $w_u$ | Carga muerta, viva y última por área | [[Combinaciones de carga y wu]] |
| $M_o$ | Momento estático total | [[Momento estático Mo]] |
| $C$, $\beta_t$ | Constante torsional y rigidez torsional relativa | [[Constante torsional C]] · [[Rigidez torsional beta t]] |
| $K_{sb}$, $K_c$, $K_t$, $K_{ec}$ | Rigideces del marco equivalente | [[Marco equivalente]] |
| FD, FT | Factor de distribución y factor de transporte | [[Factores de distribución]] |
| $m_u$ | Momento último por unidad de ancho | [[S08 Diseño por flexión]] |
| $d$, $R_n$, $\rho$, $A_s$, $s$ | Peralte efectivo, coeficiente de resistencia, cuantía, acero, separación | [[Coeficiente Rn y cuantía]] |
| $\phi$ | Factor de reducción: 0.90 flexión, 0.75 cortante | ACI 21.2.1 |
| $V_u$, $V_c$, $\lambda_s$, $\rho_w$ | Cortante último, resistencia del concreto, efecto de tamaño, cuantía | [[Resistencia a cortante Vc]] |
| $M_a$, $M_{cr}$, $I_g$, $I_{cr}$, $I_e$ | Momento de servicio, de agrietamiento e inercias | [[Inercia efectiva Ie]] |
| $\Delta$, $\lambda_\Delta$, $\xi$, $\psi$ | Flecha, multiplicador de largo plazo, factor de tiempo, fracción sostenida de $L$ | [[Deflexión a largo plazo]] |
| $\ell_d$, $\ell_{dh}$, $\ell_{st}$, $d_b$ | Desarrollo, gancho, empalme, diámetro de barra | [[Longitud de desarrollo ld]] |

## Unidades

La hoja calcula **internamente en pulgadas, kip y ksi**, porque así están escritas las ecuaciones de la edición en libras-pulgadas del ACI ($57\,000\sqrt{f'_c}$, $7.5\lambda\sqrt{f'_c}$, $\lambda_s$ con $d$ en pulgadas, etc.). Lo que ves en pantalla se convierte a la unidad que elijas; **cambiar unidades no altera el cálculo**.

> [!tip] Si calculas a mano
> Trabaja en un solo sistema. Con las ecuaciones tal como aparecen en este manual usa **psi, lb e in**; al final convierte: 1 in = 2.54 cm, 1 kip = 0.4536 tonf, 1 kip·ft = 0.1383 tonf·m, 1 psi = 0.0703 kgf/cm², 1 psf = 4.882 kgf/m².

| Magnitud | MKS (por defecto) | SI | Inglés |
|---|---|---|---|
| Dimensiones de sección | cm | mm | in |
| Claros y longitudes | m | m | ft |
| Carga por área | kgf/m² | kPa | psf |
| Momento | tonf·m | kN·m | kip·ft |
| Momento por ancho | tonf·m/m | kN·m/m | kip·ft/ft |
| Fuerza por longitud | tonf/m | kN/m | kip/ft |
| Acero por ancho | cm²/m | mm²/m | in²/ft |
| Esfuerzo | kgf/cm² | MPa | psi |
| Inercia | cm⁴ | cm⁴ | in⁴ |

## Barras de refuerzo

| Barra | $d_b$ (in) | $d_b$ (cm) | $A_b$ (in²) | $A_b$ (cm²) |
|---|---|---|---|---|
| #3 | 0.375 | 0.95 | 0.11 | 0.71 |
| #4 | 0.500 | 1.27 | 0.20 | 1.29 |
| #5 | 0.625 | 1.59 | 0.31 | 2.00 |
| #6 | 0.750 | 1.91 | 0.44 | 2.84 |

Volver a [[00 Inicio]].
