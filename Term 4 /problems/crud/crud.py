import mysql.connector as sql
from mysql.connector import cursor


def connect():
    try:
        cnx = sql.connect(user='poulstar', password='poulstar',
            host='127.0.0.1', database='gym')
        cursor = cnx.cursor()
        print("Successfully Connected!")
        return cnx, cursor
    except :
        print("Something is wrong with your connection")
        return None, None


def create(cnx, cursor, first_name, last_name, phone, sex):
    data = (first_name, last_name, phone, sex)
    query = """
    INSERT INTO athles
    (first_name, last_name, phone, sex)
    VALUES
    (%s, %s, %s, %s);
    """
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("INSERT SUCCESSFULLY DONE!")


def read(cnx, cursor):
    query = """
    SELECT * FROM athles;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    print("READ SUCCESSFULLY DONE!")
    return data


def update(cnx, cursor, f, l, p, s, id_):
    data = (f, l, p, s, id_)
    query = """
    UPDATE athles
    SET first_name=%s, last_name=%s, phone=%s, sex=%s
    WHERE id=%s;
    """
    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("UPDATE SUCCESSFULLY DONE!")


def delete(cnx, cursor, id_):
    query = f"""
    DELETE FROM athles
    WHERE id={id_};
    """
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("DELETE SUCCESSFULLY DONE!")


def get_one(cnx, cursor, id_):
    query = f"""
    SELECT * FROM athles WHERE id={id_};
    """
    cursor.execute(query)
    data = cursor.fetchone()
    cnx.commit()
    cursor.close()
    cnx.close()
    print("READ SUCCESSFULLY DONE!")
    return data
