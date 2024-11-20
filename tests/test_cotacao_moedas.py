from src.api.cotacao_moedas import cotacao
import responses
import random


@responses.activate
def test_cotacao1():
    price1 = random.randint(500, 600)/100
    price2 = random.randint(500, 600)/100
    json_moock = {'USDBRL':
                      {'code': 'USD', 'codein': 'BRL',
                       'name': 'Dólar Americano/Real '
                               'Brasileiro', 'high': '5.7969', 'low': '5.7448',
                       'varBid': '0.0034',
                       'pctChange': '0.06', 'bid': price1, 'ask': price2,
                       'timestamp':
                           '1732122825', 'create_date': '2024-11-20 14:13:45'}}

    http_get = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    responses.add(responses.GET, http_get, json=json_moock)
    assert cotacao() == (price1+price2)/2
