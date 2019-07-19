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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

f_t = texts[0]
l_c = calls[-1]

print(f"First record of texts, {f_t[0]} texts {f_t[1]} at time {f_t[2]}")
print(f"Last record of calls, {l_c[0]} calls {l_c[1]} at time {l_c[2]}, lasting {l_c[3]} seconds")


