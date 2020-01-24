"""
AUTOR: CARR
FECHA DE CREACIÓN: 22/01/2020
"""

from os.path import abspath, dirname, join
import os

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

"""
Se genera en la consola de python con
import secrets
secrets.token_urlsafe(64)
La salida se copia y se pone en 
la variable de ambiente SECRET_KEY
"""
SECRET_KEY = os.getenv('SECRET_KEY')

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'comercialccsys@gmail.com'
""" 
EL MAIL_PASSWORD se pone en una variable de ambiente 
"""
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
DONT_REPLY_FROM_EMAIL = 'comercialccsys@gmail.com'
ADMINS = ('comercialccsys@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 3
