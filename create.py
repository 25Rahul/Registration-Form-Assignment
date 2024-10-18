import mysql.connector

def create_registration(name, email, dob):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9142438445",
            database="mydatabase"
        )
        cursor = conn.cursor()
        query = "INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, dob))
        conn.commit()
        print("Registration created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

create_registration("John Doe", "john.doe@example.com", "1990-05-15")