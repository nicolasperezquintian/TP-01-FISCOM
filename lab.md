# Cuaderno de laboratorio

## Fecha — Oscilador con los dos Euler

### Afirmación

¿Qué pueden afirmar a partir de los tests y de las figuras?
Que realizar este tipo de aproximaciones no conservan la energía, pero reducir dt (a cantidad de períodos fija) mejora la aproximación

### Evidencia

- Comando ejecutado: uv run python experiments/muchos_ciclos.py
- Resultado cuantitativo: Al reducir dt se reduce |Ef-Eo|
- Figura regenerable:

### Limitaciones

¿Qué no permite concluir este experimento? Consideren tanto el modelo físico
como el método numérico.
Que la energía se conserva

### Próximo control

¿Qué prueba adicional harían para confiar más en el resultado?
Graficaría los residuos que resultan de solución_exacta-solución_aproximada