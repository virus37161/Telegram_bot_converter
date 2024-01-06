import requests
import json
from config import keys

class Exceptionn(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise Exceptionn("Укажите боту корректные валюты для перевода")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Exceptionn(f"Валюта {quote} введена некорректно")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise Exceptionn(f"Валюта {base} введена некорректно")

        try:
            amount = float(amount)
        except ValueError:
            raise Exceptionn(f"Введено не корректное количество {amount}")

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=6951f4d4fd80fae0cae0ca6bf547ed67')
        text = json.loads(r.content).get('data').get(keys.get(quote) + keys.get(base))
        return text