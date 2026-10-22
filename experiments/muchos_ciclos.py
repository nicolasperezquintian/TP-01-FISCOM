"""Integra el resorte durante muchos períodos con los dos Euler.

Genera results/muchos_ciclos.png: la órbita en el espacio de fases (x, v) y la
energía relativa en función del tiempo. Ejecutar desde la raíz del repositorio:

    uv run python experiments/muchos_ciclos.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from oscilador.simulacion import energia, integrar_euler_explicito, integrar_euler_implicito

RESULTADOS = Path(__file__).resolve().parents[1] / "results"


def main() -> None:
    inicial = np.array([1.0, 0.0])
    dt = 0.02
    periodos = 10
    pasos = round(periodos * 2 * np.pi / dt)

    figura, (fases, energias) = plt.subplots(1, 2, figsize=(10, 4))
    for nombre, integrar in (("explícito", integrar_euler_explicito), ("implícito", integrar_euler_implicito)):
        tiempos, estados = integrar(inicial, dt, pasos)
        relativa = energia(estados) / energia(inicial)
        fases.plot(estados[:, 0], estados[:, 1], lw=0.8, label=f"Euler {nombre}")
        energias.plot(tiempos / (2 * np.pi), relativa, label=f"Euler {nombre}")
        print(f"Euler {nombre}: E/E0 = {relativa[-1]:.3f} después de {periodos} períodos")

    # La órbita exacta es el círculo unitario porque el estado inicial es [1, 0].
    circulo = np.linspace(0.0, 2 * np.pi, 200)
    fases.plot(np.cos(circulo), np.sin(circulo), "k--", lw=1)
    fases.set(xlabel="x", ylabel="v", aspect="equal", title=f"Espacio de fases, dt = {dt} (exacta: trazos)")
    energias.axhline(1.0, color="black", ls="--", lw=1)
    energias.set(xlabel="tiempo [períodos]", ylabel="E / E0", title="Energía relativa")
    energias.legend()

    RESULTADOS.mkdir(exist_ok=True)
    destino = RESULTADOS / "muchos_ciclos.png"
    figura.savefig(destino, dpi=150, bbox_inches="tight")
    print(f"figura: {destino}")


if __name__ == "__main__":
    main()
