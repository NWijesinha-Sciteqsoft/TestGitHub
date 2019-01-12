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

# filter movies that received at least 250 ratings
# Create a data frame to capture rating by title
rating_by_title = data.groupby('title').size()
print(rating_by_title[:10])
# create a dataframe to capture rating which got more than 250
active_titles = rating_by_title.index[rating_by_title >= 250]
print(active_titles[:10])
# Index the titles which recieve 250 in mean ratings using active titles
mean_ratings = mean_ratings.ix[active_titles]
print(mean_ratings[:10])

# Filer tp films among female viewers
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:10])
# Find most division between male and female viewers for movies
mean_ratings['Diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='Diff')
print(sorted_by_diff[:15])
# Find the movies prefered by mean that women did not like
print(sorted_by_diff[::-1][:15])

# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active title
rating_std_by_title = rating_std_by_title.ix[active_titles]
# order Series by value in descending order
print(rating_std_by_title.sort_values(ascending=False)[:10])

