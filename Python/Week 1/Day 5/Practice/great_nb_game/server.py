from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'nb' not in session:
        session['nb'] = random.randint(1, 100)
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['nb']:
            msg = 'Too low!'
            color = 'red'
        elif guess > session['nb']:
            msg = 'Too high!'
            color = 'red'
        else:
            msg = f'Congratulations! you guessed the Number {session["nb"]} in {session["attempts"]} attempts!'
            color = 'green'
            session.pop('nb')  

        return render_template('index.html', msg=msg, color=color)

    return render_template('index.html', msg=None, color=None)

if __name__ == '__main__':
    app.run(debug=True)
