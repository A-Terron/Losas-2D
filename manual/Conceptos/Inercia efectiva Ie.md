---
tags: [losas-2d, concepto, deflexiones]
---
# Inercia efectiva Ie

**Qué es.** Una inercia intermedia entre la bruta $I_g$ y la agrietada $I_{cr}$ que representa la rigidez promedio de un miembro parcialmente agrietado.

**Fórmula (ACI 318-19, Tabla 24.2.3.5).**

$$I_e=\begin{cases} I_g & M_a\le \tfrac23 M_{cr}\\[6pt] \dfrac{I_{cr}}{1-\left(\dfrac{(2/3)M_{cr}}{M_a}\right)^2\left(1-\dfrac{I_{cr}}{I_g}\right)} & M_a> \tfrac23 M_{cr}\end{cases}$$

![[F22-inercia-efectiva.svg]]

**Variables.** $M_a$ momento máximo de servicio en la sección para el nivel de carga que se evalúa; $M_{cr}$ del [[Momento de agrietamiento Mcr]]; $I_{cr}$ de la [[Inercia agrietada Icr]].

**Por qué cambió respecto a 318-14.** La expresión de Branson, $I_e=(M_{cr}/M_a)^3 I_g+[1-(M_{cr}/M_a)^3]I_{cr}$, sobrestima la rigidez de miembros con poco acero, que es justo el caso de las losas. La nueva expresión promedia flexibilidades y adelanta el agrietamiento a $\tfrac23 M_{cr}$ para considerar la restricción por contracción.

**Promedio a lo largo del claro.** El miembro es continuo y su rigidez varía; se pondera el centro con los apoyos:

$$I_{e,prom}=0.70\,I_{e,m}+0.15\,(I_{e,1}+I_{e,2})\qquad\text{o}\qquad I_{e,prom}=0.85\,I_{e,m}+0.15\,I_{e,cont}$$

La primera para claros con dos extremos continuos, la segunda para claros extremos. ACI §24.2.3.6 permite promediar las secciones críticas; los pesos son los de ACI 435R.

**Cuándo se evalúa.** Una vez por nivel de carga (D, D + $\psi$L, D + L), porque $M_a$ cambia y con él $I_e$. Por eso la flecha por carga viva se obtiene restando: $\Delta(D+L)-\Delta(D)$.

**En la HT1 (eje 6, claro I–K, D + L).** $M_a$ = 10.50 > ⅔ × 11.23 = 7.49 → $I_e$ = 141 734 / [1 − (7.49/10.50)²(1 − 0.0885)] = **263 876 cm⁴**; $I_{e,prom}$ = 274 757 cm⁴ = 0.17 $I_g$. Con solo carga muerta ($M_a$ = 6.91 < 7.49) el centro no se agrieta e $I_{e,prom}$ = 0.88 $I_g$.

**La hoja permite** elegir la expresión de Branson solo para comparar.

**Referencia.** ACI 318-19 §24.2.3.5, §24.2.3.6; ACI 435R.

Se usa en: [[S10 Deflexiones]] · [[Método de las franjas cruzadas]]
