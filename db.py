import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'workers',
    user = 'root',
    password = ''
)
mycursor = mydb.cursor(dictionary=True)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Employee(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(200)NOT NULL,
        gender VARCHAR
        (55) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(200) NOT NULL,
        address VARCHAR(200) NOT NULL,
        password VARCHAR(200) NOT NULL,
        qualification VARCHAR(200) NOT NULL,
        hire_date VARCHAR(50) NOT NULL,
        position VARCHAR(100) NOT NULL,
        department_id INT NOT NULL,
        phone_no INT NOT NULL,
        state VARCHAR(50) NOT NULL,
        PRIMARY KEY(ID)
    );
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Department(
        ID INT NOT NULL AUTO_INCREMENT,
        job_department VARCHAR(100) NOT NULL,
        salary_range INT NOT NULL,
        description VARCHAR(300) NOT NULL,
        PRIMARY KEY(ID)
    );
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Salary(
        ID INT NOT NULL AUTO_INCREMENT,
        job_id INT NOT NULL,
        Amount INT NOT NULL,
        Annual INT NOT NULL,
        BONUS INT NOT NULL,
        PRIMARY KEY(ID)
    );
    """
)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Admin(
 ID INT NOT NULL AUTO_INCREMENT,
 full_name VARCHAR(200) NOT NULL,
 gender VARCHAR(10) NOT NULL,
 age INT NOT NULL,
 email VARCHAR(200) NOT NULL,
 address VARCHAR(200) NOT NULL,
 password VARCHAR(200) NOT NULL,
 qualification VARCHAR(200) NOT NULL,
 tittle VARCHAR(100) NOT NULL,
 phone_no INT NOT NULL,
 state VARCHAR(50) NOT NULL,
 PRIMARY KEY(ID)
);
"""
)