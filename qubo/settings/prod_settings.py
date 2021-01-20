from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['qubo.pythonanywhere.com', 'www.qubocultura.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qubo$default',
        'USER': 'qubo',
        'PASSWORD': 'amantedelacomida',
        'HOST': 'qubo.mysql.pythonanywhere-services.com',
    }
}
