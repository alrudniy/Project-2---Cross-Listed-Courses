"""
Write a Python Flask application that has separate pages to display all faculty, all committees, faculty participation in committee for all time sorted by academic year, and faculty participation in committee for last 5 academic years sorted by year. App must have a menu. Use this database schema: 
Committee (Designation, Committee Code, Committee Name, Committee Type)
Faculty (Faculty Email, Faculty Name)
Faculty-Committee(Committee Code, Faculty Name, Faculty Start Semester, Membership Type, Designation, Academic Year) 
"""
from flask import Flask, render_template
from flask import request, redirect, url_for
# pip3 install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

app = Flask(__name__)

# Configure the application with a database
# to create a new database run this command in terminal:
# sqlite ./instance/faculty_committees.db

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p2:csci400@34.71.71.82:3306/p2_courses"
db = SQLAlchemy(app)

# Define the models
class CourseAttributes(db.Model):
    attribute_code = db.Column(db.String(255), primary_key=True)
    attribute = db.Column(db.String(255))
    attribute_description = db.Column(db.String(255))

class Courses (db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    subject_code = db.Column(db.String(10))
    course_number = db.Column(db.String(10))
    college = db.Column(db.String(5))
    department_code = db.Column(db.Integer)
    division_code = db.Column(db.Integer)
    short_title = db.Column(db.String(100))
    long_title = db.Column(db.String(255))
    last_term_offered = db.Column(db.Integer, nullable=False)

class Departments (db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(255))

class Divisions (db.Model):
    division_id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String(20))

class Faculty (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_email = db.Column(db.String(255))
    faculty_name = db.Column(db.String(255))

class Prerequisites (db.Model):
    subject_code = db.Column(db.String(10), primary_key=True)
    course_id = db.Column(db.String(10), primary_key=True)


# Define routes

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
     if request.method == 'POST':
        id = request.form['course_id']
        subject_code = request.form['subject_code']
        number = request.form['course_number']
        college = request.form['college']
        longtitle = request.form['long_title']
        shorttitle = request.form['short_title']
        last_term = request.form['last_term_offered']
        Courses = Courses(course_id=id, subject_code=subject_code, course_number=number, college=college, long_title=longtitle, short_title=shorttitle, last_term_offered=last_term)
        db.session.add(Courses)
        db.session.commit()
        return redirect(url_for('course_list'))
     return render_template('add_course.html')

@app.route('/edit_course/<course_id>', methods=['GET', 'POST'])
def edit_faculty(course_id):
    course = Courses.query.get(course_id)
    if request.method == 'POST':
        course.short_title = request.form['short_title']
        db.session.commit()
        return redirect(url_for('course_list'))
    return render_template('edit_course.html', course=course)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/course_attributes')
def course_attributes():
    course_attributes_list = CourseAttributes.query.order_by(CourseAttributes.attribute_code).all()
    return render_template('course_attributes.html', course_attributes_list=course_attributes_list)

@app.route('/courses')
def courses():
    courses_list = Courses.query.order_by(Courses.course_id).all()
    return render_template('courses.html', courses_list=courses_list)

@app.route('/departments')
def departments():
    departments_list = Departments.query.order_by(Departments.department_id).all()
    return render_template('departments.html', departments_list=departments_list)

@app.route('/divisions')
def divisions():
    divisions_list = Divisions.query.order_by(Divisions.division_id).all()
    return render_template('divisions.html', divisions_list=divisions_list)

@app.route('/faculty')
def faculty():
    faculty_list = Faculty.query.order_by(Faculty.id).all()
    return render_template('faculty.html', faculty_list=faculty_list)

@app.route('/prerequisites')
def prerequisites():
    prerequisites_list = Prerequisites.query.order_by(Prerequisites.subject_code).all()
    return render_template('prerequisites.html', prerequisites_list=prerequisites_list)


if __name__ == '__main__':
    app.run(debug=True)