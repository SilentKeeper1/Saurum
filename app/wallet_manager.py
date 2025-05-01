import json
import os

class WalletManager:
    def __init__(self, storage_file='Saurum/app/data/wallets.json'):
        self.storage_file = storage_file
        self.wallets = {}
        self.exchange_rates = {}
        self.transaction_log = []
        self.load_data()

    def create_wallet(self, currency, balance):
        if currency in self.wallets:
            raise ValueError(f"Wallet with currency {currency} already exists.")
        self.wallets[currency] = balance
        self.transaction_log.append(f"Створено гаманець: {currency} з балансом {balance}") 
        self.save_data()

    def set_balance(self, currency, amount):
        self.wallets[currency] = amount
        self.transaction_log.append(f"Баланс гаманця {currency} встановлено на {amount}")  
        self.save_data()

    def delete_wallet(self, currency):
        if currency in self.wallets:
            del self.wallets[currency]
            self.transaction_log.append(f"Видалено гаманець: {currency}")  
            self.save_data()

    def get_wallet(self):
        return self.wallets

    def add_exchange_rate(self, from_currency, to_currency, rate):
        self.exchange_rates[(from_currency, to_currency)] = rate
        self.transaction_log.append(f"Встановлено курс: {from_currency} → {to_currency} = {rate}") 
        self.save_data()

    def convert(self, from_currency, to_currency, amount):
        if (from_currency, to_currency) not in self.exchange_rates:
            raise ValueError("Conversion rate not set.")
        if self.wallets.get(from_currency, 0) < amount:
            raise ValueError("Not enough funds.")
        rate = self.exchange_rates[(from_currency, to_currency)]
        converted = amount * rate
        self.wallets[from_currency] -= amount
        self.wallets[to_currency] = self.wallets.get(to_currency, 0) + converted
        self.transaction_log.append( 
            f"Конвертовано: {amount} {from_currency} → {to_currency} @ {rate} = {converted}"
        )
        self.save_data()
        return converted

    def reset_wallet(self):
        self.wallets = {}
        self.exchange_rates = {}
        self.transaction_log.append("Всі гаманці та курси скинуто") 
        self.save_data()

    def get_transaction_log(self):
        return self.transaction_log

    def save_data(self):
        os.makedirs(os.path.dirname(self.storage_file), exist_ok=True)
        with open(self.storage_file, 'w') as f:
            json.dump({
                'wallets': self.wallets,
                'exchange_rates': {f"{k[0]}_{k[1]}": v for k, v in self.exchange_rates.items()}
            }, f)

    def load_data(self):
        if not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
            self.wallets = data.get('wallets', {})
            self.exchange_rates = {
                tuple(k.split('_')): v for k, v in data.get('exchange_rates', {}).items()
            }
