---
tags: [losas-2d-u, concepto, una-direccion]
---
# Coeficientes de momento y cortante (§6.5)

**Qué es.** El método simplificado de ACI 318-19 para vigas continuas y losas en una dirección: momentos y cortantes como una fracción de $w_u\ell_n^2$ y $w_u\ell_n$.

**Condiciones (6.5.1).** Miembro prismático, carga uniforme, $L\le3D$, al menos dos claros, y el mayor de dos claros adyacentes no excede al menor en más de 20 %.

**Momentos (Tabla 6.5.2).**

| Sección | Condición | $M_u$ |
|---|---|---|
| Positivo, claro extremo | Extremo discontinuo monolítico con el apoyo | $w_u\ell_n^2/14$ |
| | Extremo discontinuo no restringido | $w_u\ell_n^2/11$ |
| Positivo, claro interior | | $w_u\ell_n^2/16$ |
| Negativo, cara interior del apoyo exterior | Monolítico con viga de borde | $w_u\ell_n^2/24$ |
| Negativo, cara exterior del primer apoyo interior | Dos claros | $w_u\ell_n^2/9$ |
| | Más de dos claros | $w_u\ell_n^2/10$ |
| Negativo, demás apoyos interiores | | $w_u\ell_n^2/11$ |
| Negativo, todos los apoyos | Losas con claros ≤ 10 ft (3.05 m) | $w_u\ell_n^2/12$ |

Para los momentos negativos, $\ell_n$ es el **promedio de los dos claros libres adyacentes**.

**Cortantes (Tabla 6.5.4).** $1.15\,w_u\ell_n/2$ en la cara exterior del primer apoyo interior; $w_u\ell_n/2$ en los demás. Para diseñar se toma a $d$ de la cara: $V_u=V_{cara}-w_ud$.

**Cómo elige la hoja.** Del apoyo y la continuidad de los dos bordes del claro, y de si el vecino es o no el último tablero (para distinguir dos claros de más de dos).

**Casos fuera del método.**

- Un claro sobre dos apoyos simples: estática, $M^+=w_u\ell_n^2/8$ con $\ell_n$ = claro libre + $h$ sin pasar de la distancia entre ejes (6.3.2.1).
- Un claro monolítico con sus apoyos: la hoja usa los coeficientes del claro extremo y avisa.

**En la hoja.** Sección 6 en una dirección. Ver [[S06 Momentos por DDM o por coeficientes]].
