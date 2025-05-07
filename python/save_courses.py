class ExchangeRates:
    def __init__(self):
        self.rates = {}

    def set_rate(self, from_currency, to_currency, rate):
        self.rates[(from_currency, to_currency)] = rate

    def get_rate(self, from_currency, to_currency):
        return self.rates.get((from_currency, to_currency), None)

    def display_rates(self):
        for (from_currency, to_currency), rate in self.rates.items():
            print(f"{from_currency} -> {to_currency}: {rate}")

exchange_rates = ExchangeRates()
exchange_rates.set_rate("USD", "EUR", 0.92)
exchange_rates.set_rate("EUR", "USD", 1.09)
exchange_rates.display_rates()
usd_to_eur = exchange_rates.get_rate("USD", "EUR")
print(f"Курс USD -> EUR: {usd_to_eur}")