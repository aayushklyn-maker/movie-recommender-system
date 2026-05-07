import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster_path(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=d078035748563d02e716196ad7120e34&language=en-US'.format(movie_id)

    # Tell the API you are a standard Chrome browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    data = response.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path

def recommend(movie_name):
    similarity_score = similarity[movie[movie['title']==movie_name].index[0]]
    movies_list = sorted(enumerate(similarity_score),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_index = i[0]
        recommended_movies.append(movie.iloc[movie_index]['title'])
        recommended_movies_posters.append(fetch_poster_path(movie.iloc[movie_index]['id']))
    return recommended_movies,recommended_movies_posters

movie = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    "Select your favourite movie",
    movie['title']
)

if st.button("Recommend", type="primary"):
    recommendations,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(recommendations[0])
        st.image(posters[0])

    with col2:
        st.write(recommendations[1])
        st.image(posters[1])

    with col3:
        st.write(recommendations[2])
        st.image(posters[2])

    with col4:
        st.write(recommendations[3])
        st.image(posters[3])

    with col5:
        st.write(recommendations[4])
        st.image(posters[4])