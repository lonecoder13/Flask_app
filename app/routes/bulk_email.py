# app/routes/bulk_email.py

from flask import render_template
# from . import bulk_email_bp  # Import the bulk_email_bp blueprint

# Edited -----------------
from flask import Blueprint
bulk_email_bp = Blueprint('bulk_email', __name__, template_folder='templates/bulk_emails')
# ---------------------

@bulk_email_bp.route('/home')
def home():
    return render_template('bulk_emails/home.html')

@bulk_email_bp.route('/upload')
def upload():
    return render_template('bulk_emails/upload.html')

@bulk_email_bp.route('/result')
def result():
    return render_template('bulk_emails/result.html')

