import os

class Config(object):
    #To make sure nothing is altered for security reasons
    SECRET_KEY = os.environ.get('SECRET_KEY') or "ghterikhsevr12034bbedje934"