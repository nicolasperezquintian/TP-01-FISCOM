# Oscilador: Euler explícito, Euler implícito y Newton–Raphson

En este repositorio van a implementar los dos métodos de Euler y el método de
Newton–Raphson, comprobarlos con tests y usarlos para integrar una masa con
resorte durante muchos períodos.

## 1. Crear y clonar tu repositorio

1. Abrí el [repositorio base](https://github.com/fisica-computacional-ib/fiscom-2026-01-oscilador).
2. Elegí **Use this template** y luego **Create a new repository**.
3. Creá un repositorio **privado** en tu cuenta. Podés llamarlo
   `fiscom-2026-01-oscilador`.
4. Cloná tu repositorio, no el repositorio base de la cátedra:

   ```bash
   git clone https://github.com/<TU-USUARIO>/fiscom-2026-01-oscilador.git
   cd fiscom-2026-01-oscilador
   ```

Reemplazá `<TU-USUARIO>` por tu nombre de usuario de GitHub.

## 2. Preparar el entorno

Si todavía no instalaron `uv`, sigan la
[página de instalación](https://fisica-computacional-ib.github.io/contenidos/la-materia/06-instalacion.html).
Desde la raíz del repositorio:

```bash
uv sync
uv run pytest
```

La primera vez, varios tests fallarán con `NotImplementedError` porque las
funciones todavía no están implementadas. Ese es el punto de partida, no un
problema de instalación.

## 3. Trabajar

1. Lean `question.md` y anoten sus predicciones **antes** de simular.
2. Completen, en `src/oscilador/simulacion.py` y en este orden:
   1. `integrar_euler_explicito`;
   2. `newton_raphson`;
   3. `integrar_euler_implicito`, que usa `newton_raphson` en cada paso.
3. Después de cada función, corran `uv run pytest` hasta que pasen sus tests.
   Pueden correr un solo archivo, por ejemplo `uv run pytest tests/test_newton.py`.
4. Generen las figuras con:

   ```bash
   uv run python experiments/muchos_ciclos.py
   uv run python experiments/convergencia.py
   ```

5. Abran las figuras de `results/` y completen `lab.md`.
6. Si usaron IA, documenten en `ai-use.md` qué delegaron y cómo lo verificaron.
7. Guarden el trabajo en su repositorio, con un commit por cada función que
   deja sus tests en verde:

   ```bash
   git add -A
   git commit -m "Implementa Euler explícito"
   git push
   ```

## Estructura

```text
README.md                        instalación y recorrido
question.md                      predicciones previas
src/oscilador/simulacion.py      modelos, métodos y solución exacta
tests/test_newton.py             controles de Newton–Raphson
tests/test_euler.py              controles de los dos Euler
experiments/muchos_ciclos.py     órbita y energía durante diez períodos
experiments/convergencia.py      error en función de dt
results/                         resultados regenerables
lab.md                           afirmación, evidencia y limitaciones
ai-use.md                        uso y verificación de IA
pyproject.toml                   Python y dependencias
```
