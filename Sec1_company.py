import sqlite3

conn = sqlite3.connect('company.db')
db = conn.cursor()

db.execute('CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, Fname TEXT, Sname TEXT, address TEXT, '
           'mobile VARCHAR(11), sex TEXT, b_date TEXT, salary REAL, D_NO INTEGER, FOREIGN KEY(D_NO) REFERENCES '
           'department(id))')

db.execute('CREATE TABLE IF NOT EXISTS department(id INTEGER PRIMARY KEY, D_name TEXT, Location TEXT, Manager_id '
           'INTEGER, FOREIGN KEY(Manager_id) REFERENCES employee(id))')

