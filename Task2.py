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

#makes a list of unique phone numbers

time_per_number = {}
unique_list = []
for x in calls:
    if x[0] not in unique_list:
        unique_list.append(x[0])

##adds up all the seconds per phone number 

for i in unique_list:
    time_per_number[i]=0
    for x in calls:
        ## checks both phone numbers and adds up total time
        if x[0] == i or x[1] == i:
            curret_time = time_per_number[i]
            total_time = int(x[3]) + int(curret_time)
            time_per_number[i] = total_time


## find the highest value in the dictionary
max_value = 0
max_key = '78130 00821'
for key in time_per_number:
    a = time_per_number[key]
    b = time_per_number[max_key]
    
    if a > b:
        max_key = key
        
        #print(max_key)
        #print(time_per_number[max_key])
print(str(max_key) + " spent the longest time, " + str(time_per_number[max_key]) + " seconds, on the phone during September 2016.")
            
