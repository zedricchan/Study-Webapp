from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/wotd')
def wotd():
    return render_template('wotd.html')

app.run()
