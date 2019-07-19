"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_numbers =[]

for row in texts:
    
    if not row[0] in phone_numbers:
        phone_numbers.append(row[0])
    if not row[1] in phone_numbers:
        phone_numbers.append(row[1])
        
for row2 in calls:
    
    if not row2[0] in phone_numbers:
        phone_numbers.append(row2[0])
    if not row2[1] in phone_numbers:
        phone_numbers.append(row2[1])
        
print(f"There are {len(phone_numbers)} different telephone numbers in the records.")