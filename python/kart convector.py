class Wallet:
    def __init__(self, currency, initial_balance):
        self.currency = currency
        self.balance = initial_balance

    def add_funds(self, amount):
        self.balance += amount

    def subtract_funds(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

class ExchangeRates:
    def __init__(self):
        self.rates = {}

    def set_rate(self, from_currency, to_currency, rate):
        self.rates[(from_currency, to_currency)] = rate

    def get_rate(self, from_currency, to_currency):
        return self.rates.get((from_currency, to_currency), None)

def convert(wallet_from, wallet_to, amount, exchange_rates):
    rate = exchange_rates.get_rate(wallet_from.currency, wallet_to.currency)
    if rate is None:
        raise ValueError("Exchange rate not found")
    converted_amount = amount * rate

    wallet_from.subtract_funds(amount)

    wallet_to.add_funds(converted_amount)

wallet1 = Wallet("USD", 1000)
wallet2 = Wallet("EUR", 500)

exchange_rates = ExchangeRates()
exchange_rates.set_rate("USD", "EUR", 0.92)

convert(wallet1, wallet2, 100, exchange_rates)

print(f"Wallet 1 (USD): {wallet1.balance}")
print(f"Wallet 2 (EUR): {wallet2.balance}")