import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests
from PIL import Image


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=32e52ea8343bb8b31927e96ae77d6295".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):

    movie_index = np.where(movies_title==movie)
    distances = similarity[movie_index].flatten().tolist()
    movie_list = sorted(enumerate(distances), reverse= True, key= lambda x:x[1])[1:6]
    recommended = []
    recommended_movie_posters = []
    for i in movie_list:
        recommended_movie_posters.append(fetch_poster(movie_id[i[0]]))
        recommended.append(movies_title[i[0]])
    return recommended, recommended_movie_posters


primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
st.title('Movie Recommender System ')
movies = pickle.load(open('movies.pkl','rb'))
movie_overview = movies['tags'].values
movie_id = movies['movie_id'].values
movies_title = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))
option = st.selectbox('Select a Movie from the dropdown',(movies_title))
st.write('You selected:', option)

if st.button('Show Recommendation'):
    names,posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

