---
tags: [losas-2d, diagrama-de-flujo]
---
# Diagrama de flujo general

Recorrido completo del diseño de la losa, en el orden en que lo hace la hoja. Cada caja lleva a su nota de sección; los rombos son las decisiones que cambian el camino.

```mermaid
flowchart TD
    A(["Inicio: planta, materiales y cargas"]) --> S1["S01 Materiales<br/>Ec, fr, n, beta1"]
    S1 --> S2["S02 Sistema y geometría<br/>claros, columnas, vigas"]
    S2 --> D0{"¿Claros entre 3 y 8 m<br/>y relación largo/corto ≤ 2?"}
    D0 -- No --> X0["Ajustar la planta:<br/>fuera del alcance de losa en dos direcciones"] --> S2
    D0 -- Sí --> S3["S03 Cargas<br/>wD, wL, wu, L/D"]
    S3 --> S4["S04 Rigidez de vigas y espesor<br/>alfa f, alfa fm, beta, h mín"]
    S4 --> D1{"¿h ≥ h mín?"}
    D1 -- No --> D1b{"¿Subir el espesor?"}
    D1b -- Sí --> S2
    D1b -- No --> N1["Se permite seguir solo si las<br/>deflexiones calculadas cumplen (8.3.2)"]
    D1 -- Sí --> S5
    N1 --> S5["S05 Método de Diseño Directo<br/>Mo, coeficientes, franjas"]
    S5 --> D2{"¿Cumple las limitaciones<br/>del DDM (8.10.2)?"}
    D2 -- No --> N2["El DDM no aplica:<br/>diseñar solo con EFM"]
    D2 -- Sí --> S6
    N2 --> S6["S06 Marco Equivalente<br/>Ksb, Kc, Kt, Kec, distribución"]
    S6 --> D3{"¿L/D > 0.75?"}
    D3 -- Sí --> P1["Patrones de carga viva<br/>con 3/4 de L mayorada"]
    D3 -- No --> P2["Un solo caso: carga total<br/>en todos los claros"]
    P1 --> S7
    P2 --> S7["S07 Momentos de diseño<br/>DDM, EFM o envolvente"]
    S7 --> S8["S08 Flexión<br/>As, barra y separación por franja"]
    S8 --> D4{"¿fi·Mn ≥ Mu, s ≤ s máx,<br/>As ≥ As mín y controlada por tensión?"}
    D4 -- No --> X4["Cambiar barra o separación,<br/>o aumentar h"] --> S8
    D4 -- Sí --> S9["S09 Cortante en una dirección<br/>Vu frente a fi·Vc"]
    S9 --> D5{"¿fi·Vc ≥ Vu?"}
    D5 -- No --> X5["Aumentar h"] --> S2
    D5 -- Sí --> S10["S10 Deflexiones<br/>inmediata, largo plazo, límites"]
    S10 --> D6{"¿Cumple l/360 y l/240 (o l/480)?"}
    D6 -- No --> X6["Aumentar h o la rigidez de vigas"] --> S2
    D6 -- Sí --> S11["S11 Detallado<br/>ld, ganchos, bastones, esquinas"]
    S11 --> S12["S12 Verificación FEM y ETABS"]
    S12 --> D7{"¿Diferencias razonables<br/>con el FEM?"}
    D7 -- No --> X7["Revisar datos, rigideces<br/>y el modelo"] --> S6
    D7 -- Sí --> Z(["Fin: planos de armado y memoria"])
```

## Cómo leerlo

- **El espesor manda al principio.** Casi todas las vueltas hacia atrás regresan a la geometría porque subir $h$ cambia el peso propio, la rigidez $\alpha_f$, los momentos, el cortante y las deflexiones a la vez.
- **DDM y EFM corren en paralelo.** No son pasos sucesivos: son dos formas de obtener los mismos momentos. La hoja calcula ambos y diseña con la envolvente, salvo que elijas uno.
- **El FEM va al final** porque el proyecto lo pide solo como verificación independiente, no como método principal.

## Diagramas por sección

Cada nota de sección trae su propio diagrama con todos los pasos internos:

[[S01 Materiales]] · [[S02 Sistema estructural y geometría]] · [[S03 Cargas]] · [[S04 Rigidez de vigas y espesor mínimo]] · [[S05 Método de Diseño Directo]] · [[S06 Método del Marco Equivalente]] · [[S07 Momentos de diseño y comparación]] · [[S08 Diseño por flexión]] · [[S09 Cortante en una dirección]] · [[S10 Deflexiones]] · [[S11 Detallado del refuerzo]] · [[S12 Verificación FEM y ETABS]]

Volver a [[00 Inicio]].
