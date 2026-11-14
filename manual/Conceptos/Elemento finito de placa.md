---
tags: [losas-2d, concepto, verificacion]
---
# Elemento finito de placa

**Qué es.** El bloque con el que la hoja construye su modelo de verificación: un rectángulo de placa delgada (teoría de Kirchhoff) con tres incógnitas por nodo.

![[F31-modelo-de-elementos-finitos.svg]]

**Incógnitas por nodo.** La flecha $w$ y sus dos pendientes, $\partial w/\partial x$ y $\partial w/\partial y$. Cuatro nodos → 12 grados de libertad. La flecha dentro del elemento se interpola con un polinomio de 12 términos.

**Rigidez de la placa.**

$$D=\frac{E_c\,h^3}{12\,(1-\nu^2)}$$

**Momentos por unidad de ancho.**

$$m_x=-D\left(\frac{\partial^2 w}{\partial x^2}+\nu\frac{\partial^2 w}{\partial y^2}\right)\qquad m_y=-D\left(\frac{\partial^2 w}{\partial y^2}+\nu\frac{\partial^2 w}{\partial x^2}\right)$$

$m_x$ es el momento que arma el acero paralelo a X.

**Los otros miembros.** Las vigas son barras sobre las líneas de ejes, con rigidez a flexión y a torsión. Las columnas impiden la flecha en su nodo y aportan resortes de giro $4E_cI_c/\ell_c$ (extremo lejano empotrado).

**Cómo se compara con DDM y EFM.** El momento de una franja es la integral de $m_x$ a lo largo de un corte: en la cara de la columna para los negativos y en el centro del claro para el positivo. Sumando la viga se obtiene el momento total del marco.

**Límites del modelo.** Es elástico y lineal: no agrieta, no redistribuye y carga todos los tableros a la vez (sin patrones). La columna es un punto, por eso el pico de momento negativo sobre ella es mayor que en la cara.

**Comprobación del elemento.** Placa cuadrada simplemente apoyada con carga uniforme: coeficiente de flecha 0.00408 frente a 0.00406 de la solución exacta.

**En la HT1.** 8 divisiones por claro → 24 × 24 elementos y 1875 grados de libertad.

**Referencia.** ACI 318-19 §6.9 (análisis por elementos finitos) y §8.2.1.

Se usa en: [[S12 Verificación FEM y ETABS]] · [[S07 Momentos de diseño y comparación]]
