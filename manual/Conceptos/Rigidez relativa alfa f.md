---
tags: [losas-2d, concepto, sistema]
---
# Rigidez relativa alfa f

**Qué es.** La relación entre la rigidez a flexión de la viga y la de la franja de losa que le corresponde.

**Fórmula.**

$$\alpha_f = \frac{E_{cb}\,I_b}{E_{cs}\,I_s}\qquad I_s = \frac{\ell_2\,h^3}{12}$$

![[F04-franja-de-losa-para-alfa-f.svg]]

**Variables.** $I_b$ de la [[Sección efectiva de viga]]; $\ell_2$ del [[Marco de diseño y ancho l2]].

**Por qué.** Es el número que dice «cuánto ayuda la viga». Aparece en tres lugares: espesor mínimo ($\alpha_{fm}$), reparto de momentos ($\alpha_{f1}\ell_2/\ell_1$) y limitación 8.10.2.7 del DDM.

**Cómo leerlo.** $\alpha_f$ = 0: no hay viga. $\alpha_f \ge 0.8$: viga de borde eficaz. $\alpha_{fm}$ > 2: vigas rígidas.

**En la HT1.** 5.69 a 11.87; todas rígidas.

**Referencia.** ACI 318-19 Tabla 8.3.1.2 (nota) y ACI 318-14 §8.10.2.7.

Se usa en: [[S04 Rigidez de vigas y espesor mínimo]] · [[Porcentajes de la franja de columna]] · [[Reparto entre viga y losa]]
