
from flask import Blueprint

# auth_bp = Blueprint('auth', __name__, template_folder='templates/auth', url_prefix='/auth')
# bulk_email_bp = Blueprint('bulk_email', __name__, template_folder='templates/bulk_email', url_prefix='/bulk-email')

base_bp = Blueprint('/', __name__, template_folder='templates')
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')
bulk_email_bp = Blueprint('bulk_email', __name__, template_folder='templates/bulk_emails')

from .base import base
from .auth import login
from .bulk_email import home, upload, result

# from flask import render_template


# Register the routes with the blueprints
base_bp.add_url_rule('/', view_func=base)
auth_bp.add_url_rule('/login', view_func=login)
bulk_email_bp.add_url_rule('/home', view_func=home)
bulk_email_bp.add_url_rule('/upload', view_func=upload, methods=['GET', 'POST'])
bulk_email_bp.add_url_rule('/result', view_func=result)

