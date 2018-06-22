from db_controller import connection, cursor
from db_model import Manager

db_manager = Manager(cursor)

db_manager.insertOffice('Programing')

cursor.execute("SELECT * FROM office")
result = cursor.fetchall()
print(result)


# connection.commit()
connection.close()


'''
cursor.execute(sql_command)

cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
print(result)
'''


