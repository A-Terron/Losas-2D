---
tags: [losas-2d, verificacion, trazabilidad]
---
# Verificación de fórmulas

Segunda revisión de la hoja: cada fórmula y cada regla se cotejó con el texto de **ACI 318-19** y, para el DDM y el EFM, con **ACI 318-14 §8.10 y §8.11**. La tabla indica el artículo, el resultado y la nota donde se explica.

> [!info] Cómo leer la columna «Resultado»
> **Conforme** = la hoja ya aplicaba el artículo tal cual. **Corregido** = la revisión encontró una diferencia y se cambió la hoja. **Criterio** = el Código no fija el procedimiento; la hoja usa un método reconocido y lo declara.

## Qué se corrigió en esta revisión

| # | Qué se encontró | Qué hace ahora la hoja | Artículo |
|---|---|---|---|
| 1 | Las separaciones se redondeaban a 1 cm | Múltiplos de **2.5 cm**, hacia abajo. Hay opción «al múltiplo más cercano», que marca en rojo cuando el acero colocado queda por debajo del requerido | 8.6.1.1 · 8.7.2.2 |
| 2 | El acero colocado menor que el requerido no invalidaba la sección | La verificación de flexión exige $A_{s,prov} \ge \max(A_{s,req}, A_{s,mín})$ | 8.6.1.1 |
| 3 | En marcos de borde, los porcentajes de franja de columna usaban el ancho del marco como $\ell_2$ | Usan el claro transversal completo del tablero (práctica usual; el Código no lo aclara) | 8.10.5 (318-14) |
| 4 | El tope de $0.175\,\ell_1$ para la sección crítica se aplicaba también al apoyo exterior | En el apoyo exterior la sección crítica es la cara del apoyo, sin tope | 8.11.6.1 · 8.11.6.2 (318-14) |
| 5 | El caso «losa con vigas entre todos los apoyos» se elegía con solo tener viga en el eje del marco | Se exige además viga transversal en todos los apoyos del marco | Tabla 8.10.4.2 (318-14) |
| 6 | La Tabla 8.3.1.2 se aplicaba a tableros con vigas solo en algunos lados | Solo si el tablero tiene vigas en sus **cuatro** lados; si no, Tabla 8.3.1.1 | 8.3.1.1 · 8.3.1.2 |
| 7 | No se revisaba el recubrimiento mínimo | Se compara con la Tabla 20.5.1.3.1 según la exposición | 20.5.1.3.1 |
| 8 | $\ell_d$ suponía siempre el caso favorable y $\psi_r$ = 1.0 | $\ell_d$ usa la fila «otros casos» si no se cumple separación libre ≥ $2d_b$ y recubrimiento ≥ $d_b$; $\psi_r$ = 1.6 si los ganchos están a menos de $6d_b$ | Tabla 25.4.2.3 · Tabla 25.4.3.2 |
| 9 | En losas sin vigas faltaba el mínimo de $5d$ | La extensión del bastón en franja de columna no baja de $5d$ | Fig. 8.7.4.1.3 |
| 10 | El refuerzo de esquina usaba solo el momento de la franja central | Usa el mayor $M_u^+$ por unidad de ancho de todo el tablero | 8.7.3.1 |
| 11 | La fracción de $\ell_n$ del bastón usaba el claro de cada lado | En apoyos con claros desiguales usa el mayor | 8.7.4.1.3(b) |
| 12 | La flecha se comparaba solo como absoluta en el centro | Por defecto, relativa a las vigas de apoyo (criterio de clase); la absoluta queda como opción | Tabla 24.2.2 |

> [!warning] Sobre «#3 @ 27.5 cm»
> Con losa de 15 cm el acero mínimo es $0.0018 \times 100 \times 15$ = 2.70 cm²/m. Una barra #3 (0.71 cm²) a 27.5 cm da 2.58 cm²/m, **menos que el mínimo**; a 25 cm da 2.84 cm²/m y cumple. La separación exacta es 26.3 cm, y en múltiplos de 2.5 cm el valor que cumple es **25 cm**. Por eso la hoja redondea hacia abajo. Ver [[Separación de barras]].

## Trazabilidad por sección

