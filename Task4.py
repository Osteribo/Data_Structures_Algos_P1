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

## check if number is in column 1 but not column 2 of call
numbers_outgoing = []
numbers_to = []
text_outgoing =[]
text_to = []

telemarketer_numbers = []

# create list of numbers in outoging and incoming
for x in calls:
    if x[0] not in numbers_outgoing:
        numbers_outgoing.append(x[0])
    if x[1] not in numbers_to:
        numbers_to.append(x[1])

for x in texts:
    if x[0] not in text_outgoing:
        text_outgoing.append(x[0])
    if x[1] not in text_to:
        text_to.append(x[1])
 
## check above the previous numbers are not in texts sent and received and incomming
for x in numbers_outgoing:
    if x not in numbers_to and x not in text_outgoing and x not in text_to:
        telemarketer_numbers.append(x)

telemarketer_numbers.sort()
print("These numbers could be telemarketers: ")
for x in telemarketer_numbers:
    print(x)


   
