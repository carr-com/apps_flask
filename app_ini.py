"""
apps_flask/app_ini.py
AUTOR: CARR
FECHA DE CREACIÓN: 21/01/2020
"""

import os

#Esta función se encuentra en
# apps_flask/apps_flask/__init__.py
from apps_flask import create_app

"""
# Exportar las variables de ambiente, estan en el archivo ./vars_app.sh
 
export FLASK_APP="app_ini"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.local" 
export SECRET_KEY="xxxxxxx......" ; Se genera ver el archivo default.py
export MAIL_PASSWORD="xxx..." o puede ser uan variable de ambiente

La recomendación para las pruebas es que añadas esas variables en el fichero 
"activate" o "activate.bat" si estás usando virtualenv
Si usas Pycharm poner las variables de ambiente en 
Run>>Edit Configutations>>Environments variables
"""

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


