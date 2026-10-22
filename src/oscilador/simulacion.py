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
