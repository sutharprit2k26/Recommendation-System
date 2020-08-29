# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:42:01 2020

@author: Pritesh

"""


import numpy as np
import pandas as pd

data = pd.read_csv('ratings.csv')


movie_titles_genre = pd.read_csv('movies.csv')


data = data.merge(movie_titles_genre,on='movieId', how='left')


Average_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())


Average_ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())


# Building The Recommender

# Calculating The Correlation
movie_user = data.pivot_table(index='userId',columns='title',values='rating')

print("Enter the movie name you like to search related:")
liked_movie = input()

correlations = movie_user.corrwith(movie_user[liked_movie])

recommendation = pd.DataFrame(correlations,columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])

# testing the recommendation system

recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()
print(recc.head())



