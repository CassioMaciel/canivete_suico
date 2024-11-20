# pylint: disable=C0114
# pylint: disable=C0206
import warnings
import requests
from urllib3.exceptions import InsecureRequestWarning


def cotacao(moeda: str = 'USD-BRL', ssl_verify: bool = False) -> float:
    """
    Retorna a cotação média de uma moeda em relação ao Real Brasileiro (BRL).

    Esta função obtém a cotação da moeda especificada em relação ao Real Brasileiro (BRL)
    a partir da API da AwesomeAPI. A função retorna a média entre os valores de compra (bid)
    e venda (ask) da moeda.

    Parâmetros:
    ----------
    moeda : str, opcional
        A moeda para a qual obter a cotação. Valores permitidos são "USD-BRL" (padrão),
        "EUR-BRL" e "BTC-BRL".
    ssl_verify : bool, opcional
        Se `True`, verifica o certificado SSL. Caso o certificado SSL esteja expirado ou
        inválido, pode-se definir como `False` para ignorar a verificação SSL. O padrão é `False`.

    Retorna:
    -------
    float
        A cotação média da moeda escolhida em relação ao Real Brasileiro (BRL).
    """
    #cotacoes_json: requests.models.Response
    # cotacoes: dict
    http_get: str
    bid: float
    ask: float

    http_get = f'https://economia.awesomeapi.com.br/last/{moeda}'
    warnings.simplefilter('ignore', InsecureRequestWarning)
    cotacoes = requests.get(http_get, verify=ssl_verify, timeout=2.5).json()
    moeda = moeda.replace("-", "")
    bid = float(cotacoes[moeda]['bid'])
    ask = float(cotacoes[moeda]['ask'])
    usd_brl = (bid + ask)/2
    return usd_brl


if __name__ == '__main__':  # pragma: no cover
    entradas = {"Dólar": "USD-BRL",
                "euro": "EUR-BRL",
                "bitcoin": "BTC-BRL"}
    for coin in entradas:
        print(f"a cotação atual do {coin} é R$", end="")
        print(f'{cotacao(moeda=entradas[coin]):_.2f}')
