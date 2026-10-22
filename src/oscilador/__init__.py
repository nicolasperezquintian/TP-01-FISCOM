"""Herramientas mínimas para simular un oscilador con los dos métodos de Euler."""

from .simulacion import (
    aceleracion_resorte,
    derivada_aceleracion_resorte,
    energia,
    integrar_euler_explicito,
    integrar_euler_implicito,
    newton_raphson,
    solucion_exacta,
)

__all__ = [
    "aceleracion_resorte",
    "derivada_aceleracion_resorte",
    "energia",
    "integrar_euler_explicito",
    "integrar_euler_implicito",
    "newton_raphson",
    "solucion_exacta",
]
