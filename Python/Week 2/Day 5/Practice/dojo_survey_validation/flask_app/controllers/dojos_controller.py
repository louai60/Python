from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if Dojo.is_valid(request.form):
        id = Dojo.save(request.form)
        return redirect(f'/result/{id}')
    return redirect('/')

@app.route('/result/<int:id>')
def show(id):
    dojo = Dojo.get_by_id(id)
    return render_template('result.html', dojo=dojo)
