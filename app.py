import pickle
import streamlit as st

def recommend(movie):
    if movie not in movies['title'].values:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommendations_movies_name = []
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    for i in movies_list[1:6]:
        recommendations_movies_name.append(movies.iloc[i[0]]['title'])
    return recommendations_movies_name

# Add custom CSS for background and box styling
st.markdown(
    """
    <style>
    body {
        background-image: url('data/BG.jpg'); /* Ensure this path is correct */
        background-size: cover;
        background-attachment: fixed;
    }
    .main-box {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrap main components in a box
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="text-align: center; font-family: 'Comic Sans MS', cursive, sans-serif;">
        <span style="color: #1E90FF;">Disney</span> 
        <span style="color: red; font-family: 'Arial', sans-serif;">Movie Recommendation System</span>
    </h1>
    """,
    unsafe_allow_html=True
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

movies = pickle.load(open('artifacts/movies.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox('Select a movie:', movie_list)

if st.button("Show Recommendations"):
    recommendations_movies = recommend(selected_movie)
    if recommendations_movies:
        for name in recommendations_movies:
            st.write(name)

st.markdown('</div>', unsafe_allow_html=True)
