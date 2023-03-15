"""
Write a Python Flask application that has separate pages to display all faculty, all committees, faculty participation in committee for all time sorted by academic year, and faculty participation in committee for last 5 academic years sorted by year. App must have a menu. Use this database schema: 
Committee (Designation, Committee Code, Committee Name, Committee Type)
Faculty (Faculty Email, Faculty Name)
Faculty-Committee(Committee Code, Faculty Name, Faculty Start Semester, Membership Type, Designation, Academic Year) 
"""
from flask import Flask, render_template
# pip3 install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

app = Flask(__name__)

# Configure the application with a database
# to create a new database run this command in terminal:
# sqlite ./instance/faculty_committees.db

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql:///liz:csci400@34.71.71.82/p2_courses"
db = SQLAlchemy(app)

# Define the models
class Course_Attributes(db.Model):
    attribute_code = db.Column(db.String(255), primary_key=True)
    attribute = db.Column(db.String(255))
    attribute_description = db.Column(db.String(255))

class Courses (db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    subject_code = db.Column(db.String(10))
    course_number = db.Column(db.String(10))
    college = db.Column(db.String(5))
    deparment_code = db.Column(db.Integer)
    division_code = db.Column(db.Integer)
    short_title = db.Column(db.String(100))
    long_title = db.Column(db.String(255))
    last_term_offered = db.Column(db.Integer, nullable=False)

class Departments (db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(255))


# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/departments')
def departments():
    department_list = Departments.query.all()
    return render_template('departments.html', department_list=department_list)

@app.route('/committees')
def committees():
    committee_list = Committee.query.all()
    return render_template('committees.html', committee_list=committee_list)

@app.route('/faculty-committee-all')
def faculty_committee_all():
    faculty_committee_list = Faculty_Committee.query.order_by(Faculty_Committee.academic_year).all()
    return render_template('faculty_committee_all.html', faculty_committee_list=faculty_committee_list)

@app.route('/faculty-committee-last-five')
def faculty_committee_last_five():
    faculty_committee_list = Faculty_Committee.query.order_by(Faculty_Committee.academic_year.desc()).limit(5).all()
    return render_template('faculty_committee_last_five.html', faculty_committee_list=faculty_committee_list)

if __name__ == '__main__':
    app.run(debug=True)