### S01 · Materiales

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| $E_c = 57\,000\sqrt{f'_c}$ (o $33\,w_c^{1.5}\sqrt{f'_c}$) | 19.2.2.1 | Conforme | [[Módulo de elasticidad Ec]] |
| $f_r = 7.5\,\lambda\sqrt{f'_c}$ | 19.2.3.1 | Conforme | [[Módulo de ruptura fr]] |
| $E_s$ = 29 000 ksi | 20.2.2.2 | Conforme | [[Relación modular n]] |
| $\beta_1$ = 0.85 hasta 4000 psi, baja 0.05 por cada 1000 psi, mínimo 0.65 | Tabla 22.2.2.4.3 | Conforme | [[Factor beta1]] |
| $\varepsilon_{ty} = f_y/E_s$ | 21.2.2.1 | Conforme | [[Sección controlada por tensión]] |

### S02 a S04 · Geometría, cargas y espesor

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| Claros de 3 a 8 m y relación ≤ 2 | Proyecto §3 | Conforme | [[S02 Sistema estructural y geometría]] |
| $U = 1.4D$ y $U = 1.2D + 1.6L$ | 5.3.1 | Conforme | [[Combinaciones de carga y wu]] |
| Patrones con ¾ de $L$ mayorada solo si $L > 0.75D$ | 6.4.3.2 · 6.4.3.3 | Conforme | [[Patrones de carga viva]] |
| Vuelo de la viga: mín($h_b - h$, $4h$) | 8.4.1.8 | Conforme | [[Sección efectiva de viga]] |
| $\alpha_f = E_{cb}I_b/(E_{cs}I_s)$ | 8.10.2.7 (318-14) | Conforme | [[Rigidez relativa alfa f]] |
| $h_{mín}$ sin vigas interiores: $\ell_n/30$, $/33$, $/36$ según el caso; ≥ 5 in | Tabla 8.3.1.1 | Conforme | [[Espesor mínimo de losa]] |
| $h_{mín}$ con vigas: expresiones (b) y (d); ≥ 5 in y ≥ 3.5 in | Tabla 8.3.1.2 | Corregido (#6) | [[Espesor mínimo de losa]] |
| +10 % en tableros de borde sin viga de $\alpha_f$ ≥ 0.80 | 8.3.1.2.1 | Conforme | [[Espesor mínimo de losa]] |
| $h < h_{mín}$ solo si las deflexiones calculadas cumplen | 8.3.2 | Conforme | [[S10 Deflexiones]] |

### S05 · Método de Diseño Directo (ACI 318-14 §8.10)

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| El DDM se permite para cargas de gravedad | 6.2.4.1 (318-19) | Conforme | [[Limitaciones del DDM]] |
| Siete limitaciones de aplicación | 8.10.2.1 a 8.10.2.7 | Conforme | [[Limitaciones del DDM]] |
| $M_o = q_u\,\ell_2\,\ell_n^2/8$, con $\ell_n \ge 0.65\,\ell_1$ | 8.10.3.2 | Conforme | [[Momento estático Mo]] |
| $\ell_2$ del marco de borde: del borde a la línea media del tablero | 8.10.3.2.3 | Conforme | [[Marco de diseño y ancho l2]] |
| Claro interior: 0.65 y 0.35 | 8.10.4.1 | Conforme | [[Coeficientes longitudinales del DDM]] |
| Claro extremo: cinco casos | Tabla 8.10.4.2 | Corregido (#5) | [[Coeficientes longitudinales del DDM]] |
| En apoyo interior, el mayor de los dos negativos | 8.10.4.5 | Conforme | [[Coeficientes longitudinales del DDM]] |
| Franja de columna: 0.25 del menor de $\ell_1$ y $\ell_2$ a cada lado | 8.4.1.5 (318-19) | Conforme | [[Franja de columna y franja central]] |
| Porcentajes de franja de columna (interpolación lineal) | Tablas 8.10.5.1, 8.10.5.2 y 8.10.5.5 | Corregido (#3) | [[Porcentajes de la franja de columna]] |
| $\beta_t = E_{cb}C/(2E_{cs}I_s)$; $C = \sum(1-0.63x/y)x^3y/3$ | 8.10.5.2 | Conforme | [[Rigidez torsional beta t]] · [[Constante torsional C]] |
| Viga: 85 % de la franja de columna si $\alpha_{f1}\ell_2/\ell_1 \ge 1$; lineal hasta 0 | 8.10.5.7.1 | Conforme | [[Reparto entre viga y losa]] |
| Peso del alma directo a la viga | 8.10.5.7.2 | Conforme | [[Peso del alma de las vigas]] |
| Franja central: suma de sus dos medias franjas | 8.10.6.2 | Conforme | [[Franja de columna y franja central]] |

### S06 · Método del Marco Equivalente (ACI 318-14 §8.11)

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| El EFM se permite para cargas de gravedad | 6.2.4.1 (318-19) | Conforme | [[Marco equivalente]] |
| Inercia de la losa-viga entre eje y cara: $I_{sb}/(1-c_2/\ell_2)^2$ | 8.11.3.3 | Conforme | [[Miembro no prismático]] |
| Columna infinitamente rígida dentro del nudo | 8.11.4 | Conforme | [[Rigidez de la columna Kc]] |
| Sección del miembro a torsión: la mayor de tres | 8.11.5.1 | Conforme | [[Constante torsional C]] |
| $K_t = \sum 9E_{cs}C/[\ell_2(1-c_2/\ell_2)^3]$ | R8.11.5 | Conforme | [[Miembro a torsión Kt]] |
| Con viga en el marco: $K_t$ por $I_{sb}/I_s$ | 8.11.5.2 | Conforme | [[Miembro a torsión Kt]] |
| $1/K_{ec} = 1/\sum K_c + 1/K_t$ | R8.11.4 | Conforme | [[Columna equivalente Kec]] |
| Sección crítica: cara del apoyo, máximo $0.175\,\ell_1$ en apoyos interiores | 8.11.6.1 · 8.11.6.2 | Corregido (#4) | [[Momento en la cara del apoyo]] |
| Reducción cuando la suma supera $M_o$ (opcional) | 8.11.6.5 | Conforme | [[Momentos de diseño y envolvente]] |
| Reparto transversal con las tablas del DDM | 8.11.6.6 | Conforme | [[Porcentajes de la franja de columna]] |
| Resultados frente al ejemplo de StructurePoint | — | Validado | [[04 Ejemplo HT1 - resultados#Validación del motor de cálculo]] |

### S08 · Flexión

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| Momento en la cara del apoyo | 8.4.2.1 | Conforme | [[Momento en la cara del apoyo]] |
| $\phi$ = 0.90 en secciones controladas por tensión | Tabla 21.2.2 | Conforme | [[Resistencia de diseño a flexión]] |
| Bloque rectangular: $a = A_sf_y/(0.85f'_cb)$ | 22.2.2.4.1 | Conforme | [[Coeficiente Rn y cuantía]] |
| Losa controlada por tensión: $\varepsilon_t \ge \varepsilon_{ty} + 0.003$ | 8.3.3.1 | Conforme | [[Sección controlada por tensión]] |
| $A_{s,mín} = 0.0018A_g$ | 8.6.1.1 | Corregido (#2) | [[Acero mínimo]] |
| $s_{máx}$ = mín($2h$, 18 in) en secciones críticas | 8.7.2.2 | Corregido (#1) | [[Separación de barras]] |
| Separación libre mínima: 1 in y $d_b$ | 25.2.1 | Conforme | [[Separación de barras]] |
| Recubrimiento mínimo | Tabla 20.5.1.3.1 | Corregido (#7) | [[Recubrimiento]] |

### S09 · Cortante en una dirección

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| Cortante en una dirección según 22.5 | 8.5.3.1.1 | Conforme | [[Resistencia a cortante Vc]] |
| Sección crítica a $d$ de la cara del apoyo | 8.4.3.2 | Conforme | [[Cortante último Vu]] |
| $V_c = 8\lambda_s\lambda\rho_w^{1/3}\sqrt{f'_c}\,b_wd$ | Tabla 22.5.5.1 (c) | Conforme | [[Resistencia a cortante Vc]] |
| $V_c \le 5\lambda\sqrt{f'_c}\,b_wd$ | 22.5.5.1.1 | Conforme | [[Resistencia a cortante Vc]] |
| $\lambda_s = \sqrt{2/(1+d/10)} \le 1$ | 22.5.5.1.3 | Conforme | [[Efecto de tamaño lambda s]] |
| $\phi$ = 0.75 | Tabla 21.2.1 | Conforme | [[Resistencia a cortante Vc]] |
| Áreas tributarias a 45° con vigas de $\alpha_{f1}\ell_2/\ell_1 \ge 1$ | 8.10.8.1 (318-14) | Criterio | [[Cortante último Vu]] |
| Coeficiente 1.15 en el primer apoyo interior | 6.5.4 (analogía) | Criterio | [[Cortante último Vu]] |

### S10 · Deflexiones

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| Las flechas deben considerar forma del tablero y apoyos | 24.2.3.3 | Conforme | [[Método de las franjas cruzadas]] |
| $M_{cr} = f_rI_g/y_t$ | 24.2.3.5 | Conforme | [[Momento de agrietamiento Mcr]] |
| $I_e$ con umbral $\tfrac23 M_{cr}$ | Tabla 24.2.3.5 | Conforme | [[Inercia efectiva Ie]] |
| Promedio de $I_e$ en miembros continuos | 24.2.3.6 | Conforme (pesos de ACI 435R) | [[Inercia efectiva Ie]] |
| $\lambda_\Delta = \xi/(1+50\rho')$ | 24.2.4.1.1 | Conforme | [[Deflexión a largo plazo]] |
| $\xi$ = 2.0 a 5 años o más | Tabla 24.2.4.1.3 | Conforme | [[Deflexión a largo plazo]] |
| Límites $\ell/360$, $\ell/240$, $\ell/480$ | Tabla 24.2.2 | Conforme | [[Límites de deflexión]] |
| Franjas cruzadas con el marco equivalente | ACI 435R | Criterio (validado) | [[Método de las franjas cruzadas]] |
| Flecha relativa a las vigas | Criterio de clase | Corregido (#12) | [[Flecha relativa a las vigas]] |

### S11 · Detallado

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| $\ell_d$ y sus factores | Tabla 25.4.2.3 · Tabla 25.4.2.5 | Corregido (#8) | [[Longitud de desarrollo ld]] |
| $\ell_{dh}$ ≥ $8d_b$ y 6 in; factores $\psi_r$, $\psi_o$, $\psi_c$ | 25.4.3.1 · Tabla 25.4.3.2 | Corregido (#8) | [[Gancho estándar ldh]] |
| Gancho a 90°: doblez $6d_b$, tramo recto $12d_b$ | Tabla 25.3.1 | Conforme | [[Gancho estándar ldh]] |
| Empalme clase B: $1.3\,\ell_d$ ≥ 12 in | Tabla 25.5.2.1 | Conforme | [[Empalme por traslape]] |
| Acero positivo: 6 in dentro del apoyo de borde | 8.7.4.1.1(a) | Conforme | [[Anclaje del refuerzo inferior]] |
| Acero negativo anclado en el apoyo de borde | 8.7.4.1.1(b) · 8.7.4.1.2 | Conforme | [[Gancho estándar ldh]] |
| Extensiones mínimas (0.30, 0.20, 0.22 $\ell_n$; 5$d$) | Fig. 8.7.4.1.3 | Corregido (#9, #11) | [[Extensión de bastones]] |
| Prolongación más allá de donde ya no se requiere: $d$ o $12d_b$; $\ell_n/16$ tras el punto de inflexión | 7.7.3.3 · 7.7.3.8.4 | Conforme | [[Extensión de bastones]] |
| Refuerzo de esquina: $\alpha_f$ > 1.0, $M_u^+$ máximo, un quinto del claro mayor | 8.7.3.1 | Corregido (#10) | [[Refuerzo de esquina]] |
| Integridad en losas sin vigas | 8.7.4.2 | Conforme (aviso) | [[Anclaje del refuerzo inferior]] |

### S12 · Elementos finitos

| Fórmula o regla | Artículo | Resultado | Nota |
|---|---|---|---|
| El FEM es un método de análisis aceptado | 6.9 · 8.2.1 | Conforme | [[Elemento finito de placa]] |
| Rigideces reducidas 0.25 / 0.35 / 0.70 | Tabla 6.6.3.1.1(a) | Conforme (opción) | [[Modificadores de rigidez]] |
| Solo verificación, no método principal | Proyecto §5 | Conforme | [[S12 Verificación FEM y ETABS]] |

## Lo que el Código no fija y la hoja decide

Estos puntos no son «fórmulas del ACI»: son criterios de ingeniería que conviene declarar en la memoria.

- **Peso del alma de las vigas.** Va directo a la viga (318-14 §8.10.5.7.2). El ejemplo de StructurePoint lo reparte en el ancho del marco; la hoja ofrece ambas opciones.
- **Cortante último de la losa.** El Código da la resistencia, no cómo obtener $V_u$ en una losa sobre vigas. Se usa el ancho tributario de medio claro libre corto, a $d$ de la cara.
- **Secciones para las deflexiones.** En los apoyos se toma el alma rectangular de la viga como sección bruta, igual que el ejemplo de StructurePoint.
- **Acero de las vigas.** No se diseñan; para la inercia agrietada se estima su acero.
- **$\psi_o$ = 1.25 en los ganchos.** Valor del lado seguro.
- **Punzonamiento.** Fuera del alcance del proyecto. En una losa sin vigas es obligatorio en un diseño real (22.6).

Volver a [[00 Inicio]].
