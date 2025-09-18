from mysql import connector

class TeacherModel:
    def __init__(self):
        self.conn = self.get_connection()
    
    def get_connection(self):
        return connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="school_db"
        )
    
    def get_teachers(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("select * from teachers")
        data=cursor.fetchall()
        return data
    
    def add_teachers(self,full_name,email):
        cursor = self.conn.cursor()
        
        cursor.execute(f"insert into teachers(full_name,email) values('{full_name}','{email}')")
        # cursor.connection.commit()
        return True
    
    def update_teachers(self,tid,full_name,email):
        cursor = self.conn.cursor()
        
        cursor.execute(f"update teachers set full_name='{full_name}',email='{email}' where teacher_id={tid}")
        # cursor.connection.commit()
        return True
    
    def delete_teachers(self,tid):
        cursor = self.conn.cursor()
        
        cursor.execute(f"delete from teachers where teacher_id={tid}")
        # cursor.connection.commit()
        return True