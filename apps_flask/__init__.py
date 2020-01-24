"""
apps_flask/apps_flask/__init__.py
AUTOR: CARR
FECHA DE CREACIÓN: 21/01/2020
"""

import logging
from logging.handlers import SMTPHandler

from flask import Flask, render_template

#import apps_flask

"""
export FLASK_APP="entrypoint"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.local"
"""

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    # Para ver las variables que cargo
    #print("variables de ambiente " + str(app.config))

    # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        # El archivo config.py esta en el directorio instance, el cual flask no permite
        # que se suba a Git por que ahí esta la conexión a la base de datos, usuario y password.
        # Otra alternativa es poner esta conexión como una variable de ambiente y no ponerla en archivo.
        # Todo esto es por proteccion.
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile('config_testing.py', silent=True)


