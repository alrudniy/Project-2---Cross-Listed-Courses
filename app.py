"""
Write a Python Flask application that has separate pages to display all faculty, all committees, faculty participation in committee for all time sorted by academic year, and faculty participation in committee for last 5 academic years sorted by year. App must have a menu. Use this database schema: 
Committee (Designation, Committee Code, Committee Name, Committee Type)
Faculty (Faculty Email, Faculty Name)
Faculty-Committee(Committee Code, Faculty Name, Faculty Start Semester, Membership Type, Designation, Academic Year) 
"""
from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
# pip3 install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Configure the application with a database
# to create a new database run this command in terminal:
# sqlite ./instance/faculty_committees.db

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p2:csci400@34.71.71.82:3306/p2_courses"
db = SQLAlchemy(app)

# Define the models



class Prerequisites(db.Model):
    __tablename__ = "prerequisites"
    subject_code = db.Column(db.VARCHAR(10), primary_key=True, nullable=False)
    course_id = db.Column(db.VARCHAR(10), primary_key=True, nullable=False)



# Define routes
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/prerequisites')
def prerequisites():
    prerequisites_list = Prerequisites.query.order_by(Prerequisites.subject_code).all()
    return render_template('prerequisites.html', prerequisites_list=prerequisites_list)

@app.route('/add_prerequisites', methods={'GET', 'POST'})
def add_prerequisites():
    if request.method =='POST':
        subject_code = request.form['prerequisites_subject_code']
        course_id = request.form['prerequisites_course_id']
        prerequisites = Prerequisites(prerequisites_subject_code=subject_code, prerequisites_course_id=course_id)
        db.session.add(prerequisites)
        db.session.commit()
        return redirect(url_for('prerequisites'))
    return render_template('add_prerequisites.html')





@app.route('/edit_prerequisites/<subject_code>', methods=['GET', 'POST'])
def edit_prerequisites(subject_code):
    prerequisites = Prerequisites.query.get(subject_code)
    if request.method == 'POST':
        prerequisites.course_id = request.form['course_id']
        db.session.commit()
        return redirect(url_for('prerequisites'))
    return render_template('edit_prerequisites.html', prerequisites=prerequisites)

                          
if __name__ == '__main__':
    app.run(debug=True)


