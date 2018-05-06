'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Practical: 4; SQLite
    Author: kmbutterfield
    File name: createdb.py
    Description: Creates an SQLite database with a single row.
'''

import sqlite3

# Connect to the database file, or create it
conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()

# Create a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Results(address TEXT, burglaries INTEGER)')

# Insert a row into the table wtith the following
def data_entry():
    c.execute("INSERT INTO Results VALUES('Queen Vic', 2)")

# Comit creations and close the database
conn.commit()
conn.close()
