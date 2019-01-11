'''
Created on Jan 10, 2019

@author: nwijesinha

Using movielens sameple file for Data Analytics using python

'''

import pandas as pd

# Add paths to the data files
path_movies = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\movielens\\movies.dat'
path_ratings = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\movielens\\ratings.dat'
path_users = 'C:\\Users\\nwijesinha\\git\\pydata-book\\datasets\\movielens\\users.dat'

# Define table column names
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
# Assign user data to users
users = pd.read_table(path_users, sep='::', header=None, names=unames, engine='python')

# Define table column names
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
# Assign ratings data to ratings
ratings = pd.read_table(path_ratings, sep='::', header=None, names=rnames, engine='python')

# Define table column names
mnames = ['movie_id', 'title', 'genres']
# Assign movies data to movies
movies = pd.read_table(path_movies, sep="::", header=None, names=mnames, engine='python')

# Checking the data import was completed properly by printing the tables
print("Printing User table first 5 rows")
print(users[:5])
print('*' * 40)
print("Printing rating table first 5 rows")
print(ratings[:5])
print('*' * 40)
print("Printing movies table first 5 rows")
print(movies[:5])
print('*' * 40)
print("Printing complete rating table")
print(ratings)
print('*' * 40)

# merge the data tables
data = pd.merge(pd.merge(ratings, users), movies)
# print merged table
# print(data[:5])
# print('*' * 40)

# print first record
print(data.ix[0])

# calculate the mean rating using pivot_tables function
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5])
