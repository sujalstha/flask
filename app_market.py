from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


'''@app.route('/')
def hello_world():
    return '<h1>Hello, Welcome to the Flask Market.<h1>'''''


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {},
        {},
    ]
    return render_template('market.html', item_name='Phone')


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About Page of [ {username} ] <h1>'