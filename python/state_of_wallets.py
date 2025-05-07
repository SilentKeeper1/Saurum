class Wallet:
    def __init__(self, currency, initial_balance):
        self.currency = currency
        self.balance = initial_balance

    def display_info(self):
        return f"Currency: {self.currency}, Balance: {self.balance}"

class UserWallets:
    def __init__(self):
        self.wallets = []

    def add_wallet(self, wallet):
        self.wallets.append(wallet)

    def display_all_wallets(self):
        print("Current state of all wallets:")
        for index, wallet in enumerate(self.wallets, start=1):
            print(f"{index}. {wallet.display_info()}")

wallet1 = Wallet("USD", 1000)
wallet2 = Wallet("EUR", 500)
wallet3 = Wallet("UAH", 20000)

user_wallets = UserWallets()
user_wallets.add_wallet(wallet1)
user_wallets.add_wallet(wallet2)
user_wallets.add_wallet(wallet3)

user_wallets.display_all_wallets()