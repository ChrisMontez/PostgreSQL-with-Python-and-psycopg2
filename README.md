## Function

- Establish connection between a Python application and a PostgreSQL database.

## Process
1. Create connection object
``conn = pg2.connect(database='db_name', user= 'user_name', password = secret)``

2. Create a cursor Object
``cur = conn.cursor()``

3. Run Queries
``cur.execute('SQL SCRIPT')``

4. Free Resources 
``cur.close()``
