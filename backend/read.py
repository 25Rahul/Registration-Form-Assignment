import mysql.connector

def read_registrations():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9142438445",
            database="mydatabase"
        )
        cursor = conn.cursor()
        
        query = "SELECT * FROM Registration"
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        if result:
            for row in result:
                print(row)  
        else:
            print("No registrations found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        
        if conn.is_connected():
            cursor.close()
            conn.close()

read_registrations()
