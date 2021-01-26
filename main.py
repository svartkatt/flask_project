from flask import Flask
import requests

app = Flask(__name__)


@app.route('/eur_to_usd/<int:amount>/')
def euro_to_usd(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json['rates']
    result = str(rates.get('USD') * amount)
    with open('history.py', 'a') as text:
        text.write('"USD", ' + str(rates.get('USD')) + ', ' + str(amount) + ', ' + result + '\n')
    return result


@app.route('/eur_to_gbp/<int:amount>/')
def euro_to_gbp(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json['rates']
    result = str(rates.get('GBP') * amount)
    with open('history.py', 'a') as text:
        text.write('"GBP", ' + str(rates.get('GBP')) + ', ' + str(amount) + ', ' + result + '\n')
    return result


@app.route('/eur_to_php/<int:amount>/')
def euro_to_php(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json['rates']
    result = str(rates.get('PHP') * amount)
    with open('history.py', 'a') as text:
        text.write('"PHP", ' + str(rates.get('PHP')) + ', ' + str(amount) + ', ' + result + '\n')
    return result


@app.route('/history/')
def get_history():
    pass


if __name__ == '__main__':
    open('history.py', 'a')
    app.run()
