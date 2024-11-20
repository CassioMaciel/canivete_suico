# pylint: disable=R0902
# pylint: disable=R0903
"""
Este módulo fornece funcionalidades para buscar e analisar relatórios METAR
de aeroportos Brazileiros.

O METAR é um relatório meteorológico de rotina para a aviação que fornece
informações sobre as condições meteorológicas em um aeroporto específico.

Para mais informações, verificar:
https://metar-taf.com/pt/explanation

Classes:
--------
Metar
    Representa um relatório METAR e fornece métodos para analisar seus
     componentes.
    raw_text : str
        O texto bruto do relatório METAR.
    hora : str
        A hora do relatório METAR.
    minuto : str
        O minuto do relatório METAR.
    dia : str
        O dia do relatório METAR.
    pressao : str
        A pressão atmosférica no relatório METAR.
    temperatura : str
        A temperatura no relatório METAR.
    temp_orvalho : str
        A temperatura do ponto de orvalho no relatório METAR.
    vel_vento : str
        A velocidade do vento no relatório METAR.
    dir_vento : str
        A direção do vento no relatório METAR.
    mes : str
        O mês do relatório METAR.
    ano : str
        O ano do relatório METAR.

Funções:
--------
download_metar(icao: str = 'sbbr') -> Metar
    Busca o METAR de um aeroporto pelo seu código ICAO.

"""
import re
import requests


class Metar:
    """
    Representa um relatório METAR e fornece métodos
    para analisar seus componentes.

    Atributos:
    ----------
    raw_text : str
        O texto bruto do relatório METAR.
    hora : str
        A hora do relatório METAR.
    minuto : str
        O minuto do relatório METAR.
    dia : str
        O dia do relatório METAR.
    pressao : str
        A pressão atmosférica no relatório METAR.
    temperatura : str
        A temperatura no relatório METAR.
    temp_orvalho : str
        A temperatura do ponto de orvalho no relatório METAR.
    vel_vento : str
        A velocidade do vento no relatório METAR.
    dir_vento : str
        A direção do vento no relatório METAR.
    mes : str
        O mês do relatório METAR.
    ano : str
        O ano do relatório METAR.
    """
    def __init__(self, raw_text: str = ""):
        pattern_1 = r'([0-9]{2})([0-9]{2})([0-9]{2})Z'           # 202200Z
        pattern_2 = r'Q([0-9]{4})'                               # Q1015
        pattern_3 = r' ([0-9]{2})/([0-9]{2}) Q'                  # 25/18
        pattern_4 = r' (...)([0-9]{2})(G[0-9]{2})?KT'            # 26006KT
        pattern_5 = r'^([0-9]{4})([0-9]{2})[0-9]{4}'             # 2024112022 -
        self.raw_text: str = re.sub('\n', "", raw_text)
        self.hora = self._factory_set_functions(pattern_1, 2)
        self.minuto = self._factory_set_functions(pattern_1, 3)
        self.dia = self._factory_set_functions(pattern_1, 1)
        self.pressao = self._factory_set_functions(pattern_2, 1)
        self.temperatura = self._factory_set_functions(pattern_3, 1)
        self.temp_orvalho = self._factory_set_functions(pattern_3, 2)
        self.vel_vento = self._factory_set_functions(pattern_4, 2)
        self.dir_vento = self._factory_set_functions(pattern_4, 1)
        self.mes = self._factory_set_functions(pattern_5, 2)
        self.ano = self._factory_set_functions(pattern_5, 1)

    def _factory_set_functions(self,
                               pattern: str,
                               group: int) -> str:
        match = re.search(pattern, self.raw_text)
        if match is not None:
            return match.group(group)
        return ""


def dowload_metar(icao: str = 'sbbr') -> Metar:
    """
    Busca o METAR de um aeroporto pelo seu código ICAO.

    METAR é um relatório meteorológico de rotina para a aviação que fornece
    informações sobre as condições meteorológicas em um aeroporto específico.

    Parâmetros:
    -----------
    icao : str, opcional
        O código ICAO do aeroporto para o qual se deseja obter o METAR.
        O código ICAO é um código de quatro letras que identifica
        exclusivamente cada aeroporto. O valor padrão é 'sbbr' (Brasília).

    Retorna:
    --------
    str
        O relatório METAR do aeroporto especificado.

    Exceções:
    ---------
    ValueError
        Se a resposta da API não contiver o relatório METAR esperado.
    """

    site = f'http://redemet.decea.gov.br//api/consulta_automatica/index.php?'\
           f'local={icao}&msg=metar'
    try:
        raw_text = requests.get(site, timeout=2.5).text
    except requests.exceptions.ConnectionError as exc:
        raise ConnectionError('Houve um erro de conecção com a API') from exc

    regex_erro_icao = r'não localizada na base de dados da REDEMET'
    pattern_erro_icao = re.compile(regex_erro_icao)
    icao_existe = re.search(pattern_erro_icao, raw_text, flags=0)

    if icao_existe is not None:
        raise ValueError('Código ICAO não encontrado')
    return Metar(raw_text)


if __name__ == '__main__':  # pragma: no cover
    variable = dowload_metar('sbxxx')
    print(variable.raw_text)
    print('O metar foi emitido as: ', end="")
    print(f'{variable.dia}/{variable.mes}/{variable.ano}', end="")
    print(f' as {variable.hora}:{variable.minuto} horas, ZULU')
    print(f"a velocidade do vento é {variable.vel_vento} nós")
    print(f"a direção do vento é {variable.dir_vento}")
    print(f"a temperatura é {variable.temperatura} graus celsius")
    print(f"a temperatura de orvalho é {variable.temp_orvalho} graus celsius")
    print(f"a pressão é {variable.pressao} hPa")
