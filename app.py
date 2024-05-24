from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/students'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://anand:DvvroAEqylm5uRQ3IsEuqRrE0O3g7qzt@dpg-cp8desn109ks738jk69g-a.oregon-postgres.render.com/student_svnw'

db=SQLAlchemy(app)

class loginData(db.Model):
  __tablename__='loginData'
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(40))
  password=db.Column(db.String(10))

  def __init__(self,username,password):
    self.username=username
    self.password=password

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  pet=db.Column(db.String(40))

  def __init__(self,fname,lname,pet):
    self.fname=fname
    self.lname=lname
    self.pet=pet


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/checkLogin', methods=['POST'])
def checkLogin():
  username=request.form['username']
  password=request.form['password']

  if username=='admin' and password=='admin':
    return render_template('loginStatus.html', status= "success", username=username)
  else:
    return render_template('loginStatus.html', status= "failure", username=username)

@app.route('/submit', methods=['POST'])
def submit():
  fname= request.form['fname']
  lname=request.form['lname']
  pet=request.form['pets']

  student=Student(fname,lname,pet)
  db.session.add(student)
  db.session.commit()

  #fetch a certain student2
  studentResult=db.session.query(Student).filter(Student.id==1)
  for result in studentResult:
    print(result.fname)

  return render_template('success.html', data=fname)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)





