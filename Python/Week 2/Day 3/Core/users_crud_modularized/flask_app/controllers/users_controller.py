from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User  
from flask_app import DATABASE

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


@app.route('/show/<int:user_id>')
def show(user_id):
    user = User.get_by_id(user_id)
    return render_template('show.html', user=user)
    
# @app.route('/update/<int:user_id>', methods=['POST'])
# def update_user(user_id):
#     # Retrieve updated user information from the request form
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     email = request.form['email']
    
#     # Update the user with the retrieved information
#     User.update(user_id, first_name, last_name, email)
    
#     return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        User.update(user_id, first_name, last_name, email)

        return redirect('/')
    else:
        user = User.get_by_id(user_id)
        return render_template('update.html', user=user)

        
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/')
