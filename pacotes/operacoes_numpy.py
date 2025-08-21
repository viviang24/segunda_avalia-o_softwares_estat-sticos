from algebra_linear import calcular_determinante, calcular_inversa, resolver_sistema, autovalores_autovetores
from random_arrays import numeros_uniformes, numeros_normais, inteiros_aleatorios, criar_array, array_zeros, array_uns, operacoes_vetorizadas, funcoes_matematicas
import numpy as np

print("=== EXEMPLOS DE ÁLGEBRA LINEAR ===")
matriz = [[2, 1], [1, 3]]
print("1. Determinante:", calcular_determinante(matriz))

matriz2 = [[4, 7], [2, 6]]
print("2. Inversa:\n", calcular_inversa(matriz2))

coef = [[3, 1], [1, 2]]
const = [9, 8]
print("3. Solução do sistema:", resolver_sistema(coef, const))

valores, vetores = autovalores_autovetores([[2, -1], [1, 4]])
print("4. Autovalores:", valores)
print("   Autovetores:\n", vetores)

print("\n=== EXEMPLOS DE ARRAYS ===")
print("1. Uniformes:", numeros_uniformes(5, 0, 10, seed=42))
print("2. Normais:", numeros_normais(5, 5, 2, seed=42))
print("3. Inteiros:", inteiros_aleatorios(5, 1, 100, seed=42))

a = criar_array([1, 2, 3, 4])
b = criar_array([5, 6, 7, 8])
print("4. Soma:", operacoes_vetorizadas(a, b, "soma"))
print("5. Multiplicação:", operacoes_vetorizadas(a, b, "multiplicacao"))

angulos = np.array([0, np.pi/2, np.pi])
print("6. Senos:", funcoes_matematicas(angulos, "seno"))
print("7. Cossenos:", funcoes_matematicas(angulos, "cosseno"))

print("\n=== EXEMPLO COMBINADO ===")
matriz_rand = numeros_uniformes((3, 3), -5, 5, seed=123)
print("Matriz aleatória:\n", matriz_rand)
print("Determinante:", calcular_determinante(matriz_rand))
print("Exponencial:\n", funcoes_matematicas(matriz_rand, "exponencial"))
