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

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://p2:csci400@34.71.71.82:3306/p2_courses"
db = SQLAlchemy(app)

# Define the models


class Divisions(db.Model):
    __tablename__ = "divisions"
    division = db.Column(db.String(255), nullable=False)
    division_id = db.Column(db.String(255), primary_key=True, nullable=False)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/divisions')
def divisions():
    divisions_list = Divisions.query.all()
    return render_template('divisions.html', divisions_list=divisions_list)

if __name__ == '__main__':
    app.run(debug=True, port =8001)

@app.route('/add_divisions', methods=['GET', 'POST'])
def add_divisions():
    if request.method == 'POST':
        div = request.form['division']
        div_id = request.form['division_id']
        divisions = Divisions(division=div, Division_id=div_id)
        db.session.add(divisions)
        db.session.commit()
        return redirect(url_for('divisions'))
    return render_template('add_divisions.html')


from flask import Flask, render_template, request, redirect, url_for

@app.route('/edit_divisions/<division>', methods=['GET', 'POST'])
def edit_divisions(division):
    division = Divisions.query.get(division)
    if request.method == 'POST':
        Divisions.division = request.form['division']
        db.session.commit()
        return redirect(url_for('division'))
    return render_template('edit_divisions.html', division = division)

