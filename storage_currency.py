#перший варіант
# Стркутра для одного користуача з кількома гаманецьами

wallets = {
    "user1": [
        {"currency": "USD", "balance": 150.75},
        {"currency": "EUR", "balance": 90.50},
    ],
    "user2": [
        {"currency": "UAH", "balance": 1200},
        {"currency": "BTC", "balance": 0.005},
    ],
}


for wallet in wallets["user1"]:
    print(f"Валюта: {wallet['currency']}, Баланс: {wallet['balance']}")

#другий варіант
# Через класи для КОРИСТУВАЧІВ
class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance


user_wallets = {
    "user1": [Wallet("USD", 150.75), Wallet("EUR", 90.50)],
    "user2": [Wallet("UAH", 1200), Wallet("BTC", 0.005)],
}