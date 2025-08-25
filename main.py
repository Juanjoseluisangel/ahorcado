from customtkinter import *
from sqlite3 import *

BD = connect("base.db")
cr = BD.cursor()

def creartabla():
    cr.execute('''
    create table if not exists base(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    descripcion TEXT NOT NULL);''')
    BD.commit()

def Ingresarpalabra():
    n = input("ingresa la palabra")
    d = input("ingresa una pequeña descripcion de la palabra")

    cr.execute('''
    INSERT INTO base(palabra, descripcion)
     VALUES(?,?);''',(n, d))
    BD.commit()

def verpalabras():
    cr.execute('''
    SELECT * FROM base;''')

    base = cr.fetchall()
    for base in base:
        print(base)

def modificarpalabra():
    i = int(input("ingrese el id de la palabra a modificar"))
    n = input("ingresa la nueva palabra")
    d = input("ingrese la nueva descripcion")

    cr.execute('''
          UPDATE base
          SET palabra = ?, descripcion = ?
          WHERE id = ?;''', (n, d, i))
    BD.commit()

def eliminarpalabra():
    i = int(input("ingrese el id de la palabra que quiere eliminar"))

    cr.execute('''
          DELETE FROM base WHERE id = ?;''', (i,))
    BD.commit()



