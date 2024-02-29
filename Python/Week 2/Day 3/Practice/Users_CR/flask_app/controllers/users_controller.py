from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def read_all():
    all_users = User.get_all()
    return render_template('read_all.html', all_users=all_users)

# #* View Route
# @app.route("/create")
# def display_form():

#     return render_template("create.html")

@app.route('/create', methods=['POST'])
def create():
    User.save(request.form)

    return redirect('/')




@app.route('/new')
def new():

    return render_template('create.html')




