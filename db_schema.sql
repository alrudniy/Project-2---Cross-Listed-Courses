

-- Excel "Department Description" goes into departments table,  department column

-- Excel "Division Desc" goes into divisions table, division column
 
-- Excel columns BART, BHUM, BINT, BNS, BSS, DVIT, DVUS, FLAN, GLC, IMMX, PPD, QUAN, WRIT, WRMJ become values in the attribute column of the attributes table

-- Excel column "Course Attribute(s)" goes into attributes table, column attribute_description

----------------------------------------------------------------------------------
-- **Alan** finish the code for this table, run code in sqlite to create the table
----------------------------------------------------------------------------------
CREATE TABLE courses (
course_id INTEGER PRIMARY KEY,
subject_code VARCHAR(10),
course_number  VARCHAR(10),
college  VARCHAR(5),
department_code
division_code
short_title
long_title 
last_term_offered 
);

----------------------------------------------------------------------------------
-- **Jarry** finish the code for this table, run code in sqlite to create the table
----------------------------------------------------------------------------------
CREATE TABLE course_attributes (
attribute_code VARCHAR(10) PRIMARY KEY,
attribute
attribute_description
);

----------------------------------------------------------------------------------
-- **Katerina** finish the code for this table, run code in sqlite to create the table
----------------------------------------------------------------------------------
CREATE TABLE prerequisites (
prereq_code VARCHAR(10) PRIMARY KEY,
prerequisite
);

----------------------------------------------------------------------------------
-- **EACH TEAM MEMBER** run code in sqlite to create the table
----------------------------------------------------------------------------------
courses_attrb_prereqs (
course_id INTEGER,
attribute_code VARCHAR(10),
prereq_code  VARCHAR(10),
PRIMARY KEY ( course_id, attribute_code, prereq_code)
);

----------------------------------------------------------------------------------
-- **Liz** finish the code for this table, run code in sqlite to create the table
----------------------------------------------------------------------------------
CREATE TABLE departments(
department_id INTEGER PRIMARY KEY,
department VARCHAR(255)
) ;

----------------------------------------------------------------------------------
-- **Maddie** finish the code for this table, run code in sqlite to create the table
----------------------------------------------------------------------------------
CREATE TABLE divisions(
division_id INTEGER,
division 
);