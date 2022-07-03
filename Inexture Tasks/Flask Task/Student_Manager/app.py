import email
import re
from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Add Database 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/studentmanager"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'the random string'    

# initialize the database 
db = SQLAlchemy(app)

# creating the models

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    # created_at = db.Column(db.Datetime(timezone=True),
    #                         server_default=func.now())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'Student {self.firstname}'

# creating a index route
'''
display records of all the student
'''
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html',students=students)

# creating a route to retrieve a student by ID
'''
this route renders a page for each individual student
'''
@app.route('/<int:student_id>/')
def student(student_id):
    #student = Student.query.get_or_404(student_id)
    student = Student.query.filter_by(id=student_id).all()
    return render_template('student.html', students=student)

# creating a new student into the db
@app.route('/create/',methods=('GET','POST'))
def create():
    if request.method=='POST':
        firstname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname,
                        lastname=lname,
                        email=email,
                        age=age,
                        bio=bio)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get(student_id)
    if request.method=='POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio
       
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html',student=student)


@app.route('/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index')) 

@app.route('/about/')
def about():
    return render_template('about.html')

# special method
if __name__=='__main__':
    app.run(debug=True)
