import mysql.connector as sql


class DataBase:

    def __init__(self):
        try:
            self.cnx = sql.connect(user='poulstar', password='poulstar',
                host='127.0.0.1', database='juniors')
            self.cursor = self.cnx.cursor()
            print("Successfully Connected!")
        except:
            print("Something is wrong with your connection")

    def close(self):     
        self.cnx.commit()
        self.cnx.close()

    def create(self, name, last_name, b_date, sex, mail, phone, id_n, addr):
        data = (name, last_name, b_date, sex, mail, phone, id_n, addr)
        query = """
        INSERT INTO student
        (first_name, last_name, birth_date, sex, email, phone, id_card, address)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(query, data)
        self.close()


    def read(self):
        query = "SELECT * FROM student;"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.close()
        return data


    def update(self, col, val, id_):
        data = ( val, id_)
        query = "UPDATE student SET "+ col +"=%s WHERE student_id=%s;"
        self.cursor.execute(query, data)
        self.close()


    def delete(self, id_):
        data = (id_, )
        query = """
        DELETE FROM student WHERE student_id=%s;
        """
        self.cursor.execute(query, data)
        self.close()