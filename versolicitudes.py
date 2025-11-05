import sqlite3

conn = sqlite3.connect('adopcion.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM solicitudes")
for fila in cursor.fetchall():
    print(fila)

conn.close()