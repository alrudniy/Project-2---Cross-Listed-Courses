from flask import Flask, render_template, request, redirect, url_for
# pip3 install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p3:Mtmqn584@34.136.218.122:3306/p3_courses"
db = SQLAlchemy(app)

# Define the models
class Departments (db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(255))

# Table routes

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


# Define routes

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
     if request.method == 'POST':
        course_id = request.form['course_id']
        subject_code = request.form['subject_code']
        number = request.form['course_number']
        college = request.form['college']
        long_title = request.form['long_title']
        short_title = request.form['short_title']
        last_term = request.form['last_term_offered']
        New_Courses = Courses(course_id=course_id, subject_code=subject_code, course_number=number, college=college, long_title=long_title, short_title=short_title, last_term_offered=last_term)
        db.session.add(New_Courses)
        db.session.commit()
        return redirect(url_for('courses'))
     return render_template('add_course.html')

@app.route('/edit_course/<course_id>', methods=['GET', 'POST'])
def edit_faculty(course_id):
    course = Courses.query.get(course_id)
    if request.method == 'POST':
        course.subject_code = request.form['subject_code']
        course.course_number = request.form['course_number']
        course.college = request.form['college']
        course.long_title = request.form['long_title']
        course.short_title = request.form['short_title']
        course.last_term_offered = request.form['last_term_offered']
        db.session.commit()
        return redirect(url_for('courses'))
    return render_template('edit_course.html', course=course)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/departments')
def departments():
    departments_list = Departments.query.order_by(Departments.department_id).all()
    return render_template('TABLES/departments.html', departments_list=departments_list)

# Add to table routes
@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        id = request.form['department_id']
        name = request.form['department_name']
        department = Departments(department_id=id, department_name=name)
        db.session.add(department)
        db.session.commit()
        return redirect(url_for('departments'))
    return render_template('ADD/add_department.html')

# Edit table routes
@app.route('/edit_departments/<department_id>', methods=['GET', 'POST'])
def edit_departments(department_id):
    department = Departments.query.get(department_id)
    if request.method == 'POST':
        department.department_name = request.form['department_name']
        db.session.commit()
        return redirect(url_for('departments'))
    return render_template('EDIT/edit_departments.html', department=department)

@app.route('/courses')
def courses():
    courses_list = Courses.query.order_by(Courses.course_id).all()
    return render_template('courses.html', courses_list=courses_list)

if __name__ == '__main__':
    app.run(debug=True)