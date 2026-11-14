---
tags: [losas-2d, concepto, deflexiones]
---
# Límites de deflexión

**Qué es.** Las flechas máximas que el Código admite, según lo que la losa soporta.

![[F26-flechas-y-limites.svg]]

| Miembro | Flecha que se revisa | Límite |
|---|---|---|
| Cubiertas planas sin elementos frágiles | Inmediata por $L_r$, $S$ o $R$ | $\ell/180$ |
| Pisos sin elementos frágiles | Inmediata por carga viva $L$ | $\ell/360$ |
| Pisos o cubiertas con elementos no estructurales **propensos** a dañarse | La que ocurre después de colocarlos | $\ell/480$ |
| Ídem, **no** propensos a dañarse | La que ocurre después de colocarlos | $\ell/240$ |

**La flecha «posterior».** Es la de largo plazo por todas las cargas sostenidas más la inmediata por la carga viva adicional:

$$\Delta_{post}=\lambda_\Delta\,\Delta_{i,sost}+\Delta_{i,L}$$

**Qué $\ell$ usar.** Con flecha relativa, el claro de la franja que se evalúa. Con flecha del centro del tablero, la hoja deja elegir entre claro corto (conservador), claro largo o diagonal.

**Cuándo aplica cada uno.** En el parqueo de la HT1 no hay tabiques ni acabados frágiles: se revisa $\ell/360$ para la carga viva y $\ell/240$ para la posterior. Si sobre la losa hay muros de mampostería o vidrio, se usa $\ell/480$.

**En la HT1 (T6).** $\Delta_{i,L}$ = 0.91 cm ≤ 670/360 = 1.86 cm. $\Delta_{post}$ = 1.44 cm ≤ 670/240 = 2.79 cm. Cumple ambos.

**Referencia.** ACI 318-19 Tabla 24.2.2 y §8.3.2.

Se usa en: [[S10 Deflexiones]]
