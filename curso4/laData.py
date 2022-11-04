import sqlite3
import urllib.request,urllib.parse, urllib.error

from bs4 import BeautifulSoup

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

archivo = input('Enter file name: ')
if (len(archivo) < 1): archivo = 'mbox.txt'
fh = open(archivo)
for line in fh:
    line = line.strip()
    if not line.startswith('From: '): continue
    pieces = line.split()
    nombres = pieces[1]
    dom = nombres.find('@')
    email = nombres[dom+1:len(nombres)]


    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
palabras = str(sqlstr)
sorted(palabras)
for row in cur.execute(sqlstr):
    print((row[0]), row[1])

cur.close()