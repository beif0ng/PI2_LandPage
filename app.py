from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


#criar a instancia do flask
app = Flask(__name__)
#Add banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgreslq://qwqicrfnwhwfxi:fa66c2f3100a0b06cdd535179c790d3df2ef42289d242cd830df4553361efa48@ec2-23-23-151-191.compute-1.amazonaws.com:5432/deahjjdvc9afis'
# Secret key
app.config['SECRET_KEY'] = "pi univesp"
#iniciar o bd
db = SQLAlchemy(app)

#Create model
class Emails(db.Model):
    email = db.Column(db.String(), primary_key=True, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Criar uma Classe de formulario
class Emailform(FlaskForm):
    email = StringField('Deixe Seu Melhor e-mail', validators=[DataRequired()])
    submit = SubmitField('Enviar')

#criar a rota
@app.route('/', methods=['GET', 'POST'])
def index():
    email = None
    form = Emailform()
    # Valitions
    if form.validate_on_submit():
        email = Emails.query.filter_by(email=form.email.data).first()
        if email is None:
            email = Emails(email=form.email.data)
            db.session.add(email)
            db.session.commit()
        form.email.data = ''
    
    return render_template("index.html", email = email, form = form)
