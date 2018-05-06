'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Practical: 4; SQLite
    Author: kmbutterfield
    File name: readdb.py
    Description: Script to read through an SQLite database by row.
'''

import sqlite3

# Connecting to the database file
conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()

# Using cursor, select all rows from the results & order by num of burglaries
for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    print((row[1]), "burglaries have happened at", (row[0]))
