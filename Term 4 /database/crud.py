import mysql.connector as sql


def connect():
    try:
        cnx = sql.connect(user='poulstar', password='poulstar',
            host='127.0.0.1', database='juniors')
        cursor = cnx.cursor()
        print("Successfully Connected!")
        return cnx, cursor
    except :
        print("Something is wrong with your connection")
        return None

def create(cnx, cursor, name, last_name, b_date, sex, mail, phone, id_n, addr):
    data = (name, last_name, b_date, sex, mail, phone, id_n, addr)
    query = """
    INSERT INTO student
    (first_name, last_name, birth_date, sex, email, phone, id_card, address)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

def delete(cnx, cursor, id_):
    data = (id_, )
    query = """
    DELETE FROM student WHERE student_id=%s;
    """
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

# amirmohammad
def update(cnx, cursor, col, val, id_):
    data = ( val, id_)
    query = "UPDATE student SET "+ col +"=%s WHERE student_id=%s;"
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

#nozhan
def select(cnx, cursor):
    query = "SELECT * FROM student;"
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    return data
