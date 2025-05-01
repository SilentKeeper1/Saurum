from flask import Flask, request, render_template, redirect, url_for
from wallet_manager import WalletManager

app = Flask(__name__)
manager = WalletManager()

@app.route('/')
def index():
    return render_template('index.html', wallets=manager.get_wallet(), tarnsaction_log=manager.get_transaction_log())

@app.route('/create_wallet')
def create_wallet():
    return render_template('index3.html')

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