---
tags: [losas-2d, concepto, ddm]
---
# Momento estático Mo

**Qué es.** El momento total que debe resistir un claro del marco: el de una viga simplemente apoyada de ancho $\ell_2$ y claro libre $\ell_n$.

![[F07-momento-estatico.svg]]

**Fórmula.**

$$M_o = \frac{w_u\,\ell_2\,\ell_n^2}{8}$$

**Variables.** $w_u$ carga última por área; $\ell_2$ ancho del marco; $\ell_n = \ell_1 - c_1 \ge 0.65\,\ell_1$.

**Por qué.** Es pura estática: en cualquier claro, $M^+ + \tfrac12(M^-_{izq} + M^-_{der}) = M_o$. Los métodos solo difieren en **cómo** lo reparten.

**Cómo usarlo de control.** Suma el positivo y el promedio de los negativos de cualquier análisis (incluido el FEM): debe dar cerca de $M_o$.

**En la HT1.** Eje 6, claro F–I: 0.892 × 5.36 × 6.20² / 8 = 22.97 tonf·m.

**Referencia.** ACI 318-14 Ec. 8.10.3.2.

Se usa en: [[S05 Método de Diseño Directo]] · Relacionado: [[Coeficientes longitudinales del DDM]]
