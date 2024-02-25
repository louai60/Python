from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', x=3, color='hsl(180deg 99.21% 50.2%)')

@app.route('/play/<int:x>')
def x(x):
    return render_template('index.html', x=x, color='hsl(180deg 99.21% 50.2%)')

@app.route('/play/<int:x>/<color>')
def x_color(x, color):
    return render_template('index.html', x=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
