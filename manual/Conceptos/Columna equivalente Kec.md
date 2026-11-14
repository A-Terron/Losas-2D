---
tags: [losas-2d, concepto, efm]
---
# Columna equivalente Kec

**Qué es.** La columna ficticia que reúne la flexibilidad de las columnas reales y la del miembro a torsión.

![[F14-columna-equivalente.svg]]

**Fórmula.**

$$\frac{1}{K_{ec}} = \frac{1}{\sum K_c} + \frac{1}{K_{ta}}$$

**Por qué en serie.** El giro de la losa respecto a la base de la columna es la suma del giro de la columna más la torsión del miembro transversal: se suman **flexibilidades**, no rigideces.

**Cómo leerlo.** $K_{ec}$ siempre es menor que $\sum K_c$. Si el miembro a torsión es muy rígido (viga transversal grande), $K_{ec} \approx \sum K_c$.

**En la HT1.** 1 / (1/14 328 + 1/755 085) = 14 062 tonf·m: con vigas rígidas, casi igual a la columna sola.

**Referencia.** ACI 318-14 R8.11.4.

Se usa en: [[Factores de distribución]] · [[S06 Método del Marco Equivalente]] · [[Método de las franjas cruzadas]] (giro de los apoyos)
