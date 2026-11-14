---
tags: [losas-2d, concepto, cortante]
---
# Cortante último Vu

**Qué es.** La fuerza cortante mayorada por metro de ancho en la sección crítica de la losa.

![[F21-cortante-areas-tributarias.svg]]

**Fórmula.**

$$V_u = C_v\,w_u\,(a_{trib} - d)$$

**Ancho tributario.**

- Con vigas rígidas en los cuatro lados: la carga se reparte a las vigas por áreas limitadas por líneas a 45° desde las esquinas. La franja más cargada está al centro del lado largo y tiene $a_{trib}$ = medio claro libre **corto**.
- Sin vigas: $a_{trib}$ = medio claro libre entre columnas, en cada dirección.

**Por qué se resta $d$.** La sección crítica está a $d$ de la cara del apoyo; la carga más cercana baja directo al apoyo por compresión.

**$C_v$.** 1.15 en el primer apoyo interior de un claro extremo, donde la continuidad aumenta el cortante; 1.0 en los demás.

**En la HT1.** T3, dirección X: 1.15 × 0.892 × (2.505 − 0.116) = 2.45 tonf/m.

**Referencia.** ACI 318-19 §8.4.3.2 y Tabla 6.5.4; ACI 318-14 §8.10.8.1.

Se usa en: [[S09 Cortante en una dirección]]
