from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['locat'] = request.form['locat']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name=session['name'], locat=session['locat'], lang=session['lang'], comment=session['comment'])

if __name__ == '__main__':
    app.run(debug=True)
