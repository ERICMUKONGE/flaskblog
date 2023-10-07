from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm , LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '1af6217ac4e6afb3dd2006c6a9a5596d'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sitefrom.db'
db = SQLAlchemy(app)

# db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

posts = [
    {
      'author':'Mukonge Eric',
      'title':'Blog Post 1',
      'content': 'First post content',
      'date_posted':'September 24, 2023' 
    },

    { 
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'September 10, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flaskblog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')   
        return redirect(url_for('home'))
    else:
        flash(f'Login Unsuccessful.Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)
 
if __name__ == "__main__":
    app.run(debug=True) 