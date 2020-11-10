# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:33:38 2020

@author: cmont
"""

secret = 'password'

import psycopg2 as pg2

conn = pg2.connect(database='db_name', user= 'user_name', password = secret)
cur = conn.cursor()

cur.execute('SQL SCRIPT')