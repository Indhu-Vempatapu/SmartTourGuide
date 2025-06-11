from flask import Flask, render_template, request, redirect, url_for
from rules_engine import TouristExpertSystem

app = Flask(__name__)
engine = TouristExpertSystem()
user_input = {}

@app.route('/')
def home():
    return redirect(url_for('start'))

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        global user_input
        user_input = {k: v for k, v in request.form.items() if v == 'y'}
        return redirect(url_for('results'))
    return render_template('form.html')

@app.route('/results')
def results():
    recs = engine.run_engine(user_input)
    return render_template('results.html', recommendations=recs)

if __name__ == '__main__':
    app.run(debug=True)
