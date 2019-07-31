"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

g_number = {}

for row in calls:
    if row[0] in g_number:
        g_number[row[0]] += int(row[3])
    
    else:
        g_number[row[0]] = int(row[3])
    
    if row[1] in g_number:
        g_number[row[1]] += int(row[3])
    
    else:
        g_number[row[1]] = int(row[3])

max_value = 0
max_key = ""

for key,value in g_number.items():
    if value > max_value:
        max_key = key
        max_value = value

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_value))