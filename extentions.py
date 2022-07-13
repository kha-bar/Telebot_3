import requests
import json
from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевезти одинаковые валюты. {quote} в {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')#.json()

        if quote_ticker == 'RUB':
            quote_rate = 1
        else:
            quote_rate = json.loads(req.content)['Valute'][quote_ticker]['Value']

        if base_ticker == 'RUB':
            base_rate = 1
        else:
            base_rate = json.loads(req.content)['Valute'][base_ticker]['Value']
        total_base = quote_rate * amount / base_rate
        return total_base





