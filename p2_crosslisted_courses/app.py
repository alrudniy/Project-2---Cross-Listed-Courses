"""
Write a Python Flask application that has separate pages to display all faculty, all committees, faculty participation in committee for all time sorted by academic year, and faculty participation in committee for last 5 academic years sorted by year. App must have a menu. Use this database schema: 
Committee (Designation, Committee Code, Committee Name, Committee Type)
Faculty (Faculty Email, Faculty Name)
Faculty-Committee(Committee Code, Faculty Name, Faculty Start Semester, Membership Type, Designation, Academic Year) 
"""
from flask import Flask, render_template, request, redirect, url_for
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


class Course_Attributes(db.Model):
    __tablename__ = "course_attributes"
    attribute_code = db.Column(db.String(255), primary_key=True)
    attribute = db.Column(db.String(255))
    attribute_description = db.Column(db.String(255))
    

# Define routes
@app.route('/course-attributes')
def course_attributes():
    course_attributes_list = Course_Attributes.query.order_by(Course_Attributes.attribute_code).all()
    return render_template('course_attributes.html', course_attributes_list=course_attributes_list)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faculty')
def faculty():
    faculty_list = Faculty.query.all()
    return render_template('faculty.html', faculty_list=faculty_list)
    #return render_template('faculty.html')

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

@app.route('/add_course_attributes', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        email = request.form['course_attributes_email']
        name = request.form['course_attributes_name']
        course_attributes = Course_Attributes(course_attributes_email=email, course_attributes_name=name)
        db.session.add(course_attributes)
        db.session.commit()
        return redirect(url_for('course_attributes_list'))
    return render_template('add_course_attributes.html')


@app.route('/edit_course_attributes/<attribute_code>', methods=['GET', 'POST'])
def edit_course_attributes(attribute_code):
    course_attributes = Course_Attributes.query.get(attribute_code)
    if request.method == 'POST':
        course_attributes.course_attributes_name = request.form['course_attributes_name']
        db.session.commit()
        return redirect(url_for('course_attributes_list'))
    return render_template('edit_course_attributes.html', course_attributes=course_attributes)

if __name__ == '__main__':
    app.run(debug=True)