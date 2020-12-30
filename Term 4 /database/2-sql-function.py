from crud import connect, create, delete, select, update

cnx, cursor = connect()
# create(
#     cnx,
#     cursor,
#     'parpar',
#     'azhdar',
#     '2000-01-01',
#     'm',
#     'a@a.com',
#     '09876541232',
#     '2375923827',
#     'asd'
# )

# delete(cnx, cursor, 11)

# update(cnx, cursor,'first_name', 'hooshang', 10)

persons = select(cnx, cursor)
for person in persons:
    print(person)