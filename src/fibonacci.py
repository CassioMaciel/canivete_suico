"""
Módulo Fibonacci

Este módulo calcula o numero de fibonacci

Funções Disponíveis:
---------------------
1. `fibonacci(entrada: int) -> numero`:
"""

def fibonacci(entrada: int):
    # noinspection PyTypeChecker
    """
    ---------------------------------------------------------------------------
    Essa função serve para calcular o elemento da sequencia de indice entrada
    ---------------------------------------------------------------------------
    Parameters
    entrada : int
    ---------------------------------------------------------------------------
    Returns
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    >>> fibonacci(8.5)
    Traceback (most recent call last):
    ...
    TypeError: A entrada desse programa de ser do tipo int
    """
    if not isinstance(entrada, int):
        raise TypeError("A entrada desse programa de ser do tipo int")

    f_n_menos_1 = 1
    f_n_menos_2 = 1
    f_n = 1

    i = 2
    while i < entrada and i < 500:
        f_n = f_n_menos_1 + f_n_menos_2
        f_n_menos_2 = f_n_menos_1
        f_n_menos_1 = f_n
        i += 1
    return f_n


if __name__ == '__main__':  # pragma: no cover
    import doctest
    doctest.testmod()
