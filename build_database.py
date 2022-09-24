#!/usr/bin/env python
# Convert TelcoData file to easier to parse CSV

import csv
import sqlite3
import os

input_file = 'sms-email-ocn.csv'
output_file = 'database.sqlite'

os.remove(output_file)

# open datafile and create database
c = csv.reader(open(input_file, 'r'), delimiter=',', quotechar='"')
db = sqlite3.connect(output_file)
cur = db.cursor()
cur.execute("""
CREATE TABLE numbers (
npanxxy int PRIMARY KEY,
company text,
type text,
email text,
ocn text
)
""")

# insert data
for row in c:
    cur.execute(
        'INSERT INTO numbers VALUES("{}", "{}", "{}", "{}", "{}")'.format(
            row[0]+row[1]+row[2], row[3], row[4], row[5], row[6]
        )
    )

db.commit()
db.close()
