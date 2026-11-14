---
tags: [losas-2d, concepto, materiales]
---
# Módulo de elasticidad Ec

**Qué es.** La pendiente del tramo inicial de la curva esfuerzo–deformación del concreto. Mide cuánto se deforma el concreto bajo carga.

**Fórmula.**

$$E_c = 57\,000\sqrt{f'_c}\ \text{(peso normal)}\qquad E_c = w_c^{1.5}\,33\sqrt{f'_c}\ \ (90 \le w_c \le 160\ \text{lb/ft}^3)$$

**Variables.** $f'_c$ en psi; $w_c$ peso unitario en lb/ft³; $E_c$ en psi.

**Por qué.** Todas las rigideces ($K_{sb}$, $K_c$, $K_t$) y todas las flechas son proporcionales a $E_c$.

**Cuándo.** Al inicio; se recalcula si cambia $f'_c$.

**Según el caso.** Con concreto liviano usa la segunda expresión. El ejemplo de StructurePoint usa la segunda con 150 lb/ft³ (da 3834 ksi en lugar de 3605 ksi).

**En la HT1.** $57\,000\sqrt{4000}$ = 3 605 000 psi = 253 456 kgf/cm².

**Referencia.** ACI 318-19 §19.2.2.1.

Se usa en: [[S01 Materiales]] · [[S06 Método del Marco Equivalente]] · [[S10 Deflexiones]] · Relacionado: [[Relación modular n]]
