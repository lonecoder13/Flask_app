# app/routes/auth.py
from flask import Blueprint
from flask import render_template
# from . import auth_bp  # Import the auth_bp blueprint

base_bp = Blueprint('/', __name__, template_folder='templates')

@base_bp.route('/')
def base():
    return render_template('base.html')