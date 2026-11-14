---
tags: [losas-2d, concepto, deflexiones]
---
# Método de las franjas cruzadas

**Qué es.** La forma manual de obtener la flecha del centro de un tablero en dos direcciones: se calcula la flecha de una franja en cada dirección, como si fueran vigas, y se suman.

![[F24-franjas-cruzadas.svg]]

**Procedimiento por marco y claro.**

1. Flecha del marco completo con extremos empotrados:

$$\Delta_{marco}=\frac{w\,\ell^4}{384\,E_c\,I_{e,prom}}$$

2. Reparto a la franja de columna y a la central con el factor de distribución lateral y la relación de inercias brutas:

$$\Delta_{c,emp}=FDL_c\,\Delta_{marco}\,\frac{I_{marco}}{I_c}\qquad \Delta_{m,emp}=FDL_m\,\Delta_{marco}\,\frac{I_{marco}}{I_m}$$

$$FDL_c=\frac12\left[\%^{+}+\frac{\%^{-}_{izq}+\%^{-}_{der}}{2}\right]\cdot\frac{1}{100}\qquad FDL_m=1-FDL_c$$

3. Efecto del giro real de cada apoyo (los extremos no están empotrados del todo):

$$\Delta_\theta=\theta\,\frac{\ell}{8}\,\frac{I_g}{I_e}\qquad \theta=\frac{M_{desequilibrado}}{K_{ec}}$$

4. Flecha de cada franja: $\Delta_c=\Delta_{c,emp}+\Delta_{\theta,izq}+\Delta_{\theta,der}$ y lo mismo para $\Delta_m$.

5. Centro del tablero: franja de columna de una dirección más franja central de la otra, promediando las dos combinaciones:

$$\Delta_{centro}=\tfrac12\left[(\Delta_{cx}+\Delta_{my})+(\Delta_{cy}+\Delta_{mx})\right]$$

**Variables.** $w$ carga de servicio por unidad de longitud del marco; $\ell$ claro libre (o entre ejes, opción más conservadora); $I_c$ inercia bruta de la franja de columna (con la viga); $I_m=(\ell_2-b_{fc})\,h^3/12$ la de la franja central; los porcentajes son los de [[Porcentajes de la franja de columna]]; $\theta$ sale del [[Marco equivalente]].

**Por qué funciona.** La franja de columna se comporta como una viga entre columnas. La franja central de la otra dirección se apoya sobre dos franjas de columna que ya bajaron, así que su flecha se suma.

**Qué cambia según el caso.** Con vigas rígidas $I_c \gg I_m$: la franja de columna casi no baja y la central concentra la flecha. Sin vigas las dos franjas tienen inercias parecidas y la flecha total crece mucho.

**En la HT1 (eje 6, claro I–K, D + L).** $\Delta_{marco}$ = 0.216 cm; $FDL_c$ = 0.821; $I_{marco}/I_c$ = 1.18; $I_{marco}/I_m$ = 21.3 → $\Delta_c$ = 0.42 cm y $\Delta_m$ = 1.04 cm (incluyen 0.03 y 0.18 cm por giro de los apoyos).

**Validación.** Reproduce la tabla de deflexiones del ejemplo de StructurePoint para carga muerta ($\Delta_{marco}$ = 0.0063 in, $\Delta_c$ = 0.009 in, $\Delta_m$ = 0.021 in).

**Referencia.** ACI 435R §3.4; ACI 318-19 §24.2.3.3.

Se usa en: [[S10 Deflexiones]] · [[Flecha relativa a las vigas]]
