'''
Created on Jan 8, 2019

@author: nwijesinha

'''
import json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\bitly_usagov\\example.txt'

records = [json.loads(line) for line in open(path)]
print(records[0])
print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])


# define a function to get counts
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


# create get counts using Python Standard Library
def get_counts2(sequence):
    counts = defaultdict(int)  # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))


# define a function to return top ten counts
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs


print(top_counts(counts))

# use collection.Counter class to get top ten
counts = Counter(time_zones)
print(counts.most_common(10))

# using panda DataFram to represent data as table
frame = DataFrame(records)
print(frame)

print(frame['tz'][:10])
# Using Series object valur_counts to get the count
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

tz_counts[:10].plot(kind='barh', rot=0)
plt.show()

print(frame['a'][1])
print(frame['a'][50])
print(frame['a'][51])

