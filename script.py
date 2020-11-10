
secret = 'password'

import psycopg2 as pg2

conn = pg2.connect(database='db_name', user= 'user_name', password = secret)
cur = conn.cursor()

cur.execute('SQL SCRIPT')