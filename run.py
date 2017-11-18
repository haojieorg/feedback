from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.secret_key = 'haojieorg'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/post/')
def feedback_post():
    return render_template('feedback_post.html')

if __name__ == '__main__':
    app.run()
