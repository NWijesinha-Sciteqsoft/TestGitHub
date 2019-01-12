'''
Created on Jan 11, 2019

@author: nwijesinha
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
# create column names
bnames = ['name', 'sex', 'births']
# Assign file path
pathyob1880 = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\babynames\\yob1880.txt'
# Read data into table
names1880 = pd.read_csv(pathyob1880, sep=',', header=None, names=bnames, engine='python')
print(names1880)
# find te sum of births per year
sum_of_births = names1880.groupby('sex').births.sum()
print(sum_of_births)
'''
# importing all the data files to data frame
# 2010 is the last available year
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

# loop through and upload all the data from the file
for year in years:
    path = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\babynames\\yob%d.txt' % year
    frame = pd.read_csv(path, sep=',', header=None, names=columns, engine='python')
    
    frame['year'] = year
    pieces.append(frame)
    
# Concatenate everything into a single Data Frame
names = pd.concat(pieces, ignore_index=True)
# print(names)

# aggregate the data at the year and sex level
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births)


def add_prop(group):
    # Integer divsion floors
    births = group.births.astype(float)
    
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)
print(names)

print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

# Analyzing Naming Trends for boys and girls

print(top1000)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births_names = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

print(total_births_names)

# subset of total births
subset = total_births_names[['John', 'Harry', 'Mary', 'Marilyn']]

subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(title='Sum of table100.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# plt.show()

df = boys[boys.year == 2010]
print(df)

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
# print(prop_cumsum)

print(prop_cumsum.searchsorted(0.5))

df = boys[boys.year == 1900]

in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
print(in1900.searchsorted(0.5) + 1)


def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return float(group.prop.cumsum().searchsorted(q) + 1)


diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
print(diversity.head())

diversity.plot(title="Number of popular names in top 50%")
# plt.show()

# extract last letter from name column
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')

print(subtable.head())
print(subtable.sum())
letter_prop = subtable / subtable.sum().astype(float)
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
print(dny_ts.head())
dny_ts.plot()

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
print(lesley_like)
filtered = top1000[top1000.name.isin(lesley_like)]
print(filtered.groupby('name').births.sum())
table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
table.tail()
table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()

