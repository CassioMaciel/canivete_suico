"""
Módulo Bhaskara

Este módulo contém uma função para resolver a equação quadrática utilizando a
 fórmula de Bhaskara.

Funções Disponíveis:
---------------------
1. `bhaskara(a, b, c) -> Tuple[float, float]`:
   Resolve a equação quadrática ax^2 + bx + c = 0 e retorna as raízes como uma
    tupla (x1, x2).
"""

from typing import Union
from typing import List


def bhaskara(
    a: Union[int, float] = 0,
    b: Union[int, float] = 0,
    c: Union[int, float] = 0,
) -> List[float]:
    """
    Essa função serve para calcular as raizes reais de
    uma equação de segundo grau.
    Deve-se entrar as 3 constantes, a b e c.
    A saida será uma lista, caso tenha 2 raízes.
    Será um float caso tenha 1 raiz
    Será um erro caso não tenha raiz
    ---------------------------------------------------------------------------
    Autor: Cássio Maciel Lemos
    E-mail: cassio.lemos@petrobras.com.br
    Desde: 2024-01-01
    Versão: 1
    Requisitos:
    Tags: matematica
    ---------------------------------------------------------------------------
    Uso:
    >>> bhaskara(a=2,b=1,c=-3)
    [1.0, -1.5]

    >>> bhaskara(a=-3,b=18,c=-15)
    [1.0, 5.0]

    >>> bhaskara(a=2,b=4,c=2)
    -1.0
    >>> bhaskara(a=2,b=2,c=2)
    Traceback (most recent call last):
    ...
    ValueError: A equação 2.0x²+2.0x+2.0=0 não tem valor real

    >>> bhaskara(a="joão",b=2,c=2)  # type: ignore
    Traceback (most recent call last):
    ...
    TypeError: Todas as entradas desse programa devem ser um número

    >>> bhaskara(a=2,b="joao",c=2)  # type: ignore
    Traceback (most recent call last):
    ...
    TypeError: Todas as entradas desse programa devem ser um número

    >>> bhaskara(a=2,b=2,c="joao") # type: ignore
    Traceback (most recent call last):
    ...
    TypeError: Todas as entradas desse programa devem ser um número
    """
    if not isinstance(a, (int, float)):
        raise TypeError('Todas as entradas desse programa devem ser um número')
    if not isinstance(b, (int, float)):
        raise TypeError('Todas as entradas desse programa devem ser um número')
    if not isinstance(c, (int, float)):
        raise TypeError('Todas as entradas desse programa devem ser um número')

    a = float(a)
    b = float(b)
    c = float(c)

    delta = b**2 - 4 * a * c

    if delta == 0:
        x = -b / (2 * a)
        return [x, x]

    if delta < 0:
        raise ValueError(f'A equação {a}x²+{b}x+{c}=0 não tem valor real')

    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    return [x1, x2]


if __name__ == '__main__':  # pragma: no cover
    import doctest

    doctest.testmod()
