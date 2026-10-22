# Pregunta y predicciones

Completen este archivo **antes** de ejecutar los experimentos.

## Pregunta

¿Qué evidencia necesitamos para confiar en una trayectoria del oscilador
calculada durante muchos ciclos?

## Respuesta
Ver que luego de n ciclos: |x(t+n*T)-x(t)|<<tolerancia

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

## Respuesta a predicciones

1. La órbita debería ser una circunferencia en el plano que lo medimos. La energía exacta debería ser constante. Pero, intuyo que al estar aproximando, va a fluctuar y, ¿quedarse alrededor de su valor original?
2. Para Euler explícito, $E_{n+1}=E_n(1+dt^2)$ (va aumentando). Para Euler implícito $E_{n+1}=E_n/(1+dt^2)$ (va disminuyendo).
3. El cambio de energía sólo cambia la amplitud, no la frecuencia. Así que esperaría ver que la amplitud va aumentando o disminuyendo según use el método explícito o implícito, respectivamente. No sé qué ocurrirá con el período.
4. Si dt es suficientemente chico, entre dos pasos el error debería reducirse a poco más de la mitad. Haciendo n pasos, ocurre lo mismo, el error se reduce a casi la mitad. Pues $(1+dt^2)^n=1+ndt^2+O(ndt^2)^2$, mientras que $(1+(dt/2)^2)^{2n}=1+ndt^2/2+O(ndt^2)^2$. El error respecto a al energía.
5. Depende de la tolerancia y dt, pero estimo que, ¿alrededor de 5 pasos? 


## Criterio de aceptación

Propongan un criterio para decidir si un valor de `dt` es aceptable para
simular cien períodos. ¿Qué cantidad medirían y qué tolerancia le pedirían?

## Respuesta

1. Mediría E y pediría que $|E_f-E_o|<tolerancia$
2. Mediría $|x_f-x_o|<np.sqrt{2*tolerancia}$
Pondría tolerancia=10^{-5} por decir algo.
