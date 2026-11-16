---
tags: [losas-2d-u, flujo]
---
# Diagrama de flujo general

El recorrido de la hoja se bifurca una sola vez: en la [[S04 Clasificación del tablero|clasificación]]. De ahí en adelante cada rama usa su capítulo del Código, y las dos vuelven a encontrarse en flexión, cortante, deflexiones y detallado.

```mermaid
flowchart TD
    A(["Materiales, tablero, bordes, vecinos y cargas"]) --> B["wu = máx(1.4D, 1.2D + 1.6L)"]
    B --> C{"Apoyos y relación de claros"}
    C -- "apoyo en 2 lados opuestos<br/>o 4 lados con relación > 2" --> U1["UNA DIRECCIÓN · Cap. 7"]
    C -- "4 lados con relación ≤ 2<br/>o apoyo en columnas" --> T1["DOS DIRECCIONES · Cap. 8"]
    C -- "3 lados y uno libre" --> X(["Fuera del alcance"])
    U1 --> U2["h mín · Tabla 7.3.1.1"]
    U2 --> U3["Mu y Vu con coeficientes · Tablas 6.5.2 y 6.5.4"]
    T1 --> T2["alfa f de cada borde y h mín · Tabla 8.3.1.1 u 8.3.1.2"]
    T2 --> T3["Marco de cada borde: tablero + vecinos"]
    T3 --> T4["DDM: Mo, coeficientes y reparto transversal"]
    T3 --> T5["EFM: Ksb, Kec, patrones y envolvente"]
    T4 --> T6["Momento de diseño: DDM, EFM o envolvente"]
    T5 --> T6
    T6 --> T7["Momentos por metro en franja de columna y franja central"]
    U3 --> F["Flexión: As, barra y separación"]
    T7 --> F
    F --> V["Cortante en una dirección"]
    V --> P{"¿Columna sin viga?"}
    P -- Sí --> P2["Punzonamiento · 22.6"]
    P -- No --> D["Deflexiones · 24.2"]
    P2 --> D
    D --> E["Detallado: ld, ganchos, bastones, esquinas"]
    E --> R(["Resumen de verificaciones"])
```

## Qué decide cada bifurcación

| Decisión | Dónde | Nota |
|---|---|---|
| Una o dos direcciones | Sección 4 | [[Una o dos direcciones]] |
| Tabla de espesor mínimo | Sección 5 | [[S05 Espesor mínimo]] |
| Caso del claro extremo del DDM | Sección 6 | [[Caso del claro extremo]] |
| Cómo termina el marco | Sección 7 | [[Marco del tablero]] |
| DDM, EFM o envolvente | Sección 8 | [[Envolvente DDM-EFM]] |
| Si hay punzonamiento | Sección 11 | [[Sección crítica de punzonamiento]] |
