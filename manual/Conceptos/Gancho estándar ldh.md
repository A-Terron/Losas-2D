---
tags: [losas-2d, concepto, detallado]
---
# Gancho estándar ldh

**Qué es.** La longitud de anclaje de una barra que termina en gancho, medida desde la sección crítica hasta la cara exterior del gancho. Se usa donde no hay espacio para desarrollar la barra recta: los bastones en las vigas de borde.

![[F28-gancho-estandar.svg]]

**Fórmula.**

$$\ell_{dh}=\left(\frac{f_y\,\psi_e\,\psi_r\,\psi_o\,\psi_c}{55\,\lambda\sqrt{f'_c}}\right)d_b^{1.5}\ \ge\ \max(8d_b,\ 6\ \text{in})$$

| Factor | Valor |
|---|---|
| $\psi_r$ (confinamiento) | 1.0 si los ganchos están separados al menos $6d_b$ (o hay estribos suficientes); si no, 1.6 |
| $\psi_o$ (ubicación) | 1.0 dentro del núcleo de una columna o con recubrimiento lateral ≥ $6d_b$; si no, 1.25 (la hoja usa 1.25, del lado seguro) |
| $\psi_c$ (concreto) | $f'_c/15\,000+0.6$ si $f'_c$ < 6000 psi; si no, 1.0 |

**Geometría del gancho a 90°.** Diámetro interior de doblez $6d_b$ (barras #3 a #8) y tramo recto de $12d_b$ después del doblez.

**Comprobación.** El espacio disponible es el ancho del apoyo menos el recubrimiento; debe ser al menos $\ell_{dh}$.

**En la HT1 (#3).** La fórmula da 10.9 cm, pero rige el mínimo de 6 in = **15.2 cm**. Disponible: 35 − 2 = 33 cm. Cumple. Tramo recto 11.4 cm, doblez 5.7 cm.

**Referencia.** ACI 318-19 §25.4.3.1, Tabla 25.4.3.2, §25.3.1 y §8.7.4.1.1.

Se usa en: [[S11 Detallado del refuerzo]] · [[Extensión de bastones]]
