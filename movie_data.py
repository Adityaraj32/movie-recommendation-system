import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# print(movies.info())
# print(ratings.info())
print(ratings['rating'].unique())
