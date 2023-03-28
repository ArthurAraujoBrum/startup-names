from flask import Flask
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ncbxzmncb_jlfkji@9823786'

from .views import views

app.register_blueprint(views, url_prefix='/')