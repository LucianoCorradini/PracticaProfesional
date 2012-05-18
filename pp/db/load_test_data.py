#-*- coding: utf-8 -*-
import sqlite3
import csv
import codecs
from sys import exit


#Al definir los .csv los datos que son string o date o time van entre '' y no ""
#las PKs y FKs tienen _id detrás.


#ejemplo de campo válido para la tabla persona
#en db muestra:
#1|1|Blanque|Brian|DNI|20000000|2000-10-10||bblanque@mail.com|46237280||1
#en .csv:
#1,1,'Blanque','Brian','DNI',20000000,'2000-10-10','bblanque@mail.com',46237280,
#,1 -> linea única


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


def csv2db(cursor, tablename):
    reader = UnicodeReader(open(("%s.csv") % (tablename), "rb"),
                            csv.excel, 'utf-8')
    fieldnames = reader.next()
    fieldnamesString = ', '.join(fieldnames)
    try:
        for row in reader:
            r = []
            for data in row:
                if data == '':
                    r.append(u"'null'")
                else:
                    r.append(data)
#            print(row, r)
            rowString = ', '.join(r)
            print(("""INSERT INTO app_%s (%s) VALUES (%s)
                      -----------------------------------\n""" %
                            (tablename, fieldnamesString, rowString)))
            cursor.execute(("INSERT INTO app_%s (%s) VALUES (%s)" %
                            (tablename, fieldnamesString, rowString)))
        return None
    except csv.Error, e:
        exit('file app_%s.csv, line %d: %s' % (tablename, reader.line_num, e))
        return None


##########
##-Main-##
##########
connection = sqlite3.connect("../db.sqlite3")
cursor = connection.cursor()
#acá agregar tablas
csv2db(cursor, 'persona')
csv2db(cursor, 'tipohabitacion')
csv2db(cursor, 'habitacion')
csv2db(cursor, 'turno')
csv2db(cursor, 'turnohabitacion')
csv2db(cursor, 'reserva')
csv2db(cursor, 'solicitudreserva')
csv2db(cursor, 'detallereserva')

cursor.close()
connection.commit()
