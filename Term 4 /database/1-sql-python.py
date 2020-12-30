import mysql.connector as sql

try:
    cnx = sql.connect(user='poulstar', password='poulstar',
        host='127.0.0.1', database='juniors')
    cursor = cnx.cursor()
    print("Successfully Connected!")
except :
    print("Something is wrong with your connection")

query = """
INSERT INTO student
(first_name, last_name, birth_date, sex, email, phone, id_card, address)
VALUES
('sina', 'bakhshandeh', '2006-01-01', 'm', 'sina@bakhshandeh.com', '09115555555', '2104879865', 'Guilan Bolvar');
"""

cursor.execute(query)
cnx.commit()

cursor.close()
cnx.close()