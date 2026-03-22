from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import smtplib

app = Flask(__name__)
app.secret_key = "change_this_to_a_strong_secret"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aakash_7890",
    database="student_result_system"
)

cursor = db.cursor()

# ---------------- HOME ----------------

@app.route('/')
def home():
    return render_template("login.html")


# ---------------- STUDENT LOGIN ----------------

@app.route('/student_login', methods=['POST'])
def student_login():

    student_id = request.form['student_id']
    password = request.form['password']

    query = "SELECT * FROM students WHERE student_id=%s AND password=%s"

    cursor.execute(query,(student_id,password))

    student = cursor.fetchone()

    if student:
        return redirect(url_for('student_dashboard', student_id=student_id))
    else:
        return "Invalid Student Login"


# ---------------- STUDENT DASHBOARD ----------------

@app.route('/student_dashboard/<int:student_id>')
def student_dashboard(student_id):
    # Load student info
    cursor.execute("SELECT name FROM students WHERE student_id=%s", (student_id,))
    student = cursor.fetchone()
    if not student:
        return "Student not found", 404

    name = student[0]

    # Load results
    cursor.execute("SELECT subject, marks, grade FROM results WHERE student_id=%s", (student_id,))
    results = cursor.fetchall()

    return render_template("student_dashboard.html", name=name, results=results, student_id=student_id)


# ---------------- ADMIN LOGIN PAGE ----------------

@app.route('/admin')
def admin():
    return render_template("admin_login.html")


# ---------------- ADMIN DASHBOARD ----------------

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template("admin_dashboard.html")


# ---------------- ADMIN LOGIN ----------------

@app.route('/admin_login', methods=['POST'])
def admin_login():

    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM admin WHERE username=%s AND password=%s"

    cursor.execute(query,(username,password))

    admin = cursor.fetchone()

    if admin:
        return redirect(url_for('admin_dashboard'))
    else:
        return "Invalid Admin Login"


# ---------------- ADD STUDENT PAGE ----------------

@app.route('/add_student_page')
def add_student_page():
    return render_template("add_student.html")


# ---------------- ADD STUDENT ----------------

@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    course = request.form['course']
    password = request.form['password']

    sql = "INSERT INTO students(name,email,mobile,course,password) VALUES(%s,%s,%s,%s,%s)"

    values = (name,email,mobile,course,password)

    cursor.execute(sql,values)

    db.commit()

    return redirect(url_for('admin_dashboard'))


# ---------------- UPLOAD RESULT PAGE ----------------

@app.route('/upload_result_page')
def upload_result_page():
    return render_template("upload_result.html")


# ---------------- EMAIL FUNCTION ----------------

def send_email(receiver):

    sender = "aakashdubb@gmail.com"
    password = "mvld nmcx gety rjmy"

    message = """Subject: Result Published

Your result has been uploaded.
Login to check your marks.
"""

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,password)
        server.sendmail(sender,receiver,message)
        server.quit()

        print("Email sent")

    except Exception as e:
        print("Email Error:", e)


# ---------------- UPLOAD RESULT ----------------

@app.route('/upload_result', methods=['POST'])
def upload_result():

    student_id = request.form['student_id']
    subject = request.form['subject']
    marks = request.form['marks']
    grade = request.form['grade']

    sql = "INSERT INTO results(student_id,subject,marks,grade) VALUES(%s,%s,%s,%s)"

    values = (student_id,subject,marks,grade)

    cursor.execute(sql,values)

    db.commit()

    # get student email
    cursor.execute("SELECT email FROM students WHERE student_id=%s", (student_id,))
    row = cursor.fetchone()
    if not row:
        return "Result uploaded, but student not found to send email."

    email = row[0]
    send_email(email)

    return "Result Uploaded and Email Alert Sent"


# ---------------- VIEW RESULT PAGE ----------------

@app.route('/view_result_page')
def view_result_page():
    return render_template("view_result_page.html")


# ---------------- VIEW RESULT ----------------

@app.route('/view_result', methods=['POST'])
def view_result():

    student_id = request.form['student_id']

    query = "SELECT subject,marks,grade FROM results WHERE student_id=%s"

    cursor.execute(query,(student_id,))

    results = cursor.fetchall()

    return render_template("view_result.html",results=results)


if __name__ == "__main__":
    app.run(debug=True)