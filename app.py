from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'

if __name__==(__name__):
    app.run()