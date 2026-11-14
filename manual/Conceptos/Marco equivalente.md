---
tags: [losas-2d, concepto, efm]
---
# Marco equivalente

**Qué es.** El modelo plano con el que el EFM representa un eje de columnas de la estructura tridimensional.

![[F11-marco-equivalente.svg]]

**Tres miembros.**

1. **Losa-viga:** la losa de ancho $\ell_2$ más la viga a lo largo del eje. → [[Rigidez de la losa-viga Ksb]]
2. **Columnas:** arriba y abajo de la losa. → [[Rigidez de la columna Kc]]
3. **Miembro a torsión:** franja transversal que conecta la losa con la columna. → [[Miembro a torsión Kt]]

Columna y miembro a torsión se combinan en la [[Columna equivalente Kec]].

**Por qué.** Reduce un problema de placa en 3D a marcos planos que se resuelven a mano, conservando el efecto de que la losa es mucho más ancha que la columna.

**Cuándo.** Siempre es válido para cargas de gravedad en marcos ortogonales; es obligado cuando el DDM no cumple sus limitaciones.

**Referencia.** ACI 318-19 §6.2.4.1; ACI 318-14 §8.11.

Se usa en: [[S06 Método del Marco Equivalente]]
