import logging
from flask import Flask, render_template


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
