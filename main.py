from flask import Flask
import requests
import sqlite3

app = Flask(__name__)
with sqlite3.connect('server.db') as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS exchange (
    currency_to TEXT, 
    exchange_rate BIGINT, 
    amount BIGINT, 
    result BIGINT
)""")

db.commit()


def get_rates():
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json['rates']
    return rates


def writing_to_db(currency, amount, result):
    cursor.execute("SELECT * FROM exchange")
    cursor.execute("INSERT INTO exchange VALUES (?, ?, ?)", (currency, get_rates().get(currency), amount, result))
    db.commit()


@app.route('/eur_to_usd/<int:amount>/')
def euro_to_usd(amount):
    currency = 'USD'
    result = str(get_rates().get(currency) * amount)
    writing_to_db(currency, amount, result)
    return result


@app.route('/eur_to_gbp/<int:amount>/')
def euro_to_gbp(amount):
    currency = 'EUR'
    result = str(get_rates().get(currency) * amount)
  #  writing_to_db(currency, amount, result)
    return result


@app.route('/eur_to_php/<int:amount>/')
def euro_to_php(amount):
    currency = 'PHP'
    result = str(get_rates().get(currency) * amount)
    writing_to_db(currency, amount, result)
    return result


@app.route('/history/')
def get_history():
    with open('history.py') as text:
        return text.read()


if __name__ == '__main__':
    open('history.py', 'a')
    app.run()
