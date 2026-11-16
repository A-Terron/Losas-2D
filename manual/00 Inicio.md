---
tags: [losas-2d, indice]
aliases: [Manual Losas 2D, Inicio]
---
# Manual técnico · Losas en dos direcciones (ACI 318-19)

Este manual explica, paso a paso, todo lo que calcula la hoja **`Losas 2D - ACI 318-19.html`**: qué fórmula se usa, **por qué** se usa, **cómo** se aplica, **cuándo** corresponde y **qué cambia** según el caso. Está escrito para que puedas repetir cada cálculo a mano.

> [!info] Cómo está organizado
> - **Notas de sección (S01 a S12).** Una por cada sección de la hoja, en el mismo orden. Cada una trae su diagrama de flujo, el procedimiento completo, las figuras y el ejemplo de la HT1.
> - **Notas de concepto.** Notas cortas, una por idea o fórmula (por ejemplo [[Rigidez relativa alfa f]] o [[Inercia efectiva Ie]]). Las secciones enlazan a ellas; sirven para repasar una sola cosa.
> - **Figuras.** Los esquemas están en la carpeta `Figuras` y aparecen incrustados en las notas.

> [!tip] ¿Un solo tablero?
> La hoja **Losas 2D U** resuelve una losa aislada, en una o en dos direcciones, con los mismos métodos. Tiene su propio manual: [Manual de Losas 2D U](https://a-terron.github.io/Losas-2D/manual-u/).

## Empieza aquí

1. [[01 Diagrama de flujo general]] — el recorrido completo del diseño en una sola vista.
2. [[02 Notación y unidades]] — símbolos, subíndices y sistema de unidades.
3. Las secciones, en orden:

| Hoja | Nota | Qué resuelve |
|---|---|---|
| 1 | [[S01 Materiales]] | $E_c$, $f_r$, $n$, $\beta_1$, $\varepsilon_{ty}$ |
| 2 | [[S02 Sistema estructural y geometría]] | Tipo de sistema, vigas, claros, columnas |
| 3 | [[S03 Cargas]] | $w_D$, $w_L$, $w_u$ y relación $L/D$ |
| 4 | [[S04 Rigidez de vigas y espesor mínimo]] | $\alpha_f$, $\alpha_{fm}$, $\beta$, $h_{mín}$ |
| 5 | [[S05 Método de Diseño Directo]] | $M_o$ y su reparto con coeficientes |
| 6 | [[S06 Método del Marco Equivalente]] | Rigideces, distribución de momentos, envolvente |
| 7 | [[S07 Momentos de diseño y comparación]] | DDM frente a EFM frente a FEM |
| 8 | [[S08 Diseño por flexión]] | $A_s$, barra y separación por franja |
| 9 | [[S09 Cortante en una dirección]] | $V_u$ frente a $\phi V_c$ |
| 10 | [[S10 Deflexiones]] | Inmediata, de largo plazo y límites |
| 11 | [[S11 Detallado del refuerzo]] | $\ell_d$, ganchos, empalmes, bastones, esquinas |
| 12 | [[S12 Verificación FEM y ETABS]] | Modelo de placa y comparación con ETABS |

4. [[03 Verificación de fórmulas]] — cada fórmula con su artículo del Código y el resultado de la revisión.
5. [[04 Ejemplo HT1 - resultados]] — los números del parqueo de la HT1, para comprobar tus cálculos a mano.

## El proyecto en pocas líneas

![[F01-planta-HT1.svg]]

- **Estructura.** Parqueo de un nivel (HT1), retícula de 3 × 3 tableros: claros de 4.90, 6.70 y 6.70 m en X y tres de 5.36 m en Y.
- **Sistema.** Losa maciza apoyada en vigas de 35 × 60 cm sobre columnas de 50 × 50 cm; la hoja también resuelve la losa sin vigas interiores.
- **Materiales.** Concreto $f'_c$ = 4000 psi, acero Grado 60.
- **Cargas.** Sobrecarga muerta 50 kgf/m², carga viva 250 kgf/m².
- **Métodos.** Diseño Directo (DDM) y Marco Equivalente (EFM) para diseñar; elementos finitos (FEM) solo para verificar.

> [!warning] Dos ediciones del Código
> ACI 318-19 §6.2.4.1 **permite** el DDM y el EFM, pero ya no trae sus reglas. El comentario R6.2.4.1 remite a la edición 2014. Por eso en este manual los artículos **8.10** (DDM) y **8.11** (EFM) son de **ACI 318-14**; todo lo demás es de **ACI 318-19**.

## Mapa de conceptos

- **Materiales:** [[Módulo de elasticidad Ec]] · [[Módulo de ruptura fr]] · [[Relación modular n]] · [[Factor beta1]]
- **Sistema y geometría:** [[Sistemas de piso en dos direcciones]] · [[Marco de diseño y ancho l2]] · [[Claro libre ln]] · [[Sección efectiva de viga]] · [[Rigidez relativa alfa f]] · [[Relación de claros beta]] · [[Espesor mínimo de losa]]
- **Cargas:** [[Combinaciones de carga y wu]] · [[Patrones de carga viva]] · [[Peso del alma de las vigas]]
- **Diseño Directo:** [[Limitaciones del DDM]] · [[Momento estático Mo]] · [[Coeficientes longitudinales del DDM]] · [[Franja de columna y franja central]] · [[Porcentajes de la franja de columna]] · [[Constante torsional C]] · [[Rigidez torsional beta t]] · [[Reparto entre viga y losa]]
- **Marco Equivalente:** [[Marco equivalente]] · [[Miembro no prismático]] · [[Rigidez de la losa-viga Ksb]] · [[Rigidez de la columna Kc]] · [[Miembro a torsión Kt]] · [[Columna equivalente Kec]] · [[Factores de distribución]] · [[Distribución de momentos (Hardy Cross)]] · [[Momento en la cara del apoyo]] · [[Momentos de diseño y envolvente]]
- **Flexión:** [[Peralte efectivo d]] · [[Coeficiente Rn y cuantía]] · [[Acero mínimo]] · [[Separación de barras]] · [[Sección controlada por tensión]] · [[Resistencia de diseño a flexión]] · [[Recubrimiento]]
- **Cortante:** [[Cortante último Vu]] · [[Resistencia a cortante Vc]] · [[Efecto de tamaño lambda s]]
- **Deflexiones:** [[Momento de agrietamiento Mcr]] · [[Inercia agrietada Icr]] · [[Inercia efectiva Ie]] · [[Método de las franjas cruzadas]] · [[Flecha relativa a las vigas]] · [[Deflexión a largo plazo]] · [[Límites de deflexión]]
- **Detallado:** [[Longitud de desarrollo ld]] · [[Gancho estándar ldh]] · [[Empalme por traslape]] · [[Extensión de bastones]] · [[Anclaje del refuerzo inferior]] · [[Refuerzo de esquina]]
- **Verificación:** [[Elemento finito de placa]] · [[Modificadores de rigidez]] · [[Comparación con ETABS]]

## Alcance y límites

- Losas macizas, tableros rectangulares, 3 × 3, cargas de gravedad uniformes.
- **No** diseña vigas ni columnas, y **no** revisa punzonamiento (el enunciado del proyecto lo excluye).
- Referencias: ACI 318-19 (Cap. 6, 8, 19, 20, 21, 22, 24 y 25), ACI 318-14 (§8.10 y §8.11), ACI 435R, Wight (*Reinforced Concrete: Mechanics and Design*, 7.ª ed., cap. 13) y el ejemplo «Two-Way Concrete Floor Slab with Beams» de StructurePoint, con el que se validó el Marco Equivalente.
