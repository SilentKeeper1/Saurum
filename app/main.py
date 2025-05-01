from flask import Flask, request, render_template, redirect, url_for
from wallet_manager import WalletManager

app = Flask(__name__)
manager = WalletManager()

@app.route('/')
def index():
    return render_template('index.html', wallets=manager.get_wallet(), transaction_log=manager.get_transaction_log())

# Добавляем поддержку POST для создания кошелька
@app.route('/create_wallet', methods=['GET', 'POST'])  # <- Вот это важно!
def create_wallet():
    if request.method == 'POST':
        currency = request.form['currency'].upper()
        balance = float(request.form['balance'])
        try:
            manager.create_wallet(currency, balance)
            return redirect(url_for('index'))  # Перенаправляем на главную
        except ValueError as e:
            return str(e), 400  # Показываем ошибку, если валюта уже существует
    return render_template('index3.html')  # GET: показываем форму

# Остальные роуты (оставляем как есть)
@app.route('/convert')
def convert():
    return render_template('index2.html')

@app.route('/set_rate')
def set_rate():
    return render_template('index3.html')

@app.route('/reset')
def reset_wallets():
    return render_template('index4.html')

if __name__ == '__main__':
    app.run(debug=True)