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
class Departments (db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(255))

# Table routes
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


if __name__ == '__main__':
    app.run(debug=True)