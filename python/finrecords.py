financial_records = [
    {"type": "income", "amount": 5000},
    {"type": "expense", "amount": 1200},
    {"type": "expense", "amount": 800},
    {"type": "income", "amount": 2000},
    {"type": "expense", "amount": 600},
]

total_income = 0
total_expense = 0


for record in financial_records:
    if record['type'] == 'income':
        total_income += record['amount']
    elif record['type'] == 'expense':
        total_expense += record['amount']


net_profit = total_income - total_expense

print("Загальний прибуток:", total_income)
print("Загальні витрати:", total_expense)
print("Чистий прибуток:", net_profit)


budget_limit = 2000
i = 0
current_expense = 0

while i < len(financial_records) and current_expense <= budget_limit:
    record = financial_records[i]
    if record["type"] == "expense":
        current_expense += record["amount"]
        if current_expense > budget_limit:
            print("Бюджет перевищено після запису №", i + 1)
            break

    i += 1

if current_expense <= budget_limit:
    print("Бюджет не перевищено. Всі витрати в межах бюджету.", current_expense)