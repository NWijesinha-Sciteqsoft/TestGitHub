'''
Created on Nov 13, 2018

@author: nwijesinha

This exerciser uses dictionaries (dict) or hashes in python code

'''
from patsy import state

# Create a list to hold mapping of state to abbreviation
states = {
    'Oregon':'OR', 
    'Florida':'FL', 
    'California':'CA', 
    'New York':'NY', 
    'Michigan':'MI'
    }

# Create a list to hold basic set of states with cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

#Add some more cities to cities list
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('_' * 20) 
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])
print('_' * 20) 

# Print the cities
print('_' * 20) 
for i in cities:
    print('%s states has:' % i, cities[i])
print('_' * 20) 

# print some states
print('_' * 20)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])
print('_' * 20)

# Print all States
print('_' * 20)
for i in states:
    print("%s's abbreviation is: " % i, states[i] )
print('_' * 20)

# print out some states and cities dict
print('_' * 20)
print('Michigan has:', cities[states['Michigan']])
print('Florida has:', cities[states['Florida']])
print('_' * 20)

# print all States and Abbreviation using items function
print('_' * 20)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))
print('_' * 20)

# print all states and city
print('_' * 20)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))
print('_' * 20)

# print all states with abbreviation and city
print('_' * 20)
for state, abbrev in states.items():
    print("%s state is abbreviate %s and has the city %s" % (state, abbrev, cities[abbrev]))
print('_' * 20)

# Safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print('Sorry, No Texas')
else:
    print('Found %s' % state)
    
# Get City with default value
city = cities.get('TX', 'Does not Exist')
print("The city for the state 'TX' is: %s" % city)
