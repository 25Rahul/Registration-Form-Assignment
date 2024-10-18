from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="9142438445",  # Replace with your MySQL password
        database="mydatabase"  # Replace with your database name
    )

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    dob = request.form['dob']

    if not name or not email or not dob:
        flash("All fields are required!", "error")
        return redirect('/')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert user details into the database
        query = "INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, dob))
        conn.commit()
        flash("Registration successful!", "success")

    except mysql.connector.Error as err:
        flash(f"Error: {err}", "error")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
