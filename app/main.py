from flask import Flask, request, render_template, redirect, url_for
from wallet_manager import WalletManager

app = Flask(__name__)
manager = WalletManager()

@app.route('/')
def index():
    return render_template('index.html', 
                         wallets=manager.get_wallet(),
                         transaction_log=manager.get_transaction_log())

@app.route('/create_wallet', methods=['GET', 'POST'])
def create_wallet():
    if request.method == 'POST':
        currency = request.form['currency'].upper()
        balance = float(request.form['balance'])
        try:
            manager.create_wallet(currency, balance)
            return redirect(url_for('index'))
        except ValueError as e:
            return str(e), 400
    return render_template('index2.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount'])
            converted = manager.convert(from_currency, to_currency, amount)
            return render_template('index3.html',
                                 wallets=manager.get_wallet(),
                                 success=f"Успішно конвертовано {amount} {from_currency} → {converted:.2f} {to_currency}")
        except ValueError as e:
            return render_template('index3.html',
                                 wallets=manager.get_wallet(),
                                 error=str(e))
    return render_template('index3.html', wallets=manager.get_wallet())

@app.route('/set_rate', methods=['GET', 'POST'])
def set_rate():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        rate = float(request.form['rate'])
        manager.add_exchange_rate(from_currency, to_currency, rate)
        return redirect(url_for('index'))
    return render_template('index4.html', wallets=manager.get_wallet())

@app.route('/reset')
def reset_wallets():
    manager.reset_wallet()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)