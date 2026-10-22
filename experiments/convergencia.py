"""Error a tiempo final fijo en función de dt, para los dos Euler.

Imprime una tabla con el orden observado entre filas sucesivas y genera
results/convergencia.png. Ejecutar desde la raíz del repositorio:

    uv run python experiments/convergencia.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from oscilador.simulacion import integrar_euler_explicito, integrar_euler_implicito, solucion_exacta

RESULTADOS = Path(__file__).resolve().parents[1] / "results"


def main() -> None:
    inicial = np.array([1.0, 0.0])
    tiempo_final = 2 * np.pi
    exacta = solucion_exacta(np.array([tiempo_final]), inicial)[0]
    pasos = np.array([25, 50, 100, 200, 400, 800])
    dts = tiempo_final / pasos

    figura, eje = plt.subplots(figsize=(6, 4))
    for nombre, integrar in (("explícito", integrar_euler_explicito), ("implícito", integrar_euler_implicito)):
        print(f"\nEuler {nombre}\n{'dt':>9} {'error':>11} {'orden':>7}")
        errores = []
        for dt, n in zip(dts, pasos):
            _, estados = integrar(inicial, dt, n)
            errores.append(np.max(np.abs(estados[-1] - exacta)))
            orden = f"{np.log2(errores[-2] / errores[-1]):.3f}" if len(errores) > 1 else "—"
            print(f"{dt:9.5f} {errores[-1]:11.3e} {orden:>7}")
        eje.loglog(dts, errores, "o-", label=f"Euler {nombre}")

    eje.set(xlabel="dt", ylabel="error en t = 2π", title="Convergencia a tiempo final fijo")
    eje.legend()
    RESULTADOS.mkdir(exist_ok=True)
    destino = RESULTADOS / "convergencia.png"
    figura.savefig(destino, dpi=150, bbox_inches="tight")
    print(f"\nfigura: {destino}")


if __name__ == "__main__":
    main()
