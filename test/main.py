from flask import Flask, request, render_template, redirect, url_for
from wallet_manager import WalletManager

app = Flask(__name__)
manager = WalletManager()

@app.route('/')
def index():
    return render_template('index.html', wallets=manager.get_wallet())

@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    currency = request.form['currency']
    balance = float(request.form['balance'])
    try:
        manager.create_wallet(currency, balance)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for('index'))

@app.route('/convert', methods=['POST'])
def convert():
    from_cur = request.form['from_currency']
    to_cur = request.form['to_currency']
    amount = float(request.form['amount'])
    try:
        manager.convert(from_cur, to_cur, amount)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for('index'))

@app.route('/set_rate', methods=['POST'])
def set_rate():
    from_cur = request.form['from_currency']
    to_cur = request.form['to_currency']
    rate = float(request.form['rate'])
    manager.add_exchange_rate(from_cur, to_cur, rate)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)