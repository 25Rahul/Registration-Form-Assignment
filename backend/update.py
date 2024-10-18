import mysql.connector

def update_registration(id, name=None, email=None, dob=None):
    try:
      
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9142438445",
            database="mydatabase"
        )
        cursor = conn.cursor()

        fields = []
        values = []
        if name:
            fields.append("Name=%s")
            values.append(name)
        if email:
            fields.append("Email=%s")
            values.append(email)
        if dob:
            fields.append("DateOfBirth=%s")
            values.append(dob)
        
        values.append(id) 
        
        
        query = f"UPDATE Registration SET {', '.join(fields)} WHERE ID=%s"
        cursor.execute(query, values)
        
   
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Registration with ID {id} updated successfully!")
        else:
            print(f"No record found with ID {id}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
       
        if conn.is_connected():
            cursor.close()
            conn.close()


update_registration(1, name="Jane Doe", email="jane.doe@example.com")
