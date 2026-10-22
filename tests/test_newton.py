import numpy as np
import pytest

from oscilador.simulacion import newton_raphson


def test_encuentra_raiz_de_dos() -> None:
    """La raíz positiva de z² - 2 es √2."""

    raiz = newton_raphson(lambda z: z**2 - 2, lambda z: 2 * z, z0=1.0)
    assert raiz == pytest.approx(np.sqrt(2), abs=1e-12)


def test_paso_implicito_del_ejemplo_de_clase() -> None:
    """Euler implícito para y' = -k y² con y_n = h = k = 1 exige z + z² - 1 = 0.

    La raíz positiva es (√5 - 1) / 2 ≈ 0.618034.
    """

    raiz = newton_raphson(lambda z: z - 1 + z**2, lambda z: 1 + 2 * z, z0=1.0)
    assert raiz == pytest.approx((np.sqrt(5) - 1) / 2, abs=1e-12)


def test_avisa_si_no_converge() -> None:
    """z² - 2 tiene raíz y z² + 1 no: en el segundo caso Newton tiene que lanzar
    ArithmeticError, no devolver cualquier cosa."""

    assert newton_raphson(lambda z: z**2 - 2, lambda z: 2 * z, z0=0.5) == pytest.approx(np.sqrt(2))
    with pytest.raises(ArithmeticError):
        newton_raphson(lambda z: z**2 + 1, lambda z: 2 * z, z0=0.5)
