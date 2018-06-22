def insert(cursor, sql_command):
  try:
    cursor.execute(sql_command)
    return 'All good!'
  except Exception as error_message:
    print(f'Ups! something went wrong: {error_message}')

class Manager:
  def __init__(self,cursor):
    self.cursor = cursor
  def insertOffice(self, name):
    sql_command = f'INSERT INTO office(id, name) VALUES (NULL, \'{name}\')'
    insert(self.cursor, sql_command)
  def insertEmployee(self, name, lastNme, gender, birth_date, officeId):
    sql_command = f'INSERT INTO empployee(id, name, lastNme, gender, birth_date, officeId) VALUES (NULL, \'{name}\', \'{lastNme}\', \'{gender}\', \'{birth_date}\', \'{officeId}\');'
    insert(self.cursor, sql_command)
    