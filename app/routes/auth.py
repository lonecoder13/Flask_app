# app/routes/auth.py
from flask import Blueprint
from flask import render_template
# from . import auth_bp  # Import the auth_bp blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')
