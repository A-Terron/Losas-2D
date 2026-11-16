---
tags: [losas-2d-u, validacion]
---
# Validación

> [!abstract] En una frase
> Con los claros de sus vecinos, un tablero aislado reproduce el marco completo: Losas 2D U da los mismos momentos, acero, espesor y deflexiones que el modelo de 3 × 3 tableros.

## Contra el modelo completo (hoja Losas 2D)

Los dos motores se ejecutaron uno al lado del otro sobre los nueve tableros de la HT1, con cada método de diseño.

| Método | Mayor diferencia en momentos por metro y separaciones | Deflexiones | Espesor mínimo |
|---|---|---|---|
| DDM | 1.3 × 10⁻¹⁵ (precisión de máquina) | idénticas | idéntico |
| EFM | 1.4 × 10⁻¹⁴ | idénticas | idéntico |
| Envolvente | 1.3 × 10⁻¹⁵ | idénticas | idéntico |

También coinciden los momentos del DDM en sistemas sin vigas, sin vigas con viga de borde y con vigas en una sola dirección.

## Diferencias que sí existen, y por qué

| Dónde | Diferencia | Motivo |
|---|---|---|
| Cortante | La resistencia $\phi V_c$ puede ser algo menor aquí | Esta hoja revisa **los dos extremos** del claro y toma el de menor acero; el modelo solo mira el primer apoyo interior |
| Bastones | La extensión puede variar un múltiplo de redondeo (5 cm) | El modelo envuelve los puntos de inflexión de los cuatro marcos de cada dirección; esta hoja, solo los dos del tablero |
| Marco truncado | Hasta 5 % en momentos del EFM si no se da el segundo vecino | El extremo lejano se supone empotrado (ver [[Marco del tablero]]) |

## Verificaciones a mano

| Qué | Caso | Resultado |
|---|---|---|
| Coeficientes de una dirección | Losa continua de 3.50 m, $w_u$ = 814 kgf/m², $\ell_n$ = 3.25 m | $M^-$ = 814·3.25²/11 = 782 kgf·m/m y $M^+$ = 814·3.25²/16 = 538 kgf·m/m: coincide |
| Losa simplemente apoyada | 3.50 m sobre muros, $w_u$ = 958 kgf/m², $\ell_n$ = 3.48 m | $M^+$ = 958·3.48²/8 = 1450 kgf·m/m: coincide |
| Punzonamiento, columna interior | Placa plana 6 × 6 m, $h$ = 20 cm | $v_{uv}$ = 8.73, $v_u$ = 10.75 y $\phi v_c$ = 13.34 kgf/cm²: D/C = 0.81, coincide |

## Prueba de robustez

4000 combinaciones aleatorias de apoyos, continuidad, vecinos, dimensiones, materiales y métodos: ninguna produjo un error de cálculo.

## Fórmulas y artículos

La trazabilidad fórmula → artículo de las expresiones compartidas (materiales, $\alpha_f$, DDM, EFM, flexión, cortante, deflexiones, longitudes de desarrollo) está en la nota de verificación del manual de Losas 2D, enlazada en [[05 Relación con el manual de Losas 2D]]. Las propias de esta hoja son:

| Fórmula | Artículo |
|---|---|
| $h_{mín}=\ell/20,\ \ell/24,\ \ell/28$ | ACI 318-19 Tabla 7.3.1.1 |
| Momentos $w_u\ell_n^2/k$ | Tabla 6.5.2 |
| Cortantes $1.15\,w_u\ell_n/2$ y $w_u\ell_n/2$ | Tabla 6.5.4 |
| $A_{s,mín}=0.0018A_g$ | 7.6.1.1 · 8.6.1.1 |
| $s_{máx}$ = mín($3h$, 18 in) y control de agrietamiento | 7.7.2.3 · 24.3.2 |
| Acero de temperatura 0.0018, $s\le$ mín($5h$, 18 in) | 24.4.3.2 · 24.4.3.3 |
| $v_c$ = mín(4, 2+4/β, 2+α_s d/b_o)·λ_s λ√f′c | Tabla 22.6.5.2 |
| $\gamma_f = 1/(1+\tfrac23\sqrt{b_1/b_2})$, $\gamma_v=1-\gamma_f$ | 8.4.2.2.2 · 8.4.4.2.2 |
| $M_{sc}$ = 0.3$M_o$ (borde) y 0.07[…] (interior) | 318-14 §8.10.7.3 · §8.10.7.2 |
| $A_{s,mín}=5v_{uv}b_{slab}b_o/(\phi\alpha_s f_y)$ | 8.6.1.2 |
| Extremo lejano empotrado | 318-14 §8.11.2.5 |
| Momento negativo uniforme en $\ell_2$ sobre muros | 318-14 §8.10.5.4 |
