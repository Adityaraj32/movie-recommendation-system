import streamlit as st
import recommender

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }

    .stApp {
        background: linear-gradient(125deg, #0d0015, #00012b, #001a1a, #0d0015);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px 40px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px rgba(0, 255, 255, 0.1),
                    inset 0 0 80px rgba(255, 255, 255, 0.02);
    }

    .hero h1 {
        color: white;
        font-size: 52px;
        font-weight: 700;
        text-shadow: 0 0 30px rgba(0, 255, 255, 0.9),
                     0 0 60px rgba(0, 255, 255, 0.5),
                     0 0 100px rgba(0, 255, 255, 0.2);
        margin-bottom: 10px;
    }

    .hero p {
        color: rgba(180, 255, 255, 0.7);
        font-size: 17px;
        letter-spacing: 1px;
    }

    .stTextInput input {
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(10px) !important;
        color: white !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        border: 1px solid rgba(0, 255, 255, 0.25) !important;
        padding: 14px !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.08),
                    inset 0 0 20px rgba(255,255,255,0.02) !important;
    }

    .stButton button {
        background: rgba(0, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        color: cyan !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        width: 100% !important;
        padding: 14px !important;
        border: 1px solid rgba(0, 255, 255, 0.35) !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.15),
                    0 0 50px rgba(120, 0, 255, 0.1) !important;
    }

    .movie-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 18px 22px;
        border-radius: 16px;
        margin: 10px 0;
        color: white;
        font-size: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 3px solid cyan;
        box-shadow: 0 4px 24px rgba(0, 255, 255, 0.05),
                    inset 0 0 30px rgba(255, 255, 255, 0.01);
    }

    .results-header {
        color: cyan;
        font-size: 22px;
        font-weight: 600;
        margin: 20px 0 10px 0;
        text-shadow: 0 0 15px rgba(0, 255, 255, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommendator")
st.markdown("##### Find movies similar to your favourites")
movie_name = st.text_input("Enter the movie name: ").lower()

if st.button("🎯 Find Similar Movies"):
    recommendation = recommender.get_recommendations(movie_name)
    if recommendation is not None:
        st.markdown('<div class="results-header">🍿 Top 10 Picks For You</div>', 
            unsafe_allow_html=True)
        for i, movie in enumerate(recommendation):
                st.markdown(f'<div class="movie-card">#{i+1} &nbsp; 🎥 {movie}</div>', 
                unsafe_allow_html=True)
    else:
        st.warning("⚠️ Movie Not Found!")