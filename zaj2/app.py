from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Witaj w mojej aplikacji Flask!'


@app.route('/about')
def about():
    return 'Zaprogramowano przez Adrian'


@app.route('/contact')
def contact():
    return 'Email: test@test.com'


if __name__ == '__main__':
    app.run(debug=False)
