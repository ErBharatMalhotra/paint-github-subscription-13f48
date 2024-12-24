import streamlit as st
import pickle
import pandas as pd
import requests


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)


def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NzFlNjZkODBlNzVlMDY1NWQxZWNjYTE3OWYyYjc1YSIsInN1YiI6IjY0YmQwNmI5ZTlkYTY5MDBlY2VhNjJmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9oIez0y-WbwchQvc-avTyxaRA2Av8H9DrdGdWmOHoEk",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    print(response.text)

    return "https://image.tmdb.org/t/p/original" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    recommended_movies = []
    recommend_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_posters(movie_id))
    return recommended_movies, recommend_movie_posters


similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted?", movies["title"].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0] )
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
