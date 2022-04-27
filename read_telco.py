#!/usr/bin/env python
# Convert TelcoData file to easier to parse CSV

import csv

source = open('sms-email-ocn.csv', 'r')
dest = open('database.csv', 'w')

c = csv.reader(source, delimiter=',', quotechar='"')

for row in c:
    dest.write('|'.join(row))
    dest.write('\n')
