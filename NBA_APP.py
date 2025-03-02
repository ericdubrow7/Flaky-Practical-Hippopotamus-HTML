from flask import Flask, render_template
from flask import Flask, jsonify
import json
from datetime import datetime
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playerstats', endpoint='playerstats')
def playerstats():
    return render_template('playerstats.html')

@app.route('/latest-nba-news', endpoint='latest-nba-news')
def latestnbanews():
    return render_template('latest-nba-news.html')

if __name__ == '__main__':
    app.run(debug=True)