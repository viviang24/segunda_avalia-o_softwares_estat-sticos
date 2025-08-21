# Meu Projeto NumPy

Este projeto demonstra funções de álgebra linear e operações com arrays utilizando Python e NumPy.

## Estrutura do Projeto

```
meu_projeto_numpy/
├── pacotes/
│   ├── algebra_linear.py        # Funções de álgebra linear (determinante, inversa, sistemas, autovalores)
│   ├── random_arrays.py         # Funções para arrays, números aleatórios e operações matemáticas
│   └── operacoes_numpy.py       # Script principal com exemplos de uso
├── pyproject.toml               # Configuração do projeto Python
├── README.md                    # Documentação do projeto
```

## Instalação

Certifique-se de ter o Python instalado.  
Instale o NumPy com:

```bash
pip install numpy
```

Se desejar instalar dependências via `pyproject.toml`, utilize um gerenciador como Poetry ou PDM:

```bash
poetry install
```
ou
```bash
pdm install
```

## Como Usar

Execute o script principal para ver exemplos:

```bash
python pacotes/operacoes_numpy.py
```

Você também pode importar as funções nos seus próprios scripts:

```python
from pacotes.algebra_linear import calcular_determinante
from pacotes.random_arrays import numeros_uniformes
```

## Exemplos

Veja exemplos de uso em `pacotes/operacoes_numpy.py` ou adicione seus próprios testes.

## Licença

Este projeto é livre para uso. 
