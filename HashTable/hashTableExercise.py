from hashTableChainLinking import HashTable
import pandas as pd

# ------------------------------------------------------------------------------------

def calcMean(arr):
    count = 0
    total = 0 
    for item in h.arr:
        if item:
            total += item[0][1] # add temperatures
            count += 1 # add number of values included
    return total/count

def maxTemp(arr):
    temp =[]
    for item in h.arr:
        if item:
            temp.append(item[0][1])
    return max(temp)


h = HashTable()

df = pd.read_csv('newyorkweather.csv')

for index, row in df.iterrows():
    date = row['date']  # get the date value from the current row
    temperature = row['temperature(F)']  # get the temperature value from the current row
    h[date] = temperature

print(calcMean(h.arr))
print(maxTemp(h.arr))

# ------------------------------------------------------------------------------------

import csv

with open('newyorkweather.csv', 'r') as file:
    reader = csv.DictReader(file)
    temp_dict = {}
    for row in reader:
        date = row['date']
        temp = row['temperature(F)']
        temp_dict[date] = temp

print(temp_dict['Jan 9'])
print(temp_dict['Jan 4'])


# ------------------------------------------------------------------------------------

word_count = {}

with open('poem.txt', 'r') as f:
    for line in f:
        words = line.strip().split() # strip() removes white space, split() splits line into words
        for word in words:
            word_count[word] = len(word)

print(word_count)

import re # regular expressions module

word_count = {}

with open('poem.txt', 'r') as f:
    for line in f:
        # Use a regular expression to split the line into words, accounting for punctuation
        words = re.findall(r'\b\w+\b', line)
        for word in words:
            word_count[word] = len(word)

print(word_count)

# ------------------------------------------------------------------------------------