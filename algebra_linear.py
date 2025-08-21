import numpy as np
import numpy.linalg as alg

def calcular_determinante(matriz):
    return alg.det(np.array(matriz))

def calcular_inversa(matriz):
    matriz_np = np.array(matriz)
    if alg.det(matriz_np) == 0:
        raise ValueError("Matriz não tem inversa")
    return alg.inv(matriz_np)

def resolver_sistema(coeficientes, constantes):
    return alg.solve(np.array(coeficientes), np.array(constantes))

def autovalores_autovetores(matriz):
    return alg.eig(np.array(matriz))
