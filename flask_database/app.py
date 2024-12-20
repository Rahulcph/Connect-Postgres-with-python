from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import random
import string


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(100))
    account = db.Column(db.String(50))

    def __repr__(self):
        return f'Password: {self.account}'


#def generate_password(length=12):
   # characters = string.ascii_letters + string.digits + string.punctuation
    #lst = []
    #for i in range(length):
      #  ch = random.choice(characters)
      #  lst.append(ch)
   # random_password = ''.join(lst)
    #return random_password
def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        word = random.choice(characters)
        password = password + word

    return password
@app.route('/', methods=['GET']) 
def index(): 
    return render_template('index.html') 


@app.route('/add', methods=['POST'])
def add_password():
    account = request.form['account']
    # pwd = request.form['pwd']
    length = int(request.form['length'])
    pwd = generate_password(length)
    
    # Create a new Password object and add it to the database
    new_password = Password(account=account, pwd=pwd)
    db.session.add(new_password)
    db.session.commit()

    return redirect(url_for('view'))

@app.route('/view', methods=['GET'])
def view():
    # Retrieve all data from the Password table
    passwords = Password.query.all()
    return render_template('view.html', passwords=passwords)



if __name__ == '__main__':
    app.run(debug=True)

