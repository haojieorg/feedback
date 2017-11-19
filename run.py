from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from feedback import admin


app = Flask(__name__)
app.debug = True
app.secret_key = 'haojieorg'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


app.register_blueprint(admin,url_prefix='/admin')

if __name__ == '__main__':
    app.run()
