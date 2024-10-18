import mysql.connector

def delete_registration(id):
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9142438445",
            database="mydatabase"
        )
        cursor = conn.cursor()
        
        query = "DELETE FROM Registration WHERE ID=%s"
        cursor.execute(query, (id,))
        
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Registration with ID {id} deleted successfully!")
        else:
            print(f"No record found with ID {id}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
      
        if conn.is_connected():
            cursor.close()
            conn.close()


delete_registration(1)
