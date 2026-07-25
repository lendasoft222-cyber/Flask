from flask import Flask
app = Flask(__name__)


from app.routes import home
from app.routes import contacto