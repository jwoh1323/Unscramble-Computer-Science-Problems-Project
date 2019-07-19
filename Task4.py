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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = []


for row in calls:
    
    telemarketers.append(row[0])


for row in calls:
    
    if row[1] in telemarketers:
        
        telemarketers.remove(row[1])
        
for row in texts:
    
    if row[0] in telemarketers:
        
        telemarketers.remove(row[0])
    
    if row[1] in telemarketers:
        
        telemarketers.remove(row[1])

final_list = []

for row in telemarketers:
    
    if not row in final_list:
        
        final_list.append(row)
        
print(f"These numbers could be telemarketers:{sorted(final_list)}")  