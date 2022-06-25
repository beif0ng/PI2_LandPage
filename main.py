from flask import Flask, render_template
#from datetime import datetime
#criar a instancia do flask
app = Flask(__name__)
#Add banco de dados
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Scret key
#app.config['SECRET_KEY'] = "pi univesp"
#iniciar o bd
#db = SQLAlchemy(app)

#Create model
#class Emails(db.model):
 #   email = db.Column(db.String(200), primary_key=True, unique=True)
#    date_added = db.Column(db.DateTime, default=datetime.utcnow)
#
    #Create A String How to Use Databases With SQLAlchemy - Flask Fridays #8 00:09:00
#criar a rota
@app.route('/')
def index():
    return render_template("index.html")