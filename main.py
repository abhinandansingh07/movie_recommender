import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# -----------------------------
# Load Data
# -----------------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# -----------------------------
# Custom CSS
# -----------------------------
page_bg = """
<style>
/* Background image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Transparent overlay for main container */
.block-container {
    background: rgba(0, 0, 0, 0.65);
    padding: 2rem;
    border-radius: 15px;
}

/* White text everywhere */
h1,h2,h3,h4,h5,h6,p,span,div,label {
    color: white !important;
}

/* ---- SELECTBOX ---- */
div[data-baseweb="select"] {
    background-color: black !important;
    color: white !important;
    border: 1px solid #666 !important;
    border-radius: 8px !important;
}

div[data-baseweb="select"] * {
    color: white !important;
}

/* Dropdown options */
ul[role="listbox"] {
    background-color: black !important;
    color: white !important;
    border-radius: 6px;
}
li[role="option"] {
    background-color: black !important;
    color: white !important;
}
li[role="option"]:hover {
    background-color: #333 !important;
    color: #ff4c4c !important;
}

/* Button */
.stButton>button {
    background-color: #ff4c4c;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #e60000;
    transform: scale(1.05);
}

/* Recommended movie cards */
.movie-card {
    background: rgba(255,255,255,0.08);
    padding: 1rem;
    margin: 0.5rem;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    color: white;
    transition: 0.3s;
}
.movie-card:hover {
    background: rgba(255,255,255,0.2);
    transform: scale(1.05);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# -----------------------------
# Streamlit UI
# -----------------------------
st.title('🍿 Movie Recommender System')

# Dropdown for movie selection
selected_movie_name = st.selectbox(
    '🎬 Choose a movie you like:',
    movies['title'].values
)

# Button to recommend
if st.button("✨ Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("### 🔮 Recommended Movies:")
    cols = st.columns(5)
    for i, movie in enumerate(recommendations):
        with cols[i % 5]:
            st.markdown(f"<div class='movie-card'>{movie}</div>", unsafe_allow_html=True)
