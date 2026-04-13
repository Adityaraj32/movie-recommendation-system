import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('movies.csv')
movies['genres'] = movies['genres'].str.replace("|",' ')

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix)

def get_recommendations(movie):
    try:
        movie_title = movies[movies['title'].str.lower().str.contains(movie)]['title'].iloc[0]
    except Exception as e:
        return None
    idx = movies[movies['title'].str.lower() == movie_title.lower()].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores.sort(key=lambda x:x[1],reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [x[0] for x in sim_scores]
    return movies['title'].iloc[movie_indices].values
