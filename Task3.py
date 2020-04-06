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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

## get all the numbers called by (080) numbers
## extract area code
## add them to list
## sort them by lexicographic order
area_code = '(080)'
num_called = []
area_code_called = []
bang_calls = 0
for x in calls:
  if x[0][:5] == area_code:
    if x[1][:1] == '(':
      #remove brackets
      a = x[1].split(")")
      a = a[0].split("(")
      #count the number of 080 to 080 calls
      if a[1] == '080':
        bang_calls += 1
      area_code_called.append(a[1])
    #add toll free numbers
    elif x[1][:3] == '140':
      area_code_called.append(x[1][:3])
    #add mobile numbers
    elif x[1][6] == ' ':
      area_code_called.append(x[1][:4])
    # add number to a list for tracking
    num_called.append(x[1])

## remove duplicates and sort
no_dupe_area_code = list(set(area_code_called))
no_dupe_area_code.sort()

## area codes called
print("The numbers called by people in Bangalore have codes: ")
for x in no_dupe_area_code:
  print(x)


## percentage of (080) to (080) calls
percentage_bang_bang = bang_calls/len(num_called)
print(str(format(percentage_bang_bang, '.2f')) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



