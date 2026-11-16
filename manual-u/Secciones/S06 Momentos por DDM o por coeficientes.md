---
tags: [losas-2d-u, seccion, ddm, coeficientes]
hoja: 6
aci: ["6.2.4.1", "6.5", "8.10 (318-14)"]
---
# S06 · Momentos: Diseño Directo (dos direcciones) o coeficientes (una dirección)

> [!abstract] En una frase
> En dos direcciones, el DDM reparte el momento estático $M_o$ de cada marco con coeficientes; en una dirección, la Tabla 6.5.2 da directamente los momentos de la franja de 1 m.

## Dos direcciones · Método de Diseño Directo

### Diagrama de flujo

```mermaid
flowchart TD
    A(["Marco de un borde del tablero"]) --> B["l2 = medio tablero + medio vecino (o borde de losa)"]
    B --> C["ln = l1 − caras de apoyo ≥ 0.65·l1"]
    C --> D["Mo = wu·l2·ln² / 8"]
    D --> E{"¿Extremos del claro?"}
    E -- "Los dos continuos" --> F["0.65 / 0.35 / 0.65"]
    E -- "Uno discontinuo" --> G["Tabla 8.10.4.2 según el caso"]
    E -- "Los dos discontinuos" --> H["Un solo claro: fuera del DDM"]
    F --> I["En cada apoyo compartido: el mayor de los dos claros"]
    G --> I
    H --> I
    I --> J["% a franja de columna: l2/l1, alfa f·l2/l1, beta t"]
    J --> K["85 % de la franja de columna a la viga si alfa f·l2/l1 ≥ 1"]
    K --> L(["Losa en franja de columna y franja central"])
```

### Procedimiento

1. **Limitaciones** (318-14 §8.10.2): tres claros, claros sucesivos que no difieran más de un tercio, relación ≤ 2, $L\le2D$ y relación de rigideces de vigas entre 0.2 y 5. La hoja las revisa con los datos de los vecinos; si alguna falla, diseña con el EFM. Ver [Limitaciones del DDM](https://a-terron.github.io/Losas-2D/manual/Conceptos/Limitaciones%20del%20DDM/).
2. **Momento estático** del marco de cada borde: [Marco de diseño y ancho l2](https://a-terron.github.io/Losas-2D/manual/Conceptos/Marco%20de%20dise%C3%B1o%20y%20ancho%20l2/), [Claro libre ln](https://a-terron.github.io/Losas-2D/manual/Conceptos/Claro%20libre%20ln/), [Momento estático Mo](https://a-terron.github.io/Losas-2D/manual/Conceptos/Momento%20est%C3%A1tico%20Mo/).
3. **Reparto longitudinal:** 0.65/0.35/0.65 en un claro interior; en un claro extremo, el [[Caso del claro extremo]]. El claro vecino lleva su propio momento al apoyo compartido y se diseña con el mayor (§8.10.4.5).
4. **Reparto transversal** con las tablas de §8.10.5: [Porcentajes de la franja de columna](https://a-terron.github.io/Losas-2D/manual/Conceptos/Porcentajes%20de%20la%20franja%20de%20columna/), [Rigidez torsional beta t](https://a-terron.github.io/Losas-2D/manual/Conceptos/Rigidez%20torsional%20beta%20t/), [Reparto entre viga y losa](https://a-terron.github.io/Losas-2D/manual/Conceptos/Reparto%20entre%20viga%20y%20losa/). Sobre un muro el momento negativo se reparte uniforme: [[Apoyo en muro]].

### Qué cambia según el caso

| Caso | Cambio |
|---|---|
| Marco de borde | $\ell_2$ más pequeño; en las tablas de reparto se usa el claro transversal completo |
| Tablero aislado | [[Tablero de un solo claro]] |
| Vecino con otro claro | Puede gobernar el momento negativo del vecino |
| Caso forzado | El selector «Caso del claro extremo» sustituye la detección automática |

### Ejemplo · HT1, T5, dirección X, marco del eje 6

$\ell_2$ = 5.36 m, $\ell_n$ = 6.70 − 0.50 = 6.20 m, $M_o$ = 0.892·5.36·6.20²/8 = **22.97 tonf·m**.

Claro interior: 14.93 / 8.04 / 14.93 tonf·m. En el eje I el vecino (claro extremo, 0.70) lleva 16.08 tonf·m, que gobierna. $\ell_2/\ell_1$ = 0.80 y $\alpha_{f1}\ell_2/\ell_1$ = 5.69 → 81 % a la franja de columna, de la que la viga toma el 85 %. Quedan para la losa 1.81 / 0.98 / 1.95 tonf·m en la franja de columna y 2.84 / 1.53 / 3.06 en la central.

## Una dirección · coeficientes de §6.5

```mermaid
flowchart TD
    A(["Franja de 1 m en el claro de trabajo"]) --> B["ln entre caras de apoyo"]
    B --> C{"Extremo A y extremo B"}
    C -- "Apoyo simple" --> D["M− = 0"]
    C -- "Discontinuo monolítico" --> E["M− = wu·ln²/24"]
    C -- "Primer apoyo interior" --> F["M− = wu·ln²/10 (o /9 con dos claros)"]
    C -- "Otro apoyo interior" --> G["M− = wu·ln²/11"]
    D --> H["M+ = wu·ln²/11 (extremo libre), /14 (extremo) o /16 (interior)"]
    E --> H
    F --> H
    G --> H
    H --> I["Vu = wu·ln/2, por 1.15 en el primer apoyo interior"]
```

Todas las reglas y sus condiciones están en [[Coeficientes de momento y cortante 6.5]].

### Ejemplo · losa continua de 3.50 m

$w_u$ = 814 kgf/m², $\ell_n$ = 3.25 m, claro interior: $M^-$ = 814·3.25²/11 = 782 kgf·m/m y $M^+$ = 814·3.25²/16 = 538 kgf·m/m.
