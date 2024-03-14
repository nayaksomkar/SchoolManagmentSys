from writeinSql import *

connection = userconnect()
cursor = connection.cursor()

cursor.execute('SHOW DATABASES')
#cursor.