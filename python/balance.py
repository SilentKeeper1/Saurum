#4)Напишіть логіку для розрахунку загального балансу на основі введених транзакцій, 
# враховуючи прибутки та витрати.

def calulate_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction['transaction_type'] =='income': #прибуток
            balance += transaction['amount']
        elif transaction['transaction_type'] == 'expense': #витрати
            balance -= transaction['amount']
    return balance

#приклад введення транзакцій
transactions = [
    {'transaction_type': 'income', 'amount': 500},
    {'transaction_type': 'expense', 'amount': 200},
    {'transaction_type': 'income', 'amount': 300},
    {'transaction_type': 'expense', 'amount': 150},
]

#розрахунок
total_balance = calulate_balance(transactions)
print(f"Загальний баланс: {total_balance}")