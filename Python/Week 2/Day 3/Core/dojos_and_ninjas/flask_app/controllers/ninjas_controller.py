from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja  
from flask_app import DATABASE

@app.route('/')
def read_all_ninjas():
    all_ninjas = Ninja.get_all()
    return render_template('read_all.html', all_ninjas=all_ninjas)

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/ninja/new')
def new():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html', dojos=dojos)
