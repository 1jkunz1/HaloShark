
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def record():
    return render_template('record.html')

@app.route('/picks')
def picks():
    return render_template('picks.html')


@app.route('/picks')
def picks():
    return render_template('scraper.html')


@app.route('/picks')
def picks():
    return render_template('forum.html')
