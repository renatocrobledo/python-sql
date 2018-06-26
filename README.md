# python-sql


Some sql basic test:


CREATE TABLE IF NOT EXISTS  office(
    id INTEGER PRIMARY KEY,
    name VARCHAR(20)
  );

=======================================

INSERT INTO office(id, name) VALUES (NULL, "MKT1"), (NULL, "MKT2"), (NULL, "ART"), (NULL, "PROGRAING"), (NULL, "RH"), (NULL, "UI"), (NULL, "IT1"), (NULL, "IT2");




SPEC:

- El programa deberá mostrar un menú al usuario con la siguiente información:

    [1] insertar oficina
    [2] insertar empleado
    [3] mostrar todas las oficinas
    [4] mostrar todos los empleados
    [5] mostrar la oficina de un empleado especifico
    [6] salir

NOTA:
   * En el número 5 el usuario introduce el nombre del empleado y como resultado
   retornará el nombre de la oficina ala que pertenece.
