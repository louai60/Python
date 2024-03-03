from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email


# @app.route('/result')
# def read_all():
#     all_emails = Email.get_all()
#     return render_template('result.html', all_emails = all_emails)

# @app.route('/', methods = ['POST'])
# def save():
#     if email.validate_user(request.form):
#         email = Email.save(request.form)
#         return redirect('/result')
#     return redirect('/create')

# @app.route('/create')
# def new():
#     return render_template('email.html')

@app.route('/')
def email():
    return render_template("email.html")


@app.route('/',methods=['POST'])
def save():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/results')


@app.route('/results')
def results():
    all_emails = Email.get_all()
    return render_template("result.html", all_emails=all_emails)
