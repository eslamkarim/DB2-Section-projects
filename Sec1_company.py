import sqlite3

conn = sqlite3.connect('company.db')
db = conn.cursor()

db.execute('CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, Fname TEXT, Sname TEXT, address TEXT, '
           'mobile VARCHAR(11), sex TEXT, b_date TEXT, salary REAL, D_NO INTEGER, FOREIGN KEY(D_NO) REFERENCES '
           'department(Dnum))')

db.execute('CREATE TABLE IF NOT EXISTS department(Dnum INTEGER PRIMARY KEY, D_name TEXT, Location TEXT, Manager_id '
           'INTEGER, FOREIGN KEY(Manager_id) REFERENCES employee(id))')

db.execute('CREATE TABLE IF NOT EXISTS projects(Pnum INTEGER PRIMARY KEY, Pname TEXT, Plocation TEXT, Dnum INTEGER, '
           'Empid INTEGER, FOREIGN KEY(Empid) REFERENCES employee(id), FOREIGN KEY(Dnum) REFERENCES '
           'department(Dnum))')

db.execute('CREATE TABLE IF NOT EXISTS works_on(Empid INTEGER, Pnum INTEGER, hours INTEGER, FOREIGN KEY(Empid) '
           'REFERENCES employee(id),FOREIGN KEY(Pnum) REFERENCES projects(Pnum))')

