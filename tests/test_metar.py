import pytest
import requests
from pytest import mark
from src.api.metar import Metar, dowload_metar
import responses


@mark.parametrize(
    'raw_text, dia, hora ,minuto, mes,ano , vel_vento,pressao,dir_vento, '
    'temp, t_orv',
    [
        ("2024111915 - METAR SBBR 191500Z VRB05KT CAVOK 28/18 Q1017=",
         "19", "15", "00", "11", "2024", "05", "1017", "VRB", "28", "18"),

        ("2024111919 - METAR SBBR 191900Z 30007KT 9999 BKN030 FEW040TCU 26/18 Q1014= ",
         "19", "19", "00", "11", "2024", "07", "1014", "300", "26", "18"),

        ("2024111919 - METAR SBBR 061311Z 31015G27KT 26/18 Q1014= ",
         "06", "13", "11", "11", "2024", "15", "1014", "310", "26", "18"),
     ],
)
def test_parse(raw_text, dia, hora, minuto, mes, ano, vel_vento, pressao,
               dir_vento,
               temp, t_orv):
    metar = Metar(raw_text)
    assert metar.dia == dia
    assert metar.hora == hora
    assert metar.minuto == minuto
    assert metar.mes == mes
    assert metar.ano == ano
    assert metar.vel_vento == vel_vento
    assert metar.dir_vento == dir_vento
    assert metar.pressao == pressao
    assert metar.temp_orvalho == t_orv
    assert metar.temperatura == temp


@mark.parametrize(
    'raw_text, dia, hora ,minuto, mes,ano , vel_vento,pressao,dir_vento, '
    'temp, t_orv',
    [
        ("2024111915 - METAR SBBR 191500Z VRB05KT CAVOK 28/18 Q1017=",
         "19", "15", "00", "11", "2024", "05", "1017", "VRB", "28", "18"),

        ("2024111919 - METAR SBBR 191900Z 30007KT 9999 BKN030 FEW040TCU 26/18 Q1014= ",
         "19", "19", "00", "11", "2024", "07", "1014", "300", "26", "18"),

        ("2024111919 - METAR SBBR 061311Z 31015G27KT 26/18 Q1014= ",
         "06", "13", "11", "11", "2024", "15", "1014", "310", "26", "18"),
        ("",
         "", "", "", "", "", "", "", "", "", ""),
     ],
)

@responses.activate
def test_metar(
    raw_text, dia, hora, minuto, mes, ano, vel_vento, pressao, dir_vento,
        temp, t_orv) -> None:
    icao = "sbbr"
    site = f'http://redemet.decea.gov.br//api/consulta_automatica/index.php?' \
           f'local={icao}&msg=metar'
    responses.add(responses.GET, site, raw_text)
    # responses.get(site, body = raw_text)
    result = dowload_metar(icao)
    print(result.temperatura)
    assert result.dia == dia
    assert result.hora == hora
    assert result.minuto == minuto
    assert result.mes == mes
    assert result.ano == ano
    assert result.vel_vento == vel_vento
    assert result.dir_vento == dir_vento
    assert result.pressao == pressao
    assert result.temp_orvalho == t_orv
    assert result.temperatura == temp


@responses.activate
def test_icao_not_found():
    raw_text = "2024112019 - Mensagem METAR de 'SBXX' para 20/11/2024 as " \
               '19(UTC) não localizada na base de dados da REDEMET'
    icao = "sbxxx"
    site = f'http://redemet.decea.gov.br//api/consulta_automatica/' \
           f'index.php?' \
           f'local={icao}&msg=metar'
    responses.get(site, body=raw_text)
    with pytest.raises(ValueError):
        dowload_metar(icao)


@responses.activate
def test_connection_error():
    # Se eu coloco para buscar um site diferente do configurado no responses
    # ele me retorna um Connection Error
    icao = "sbbr"
    site = f'http://redemet.decea.gov.br//api/consulta_automatica/' \
           f'index.php?local={icao}&msg=metar'
    responses.add(responses.GET,
                  site,
                  body=requests.exceptions.ConnectionError()
                  )
    with pytest.raises(ConnectionError):
        dowload_metar(icao)
