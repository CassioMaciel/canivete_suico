"""
Módulo Bissexto

Este módulo contém uma função para resolver se o ano fornecido é bissexto

Funções Disponíveis:
---------------------
1. `bissexto(int) -> 1 ou 0`
"""
import datetime
from typing import Union


def bissexto(ano: Union[int, datetime.date] = datetime.date.today()) -> bool:
    """
    ---------------------------------------------------------------------------
    Diz se o ano informado é bissexto ou não.
    Retorna True se for bissexto e False se não for
    Funciona com formato datetime ou inteiro
    Obs.: Se o ano não for informado, usa o atual.
    ---------------------------------------------------------------------------
    Autor: Cássio Maciel Lemos
    E-mail: cassio.lemos@petrobras.com.br
    Desde: 2024-01-01
    Versão: 1
    Requisitos:
    Tags: data
    ---------------------------------------------------------------------------
    A year is a leap year if it is evenly divisible by 4
    ...but not if it's evenly divisible by 100
    ...unless it's also evenly divisible by 400
    http://timeanddate.com
    http://www.delorie.com/gnu/docs/gcal/gcal_34.html
    http://en.wikipedia.org/wiki/Leap_year
    Uso:
    >>> bissexto(2000)
    True
    >>> bissexto(datetime.date(year=2000, month=1, day=1))
    True
    >>> bissexto(2003)
    False
    >>> bissexto(datetime.date(year=2003, month=1, day=1))
    False
    >>> bissexto(2022)
    False
    >>> bissexto(datetime.date(year=2022, month=1, day=1))
    False
    >>> bissexto(2023)
    False
    >>> bissexto(datetime.date(year=2023, month=1, day=1))
    False
    >>> bissexto(2024)
    True
    >>> bissexto(datetime.date(year=2024,month=1,day=1))
    True
    >>> bissexto(2100)
    False
    >>> bissexto(datetime.date(year=2100,month=1,day=1))
    False
    """

    if not isinstance(ano, datetime.date):
        # Tenta converter ano para datetime.date
        try:
            ano = datetime.date(year=int(ano), month=1, day=1)
        except (ValueError, TypeError) as exc:
            raise TypeError(
                'O ano deve ser do tipo datetime.date ou ser '
                'convertível para datetime.date.'
            ) from exc

    if ano.year % 400 == 0 or (ano.year % 4 == 0 and ano.year % 100 != 0):
        return True

    return False


if __name__ == '__main__':   # pragma: no cover
    import doctest

    doctest.testmod()
