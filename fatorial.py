def fatorial(entrada: int):
    # noinspection PyTypeChecker
    """
    Essa função serve para calcular o fatorial de um numero inteiro fornecido.
    --------------------------------------------------------------------------------------------------------------------
    Autor: Cássio Maciel Lemos
    E-mail: cassio.lemos@petrobras.com.br
    Desde: 2024-01-01
    Versão: 1
    Requisitos:
    Tags: matematica
    --------------------------------------------------------------------------------------------------------------------
    Uso:
    >>> fatorial(0)
    1
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    >>> fatorial(5)
    120
    >>> fatorial(6)
    720
    >>> fatorial(7)
    5040
    >>> fatorial(8)
    40320
    >>> fatorial(9)
    362880
    >>> fatorial(10)
    3628800
    >>> fatorial(3.5)
    Traceback (most recent call last):
    ...
    TypeError: A entrada desse programa de ser do tipo int
    """
    if not isinstance(entrada, int):
        raise TypeError("A entrada desse programa de ser do tipo int")

    output = 1
    for i in range(entrada+1)[1:]:
        output *= i

    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
