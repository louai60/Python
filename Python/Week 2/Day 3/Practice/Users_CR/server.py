from flask import Flask,render_template,redirect,request
from user import User

app = Flask(__name__)



@app.route('/')
def read_all():
    all_users = User.get_all()
    return render_template('read_all.html', all_users=all_users)



@app.route('/create', methods=['POST'])
def create():
    User.save(request.form)

    return redirect('/')




@app.route('/new')
def new():

    return render_template('create.html')




if __name__ == '__main__':
    app.run(debug=True)