import os

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

basedir = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'contacts.db'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Contacts(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer(), primary_key=True)
    company = db.Column(db.String(50))
    email = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(50))
    name = db.Column(db.String(50))
    country = db.Column(db.String(50))
    job_history = db.Column(db.String(150))

    def __repr__(self):
        return "<Name: {}>".format(self.name)


@app.route('/', methods=['GET', 'POST'])
def index():
    contacts = Contacts.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/search', methods=['POST'])
def search():
    name = request.form.get("name")

    if not name:
        contacts = Contacts.query.all()
    else:
        contacts = Contacts.query.filter(Contacts.name.contains(name)).all()

    return render_template('index.html', contacts=contacts)


if __name__ == '__main__':
    app.run()
