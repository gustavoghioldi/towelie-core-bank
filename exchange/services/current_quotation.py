"""
    A class used to represent the current quotation for a pair of currencies.
"""
class CurrentQuotation:

    def __init__(self, currency_source, currency_target):
        self.currency_source = currency_source
        self.currency_target = currency_target
        self.price = 0
        self.last_datetime = None

    def __str__(self):
        return f'Pair: {self.currency_source}-{self.currency_target}, price: {self.price}, last update: {self.last_datetime}'
