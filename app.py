import os

from flask import Flask
from flask import render_template

basedir = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'contacts.db'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
