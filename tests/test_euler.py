import numpy as np
import pytest

from oscilador.simulacion import (
    energia,
    integrar_euler_explicito,
    integrar_euler_implicito,
    solucion_exacta,
)


def test_solucion_exacta_parte_del_estado_inicial_y_conserva_la_energia() -> None:
    """La referencia contra la que comparamos también tiene que ser controlada."""

    inicial = np.array([0.3, -1.2])
    tiempos = np.linspace(0.0, 50.0, 1001)
    exacta = solucion_exacta(tiempos, inicial)
    np.testing.assert_allclose(exacta[0], inicial)
    assert np.ptp(energia(exacta)) < 1e-12


def test_euler_explicito_hace_un_paso_con_la_pendiente_inicial() -> None:
    """Desde [1, 0]: x no cambia porque v = 0, y v cambia según a(1) = -1."""

    tiempos, estados = integrar_euler_explicito(np.array([1.0, 0.0]), dt=0.1, pasos=1)
    np.testing.assert_allclose(tiempos, [0.0, 0.1])
    np.testing.assert_allclose(estados, [[1.0, 0.0], [1.0, -0.1]])


def test_euler_implicito_hace_un_paso_con_la_pendiente_final() -> None:
    """Para el resorte, las dos ecuaciones del paso implícito son lineales:

    x[1] - dt v[1] = x[0],  dt x[1] + v[1] = v[0].

    El test resuelve ese sistema de 2×2 por separado y compara.
    """

    dt = 0.1
    inicial = np.array([1.0, 0.0])
    tiempos, estados = integrar_euler_implicito(inicial, dt=dt, pasos=1)
    esperado = np.linalg.solve([[1.0, -dt], [dt, 1.0]], inicial)
    np.testing.assert_allclose(tiempos, [0.0, dt])
    np.testing.assert_allclose(estados[1], esperado, rtol=1e-12)


@pytest.mark.parametrize("integrar", [integrar_euler_explicito, integrar_euler_implicito])
def test_los_dos_euler_son_de_primer_orden(integrar) -> None:
    """Compara el error a tiempo final fijo con dt y dt/2. Si falla, el método
    no tiene el orden que corresponde a Euler."""

    inicial = np.array([1.0, 0.0])
    tiempo_final = 2.0
    exacta = solucion_exacta(np.array([tiempo_final]), inicial)[0]
    errores = []
    for dt in (0.01, 0.005):
        _, estados = integrar(inicial, dt, round(tiempo_final / dt))
        errores.append(np.max(np.abs(estados[-1] - exacta)))
    assert errores[0] / errores[1] == pytest.approx(2.0, rel=0.05)
