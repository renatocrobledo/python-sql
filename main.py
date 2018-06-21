import sqlite3

try:
  connection = sqlite3.connect("company.db") ## CREATE DATABASE company;

  cursor = connection.cursor()
  
  cursor.execute("PRAGMA foreign_keys = 1")

  '''
    comandos con referencia al esquema:
    CREATE, DROP
  '''
  
  sql_command = """
  INSERT INTO office (
      id,
      name
  ) VALUES (
      NULL,
      "MKT"
  );
  """
  cursor.execute(sql_command)

  sql_command = """
    INSERT INTO employee (
        id,
        name,
        lastNme,
        gender,
        birth_date,
        officeid
    ) VALUES (
        NULL,
        "PEPE",
        "LEPU",
        "H",
        "1988-05-21",
        5
    );
  """

  cursor.execute(sql_command)
  
  cursor.execute("SELECT * FROM employee")
  result = cursor.fetchall()
  print(result)
  
  connection.commit()
  connection.close()

except Exception as identifier:
  print('Ups! something went wrong...')
  print(identifier)



