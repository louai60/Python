from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo  
from flask_app import DATABASE


# @app.route('/')
# def index():
#     return redirect('/dojo')

@app.route('/dojo')
def dojos():
    return render_template('add_dojo.html',all_dojos=Dojo.get_all())

@app.route('/add/dojo', methods=['POST'])
def add_dojo():
    data = {
        "name": request.form['name']
    }
    dojo_id = Dojo.save(data)
    
    all_dojos = Dojo.get_all()
    
    return render_template('add_dojo.html', all_dojos=all_dojos, form_data=data)


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('add_dojo.html',dojo=Dojo.get_by_id(data))

