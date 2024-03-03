# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "Your_Secret_Key"


DATABASE = 'email_schema'