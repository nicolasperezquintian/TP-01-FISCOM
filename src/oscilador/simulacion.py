"""Oscilador con Euler explícito, Euler implícito y Newton–Raphson.

El estado se representa como ``[x, v]``. El tiempo se mide en unidades de
``1/ω``, con ``ω = sqrt(k/m)``: así la masa con resorte cumple ``x'' = -x`` y
un período dura ``2π``.

Los integradores reciben la aceleración como una función de la posición,
``a(x)``. Euler implícito recibe además su derivada ``da/dx``, que usa
Newton–Raphson.
"""

import numpy as np


def aceleracion_resorte(x: float) -> float:
    """Aceleración de la masa con resorte ideal, ``a(x) = -x``."""

    return -x


def derivada_aceleracion_resorte(x: float) -> float:
    """Derivada ``da/dx`` del resorte ideal."""

    return -1.0


def newton_raphson(G, derivada_G, z0: float, tolerancia: float = 1e-12, max_iter: int = 50) -> float:
    """Busca una raíz de ``G`` partiendo de ``z0``.

    Cada iteración reemplaza ``G`` por su recta tangente y toma el cero de esa
    recta: ``z ← z - G(z) / G'(z)``. Se detiene cuando el residuo ``|G(z)|`` es
    menor que ``tolerancia``: una corrección pequeña no alcanza si el residuo
    sigue siendo grande. Si la derivada se anula o no converge en ``max_iter``
    iteraciones, lanza ``ArithmeticError``: nunca devuelve en silencio un valor
    que no convergió.
    """
    iteracion = 0
    z = z0 #condición inicial de z

    #armo el bucle
    while iteracion < max_iter and abs(G(z)) > tolerancia:
        #manejo de error para la derivada
        dG = derivada_G(z)
        if dG == 0:
            raise ArithmeticError(f"derivada_G=0 en Newton-Raphson, iteración: {iteracion}")

        #actualizo z
        z = z - G(z) / dG
        iteracion += 1

    if iteracion == max_iter:
        raise ArithmeticError(f"Newton-Raphson no convirgió en {max_iter} iteraciones, residuo G(z)={G(z)}")
    else:
        return z

    raise NotImplementedError("completar Newton–Raphson")


def integrar_euler_explicito(
    estado_inicial: np.ndarray,
    dt: float,
    pasos: int,
    aceleracion=aceleracion_resorte,
) -> tuple[np.ndarray, np.ndarray]:
    """Integra ``x' = v``, ``v' = a(x)`` con Euler explícito.

    Cada paso usa la pendiente al **comienzo** del intervalo:

        x[n+1] = x[n] + dt v[n]
        v[n+1] = v[n] + dt a(x[n])

    Devuelve un arreglo de tiempos y otro de estados. Ambos incluyen la
    condición inicial, por lo que tienen ``pasos + 1`` elementos.
    """
    tiempos = np.linspace(0,dt*pasos,pasos+1)
    estados = np.zeros((pasos+1,2)) #tenemos dos variables de estado, x y v
    estados[0] = estado_inicial #condición inicial
    for i in range(1,pasos+1):
        x_n, v_n = estados[i-1] #estado anterior
        x_n1 = x_n + dt * v_n #estado actualizado de x
        v_n1 = v_n + dt * aceleracion(x_n) #estado actualizado de v
        estados[i] = [x_n1, v_n1] #actualizo el estado

    return tiempos, estados

    raise NotImplementedError("completar Euler explícito")


def integrar_euler_implicito(
    estado_inicial: np.ndarray,
    dt: float,
    pasos: int,
    aceleracion=aceleracion_resorte,
    derivada_aceleracion=derivada_aceleracion_resorte,
) -> tuple[np.ndarray, np.ndarray]:
    """Integra ``x' = v``, ``v' = a(x)`` con Euler implícito.

    Cada paso usa la pendiente al **final** del intervalo:

        x[n+1] = x[n] + dt v[n+1]
        v[n+1] = v[n] + dt a(x[n+1])

    Reemplazando la segunda ecuación en la primera queda una sola ecuación
    para ``z = x[n+1]``:

        G(z) = z - x[n] - dt v[n] - dt² a(z) = 0,

    que se resuelve con ``newton_raphson`` partiendo de ``z = x[n]``. Después,
    ``v[n+1]`` sale de la segunda ecuación.

    Devuelve tiempos y estados, con ``pasos + 1`` elementos cada uno.
    """
    tiempos = np.linspace(0,dt*pasos,pasos+1)
    estados = np.zeros((pasos+1,2)) #tenemos dos variables de estado, x y v
    estados[0] = estado_inicial #condición inicial  

    for i in range(1,pasos+1): #cuidado con los límites de la suma, acá había puesto (1,pasos) me saltaba un error por no terminaba de ser obvio que estaba acá
        #llamo a las variables del estado anterior
        x_n, v_n = estados[i-1]

        #Defino G y su derivada como variables únicamente de z
        def G(z):
            return z - x_n -dt * v_n - dt**2 * aceleracion(z)
        def derivada_G(z):
            return 1 - dt**2 * derivada_aceleracion(z)

        x_n1 = newton_raphson(G,derivada_G,x_n) #dejamos la tolerancia e iteraciones máximas por defecto definidas en la función y actualizamos x
        v_n1 = v_n - dt * x_n1 #actualizo v
        estados[i]=[x_n1,v_n1] #actualizo el estado

    return tiempos, estados

    raise NotImplementedError("completar Euler implícito")


def solucion_exacta(tiempos: np.ndarray, estado_inicial: np.ndarray) -> np.ndarray:
    """Solución del resorte ideal, ``x(t) = x0 cos t + v0 sin t``."""

    x0, v0 = np.asarray(estado_inicial, dtype=float)
    t = np.asarray(tiempos, dtype=float)
    return np.column_stack(
        (
            x0 * np.cos(t) + v0 * np.sin(t),
            -x0 * np.sin(t) + v0 * np.cos(t),
        )
    )


def energia(estados: np.ndarray) -> np.ndarray:
    """Energía del resorte por unidad de masa, ``(v² + x²) / 2``.

    Acepta un estado ``[x, v]`` o una tabla de estados de forma ``(n, 2)``.
    """

    estados = np.asarray(estados, dtype=float)
    return 0.5 * (estados[..., 0] ** 2 + estados[..., 1] ** 2)
