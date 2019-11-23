import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '&E)H@McQfTjWnZr4u7x!A%C*F-JaNdRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t6w9'
