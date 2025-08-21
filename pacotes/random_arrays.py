import numpy as np

def numeros_uniformes(tamanho, minimo=0, maximo=1, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.uniform(minimo, maximo, tamanho)

def numeros_normais(tamanho, media=0, desvio=1, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.normal(media, desvio, tamanho)

def inteiros_aleatorios(tamanho, minimo=0, maximo=10, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(minimo, maximo, tamanho)

def criar_array(lista):
    return np.array(lista)

def array_zeros(forma):
    return np.zeros(forma)

def array_uns(forma):
    return np.ones(forma)

def operacoes_vetorizadas(array1, array2, operacao):
    if operacao == 'soma':
        return array1 + array2
    elif operacao == 'subtracao':
        return array1 - array2
    elif operacao == 'multiplicacao':
        return array1 * array2
    elif operacao == 'divisao':
        return array1 / array2
    else:
        raise ValueError("Operação inválida")

def funcoes_matematicas(array, funcao):
    if funcao == 'seno':
        return np.sin(array)
    elif funcao == 'cosseno':
        return np.cos(array)
    elif funcao == 'exponencial':
        return np.exp(array)
    elif funcao == 'logaritmo':
        return np.log(array)
    elif funcao == 'raiz_quadrada':
        return np.sqrt(array)
    else:
        raise ValueError("Função inválida")
