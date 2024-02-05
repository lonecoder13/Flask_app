
from flask import Flask

def create_app():
    print("execute hua")
    app = Flask(__name__)
    

    # Import blueprints
    from app.routes import base_bp, auth_bp, bulk_email_bp


    # Register blueprints
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(bulk_email_bp)


    #Edited ------------
    app.register_blueprint(base_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(bulk_email_bp, url_prefix='/bulk-email')
    #--------------------

    return app
