# Pregunta y predicciones

Completen este archivo **antes** de ejecutar los experimentos.

## Pregunta

¿Qué evidencia necesitamos para confiar en una trayectoria del oscilador
calculada durante muchos ciclos?

## Modelo y supuestos

- Una masa unida a un resorte ideal, sin rozamiento: $m x''=-kx$.
- Medimos el tiempo en unidades de $1/\omega$, con $\omega=\sqrt{k/m}$. Así la
  ecuación queda $x''=-x$ y un período dura $2\pi$.
- La energía por unidad de masa es $E=(x^2+v^2)/2$.

## Predicciones

1. ¿Qué forma tiene la órbita exacta en el plano $(x,v)$? ¿Qué pasa con la
   energía exacta a lo largo del tiempo?
2. Escriban a mano un paso de Euler explícito para $x''=-x$. ¿En qué factor
   cambia $x^2+v^2$ en ese paso? ¿Y en un paso de Euler implícito?
3. Con esa cuenta, ¿qué esperan que pase con la amplitud y con el período de
   la oscilación después de diez períodos con cada método? ¿Qué verían en el
   plano $(x,v)$?
4. Si `dt` se reduce a la mitad, ¿qué esperan que ocurra con el error a tiempo
   final fijo?
5. Para el resorte, ¿cuántas iteraciones de Newton esperan que haga falta en
   cada paso implícito?

## Criterio de aceptación

Propongan un criterio para decidir si un valor de `dt` es aceptable para
simular cien períodos. ¿Qué cantidad medirían y qué tolerancia le pedirían?
