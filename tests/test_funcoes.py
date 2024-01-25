import datetime
import pytest
from pytest import mark
import src as cs


def test_fatorial_de_5_igual_120():
    assert cs.fatorial(5) == 120


def test_fatorial_type_error():
    with pytest.raises(TypeError) as excinfo:
        cs.fatorial(3.5)  # type: ignore
    assert str(excinfo.value) == "A entrada desse programa só pode ser do " \
                                 "tipo int"


def test_fatorial_type_error_2():
    with pytest.raises(TypeError) as excinfo:
        cs.fatorial("batatinha")  # type: ignore
    assert str(excinfo.value) == "A entrada desse programa só pode ser do " \
                                 "tipo int"


def test_fatorial_value_error():
    with pytest.raises(ValueError) as excinfo:
        cs.fatorial(-1)
    assert str(excinfo.value) == 'So existe fatorial de numero positivo'


def test_bhaskara_1():
    assert cs.bhaskara(a=2, b=1, c=-3) == [1.0, -1.5]


def test_bhaskara_2():
    assert cs.bhaskara(a=-3, b=18, c=-15) == [1.0, 5.0]


def test_bhaskara_3():
    assert cs.bhaskara(a=2, b=4, c=2) == [-1.0, -1.0]


def test_baskara_4():
    with pytest.raises(ValueError) as excinfo:
        cs.bhaskara(a=2, b=2, c=2)
    assert str(excinfo.value) == 'A equação 2.0x²+2.0x+2.0=0 não tem valor ' \
                                 'real'


def test_baskara_5():
    with pytest.raises(TypeError) as excinfo:
        cs.bhaskara(a="joão", b=2, c=2)  # type: ignore
    assert str(excinfo.value) == 'Todas as entradas desse programa devem ' \
                                 'ser um número'


def test_baskara_6():
    with pytest.raises(TypeError) as excinfo:
        cs.bhaskara(a=2, b="joao", c=2)  # type: ignore
    assert str(excinfo.value) == 'Todas as entradas desse programa devem ' \
                                 'ser um número'


def test_baskara_7():
    with pytest.raises(TypeError) as excinfo:
        cs.bhaskara(a=2, b=2, c="joao")  # type: ignore
    assert str(excinfo.value) == 'Todas as entradas desse programa devem ' \
                                 'ser um número'


def test_finonacci_1():
    assert cs.fibonacci(5) == 5


def test_finonacci_2():
    with pytest.raises(TypeError) as excinfo:
        cs.fibonacci(3.5)  # type: ignore
    assert str(excinfo.value) == 'A entrada desse programa de ser do tipo int'


def test_bissexto_1():
    with pytest.raises(TypeError) as excinfo:
        cs.bissexto("joão")  # type: ignore
    assert str(excinfo.value) == 'O ano deve ser do tipo datetime.date ou ' \
                                 'ser convertível para datetime.date.'


@mark.parametrize('ano,resposta',
    [
        (2000, 1),
        (datetime.date(year=2000, month=1, day=1), 1),
        (2003, 0),
        (2003, 0),
        (datetime.date(year=2003, month=1, day=1), 0),
        (2022, 0),
        (datetime.date(year=2022, month=1, day=1), 0),
        (2023, 0),
        (datetime.date(year=2023, month=1, day=1), 0),
        (2024, 1),
        (datetime.date(year=2024, month=1, day=1), 1),
        (2100, 0),
        (datetime.date(year=2100, month=1, day=1), 0)
    ])
def test_bissexto_parametrize(ano, resposta):
    assert cs.bissexto(ano) == resposta
