from exchange.services.current_quotation import CurrentQuotation

import requests, logging, datetime, statistics

logger = logging.getLogger(__name__)


"""
A class for get currency quotation from an exchange.
"""
class ExchangeCurrencyService:

    quotations = {}

    """
    Returns the currency pair quotation.
    """
    @staticmethod
    def get_quotation(self, currency_source: str, currency_target: str):

        key = f'{currency_source}{currency_target}'

        if self.quotations.get(key):
            logger.info('Retrieving quotation from cache')

            return self.quotations.get(key)
        else:
            logger.info('Looking for the quote in the API')

            response = self.generate_request('https://criptoya.com/api', 'buenbit', currency_source, currency_target)

            quotation = CurrentQuotation(currency_source, currency_target)
            quotation.price = statistics.mean([float(response['totalAsk']), float(response['totalBid'])])
            quotation.last_datetime = datetime.datetime.fromtimestamp(response['time'])

            self.quotations[key] = quotation

            return quotation

    def generate_request(self, base_url:str, exchange:str, coin:str, fiat:str):
        response = requests.get(f'{base_url}/{exchange}/{coin}/{fiat}')

        if response.status_code == 200:
            return response.json()
