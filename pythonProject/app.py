import streamlit as st
import pickle
import pandas as pd


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)

    return recommended_movies


# Load your movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.markdown(
    """
    <style>
    body {
        background-image: url("https://thumbs.dreamstime.com/b/cute-lovely-cartoon-seamless-vector-pattern-background-illustration-popcorn-beverages-cute-lovely-cartoon-seamless-136380012.jpg");
        background-size: cover;

    }
    .stApp {
        background-image: url("https://thumbs.dreamstime.com/b/cute-lovely-cartoon-seamless-vector-pattern-background-illustration-popcorn-beverages-cute-lovely-cartoon-seamless-136380012.jpg");
        background-size: cover;
    }
    .stButton button {
        background-color: red;
        color: white;
        border: none;
        border-radius: 5px;

    }
    .stSelectbox {
        background-color: #ff333;
        border: none;
        border-radius: 5px;
        color: black;
    }
   .stTitle {
    text-align: center;
    color:black;
    }

    .movie-card {
        background-color: red;
        color: white;
        padding: 5px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .center {
    display: flex;
    justify-content: center;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="stTitle">FlickFinder</h1>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Search for your favorite movies:', movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for title in recommendations:
        st.markdown(f'<div class="movie-card"><h5>{title}</h5></div>', unsafe_allow_html=True)


