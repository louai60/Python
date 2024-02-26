from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1

    return render_template('index.html', visits=session['visits'])

@app.route('/click', methods=['POST'])
def click():
    # increment visit count
    session['visits'] += 1
    # redirect to the route 
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    # reset visit count
    session['visits'] = 0
    # redirect to the route 
    return redirect('/')

@app.route('/clear_session')
def destroy_session():
    # clear the session
    session.clear()
    # redirect to the route 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
