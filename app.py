from logging import debug, FileHandler, WARNING
from flask import Flask, render_template, redirect, request
from db import mydb, mycursor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('INDEX.HTML', template_folder = 'template')

    file_handler = FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)




@app.route('/employees')
def employee():
    mycursor.execute("SELECT * FROM Employee")
    Employee = mycursor.fetchall()
    return render_template('INFOR.HTML', Employee = Employee)

@app.route('/submit', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('REG.HTML')
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']
        qualification = request.form['qualification']
        date = request.form['date']
        position = request.form['position']
        department_id = request.form['department_id']
        phone = request.form['phone']
        state = request.form['state']

        sql = 'INSERT INTO Employee(name, gender, age, email, address, password, qualification, hire_date, position, department_id, phone_no, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (full_name, gender, age, email, address, password, qualification, date, position, department_id, phone, state)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')


@app.route('/submit1', methods=['GET', 'POST'])
def add_department():
    if request.method == 'GET':
        return render_template('DEP.HTML')
    if request.method == 'POST':
        job_department = request.form['job_department']
        salary_range = request.form['salary_range']
        job_description = request.form['job_description']

        sql = 'INSERT INTO Department(job_department, salary_range, description) VALUES(%s,%s,%s)'
        val = (job_department, salary_range, job_description)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/submit2')

@app.route('/submit2', methods=['GET', 'POST'])
def add_salary():
    if request.method == 'GET':
        return render_template('SAL.HTML')
    if request.method == 'POST':
        job_id = request.form['job_id']
        amount = request.form['amount']
        Annual = request.form['Annual']
        bonus = request.form['bonus']

        sql = 'INSERT INTO Salary(job_id, Amount, Annual, BONUS) VALUES(%s,%s,%s,%s)'
        val = (job_id, amount, Annual, bonus)
        mycursor.execute(sql, val)

        mydb.commit()
        return redirect('/', message = "you have entered data successfully")



@app.route('/about')
def about_us():
    return render_template('ABOUT.HTML')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Employee WHERE ID={id}')
        Employee = mycursor.fetchone()
        return render_template('EDIT.HTML', Employee = Employee)
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']
        qualification = request.form['qualification']
        date = request.form['date']
        position = request.form['position']
        department_id = request.form['department_id']
        phone = request.form['phone']
        state = request.form['state']

        sql = f'UPDATE Employee SET full_name = %s, gender = %s, age= %s, email= %s, password= %s, address= %s, qualification= %s, date= %s, position= %s, department_id= %s, state= %s, WHERE ID = %s'
        values =  (full_name, gender, age, email, password, address, qualification, date, position, department_id, state)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port=9989,use_reloader=False)