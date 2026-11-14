---
tags: [losas-2d, concepto, deflexiones]
---
# Momento de agrietamiento Mcr

**Qué es.** El momento con el que la fibra más tensionada de la sección bruta alcanza el módulo de ruptura y el concreto empieza a agrietarse.

**Fórmula.**

$$M_{cr}=\frac{f_r\,I_g}{y_t}$$

**Variables.** $f_r$ del [[Módulo de ruptura fr]]; $I_g$ inercia bruta de la sección; $y_t$ distancia del centroide a la fibra en tensión.

**Cómo se aplica en la hoja.** Se calcula para la sección del **marco completo**, no para un metro de losa, porque la flecha se obtiene del marco:

| Zona | Sección | Fibra en tensión |
|---|---|---|
| Centro del claro ($M^+$) | T: losa de ancho $\ell_2$ más el alma de la viga | Inferior, $y_t = h_b - \bar y$ |
| Apoyos ($M^-$) | Rectángulo del alma $b_w \times h_b$ (el patín queda en tensión y se desprecia) | Superior, $y_t = h_b/2$ |
| Sin viga | Losa $\ell_2 \times h$ en ambas zonas | $y_t = h/2$ |

**Por qué importa.** Es el umbral que separa la sección sin agrietar (rígida) de la agrietada (mucho más flexible). En ACI 318-19 el umbral efectivo es $\tfrac23 M_{cr}$: ver [[Inercia efectiva Ie]].

**En la HT1 (eje 6, claro I–K).** Centro: 33.35 × 1 601 835 / 47.59 = 1 122 500 kgf·cm = **11.23 tonf·m**. Apoyo: 33.35 × 630 000 / 30 = **7.00 tonf·m**.

**Referencia.** ACI 318-19 Tabla 24.2.3.5 (definición de $M_{cr}$) y §19.2.3.1.

Se usa en: [[S10 Deflexiones]] · [[Inercia efectiva Ie]]
