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

unique_list = []
for x in calls:
    if x[0] not in unique_list:
        unique_list.append(x[0])

num_unique = len(unique_list)

print("There are " + str(num_unique) + " different telephone numbers in the records.")

#DONE