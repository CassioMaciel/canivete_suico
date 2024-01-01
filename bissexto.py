import datetime
from typing import Union


def bissexto(ano: Union[int, datetime.date] = datetime.date.today()):
    """
    --------------------------------------------------------------------------------------------------------------------
    Diz se o ano informado é bissexto ou não.
    Retorna 1 se for bissexto e 0 se não for
    Funciona com formato datetime ou inteiro
    Obs.: Se o ano não for informado, usa o atual.
    --------------------------------------------------------------------------------------------------------------------
    Autor: Cássio Maciel Lemos
    E-mail: cassio.lemos@petrobras.com.br
    Desde: 2024-01-01
    Versão: 1
    Requisitos:
    Tags: data
    --------------------------------------------------------------------------------------------------------------------
    A year is a leap year if it is evenly divisible by 4
    ...but not if it's evenly divisible by 100
    ...unless it's also evenly divisible by 400
    http://timeanddate.com
    http://www.delorie.com/gnu/docs/gcal/gcal_34.html
    http://en.wikipedia.org/wiki/Leap_year
    Uso:
    >>> bissexto(2000)
    1
    >>> bissexto(datetime.date(year=2000, month=1, day=1))
    1
    >>> bissexto(2003)
    0
    >>> bissexto(datetime.date(year=2003, month=1, day=1))
    0
    >>> bissexto(2022)
    0
    >>> bissexto(datetime.date(year=2022, month=1, day=1))
    0
    >>> bissexto(2023)
    0
    >>> bissexto(datetime.date(year=2023, month=1, day=1))
    0
    >>> bissexto(2024)
    1
    >>> bissexto(datetime.date(year=2024,month=1,day=1))
    1
    >>> bissexto(2100)
    0
    >>> bissexto(datetime.date(year=2100,month=1,day=1))
    0
    """

    if not isinstance(ano, datetime.date):
        # Tenta converter ano para datetime.date
        try:
            ano = datetime.date(year=int(ano), month=1, day=1)
        except (ValueError, TypeError):
            raise TypeError("O ano deve ser do tipo datetime.date ou ser convertível para datetime.date.")

    if ano.year % 400 == 0 or (ano.year % 4 == 0 and ano.year % 100 != 0):
        return 1
    else:
        return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assert bissexto(datetime.date(year=2024, month=1, day=1)) == 1
    assert bissexto(datetime.date(year=2023, month=1, day=1)) == 0
    assert bissexto(datetime.date(year=2000, month=1, day=1)) == 1
    assert bissexto(datetime.date(year=2003, month=1, day=1)) == 0
    assert bissexto(datetime.date(year=2100, month=1, day=1)) == 0
    assert bissexto(datetime.date(year=2400, month=1, day=1)) == 1
