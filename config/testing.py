"""
AUTOR: CARR
FECHA DE CREACIÓN: 22/01/2020
"""

from .default import *


# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

print ("APP_ENV_TESTING-..." + APP_ENV_TESTING)

APP_ENV = APP_ENV_TESTING

WTF_CSRF_ENABLED = False
