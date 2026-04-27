# 🎬 ML Movie Recommender

A content-based movie recommendation system built with Python and Machine Learning that suggests similar movies based on genres.

## 🚀 Demo
Type any movie name and get 10 similar movie recommendations instantly!

## 🧠 How It Works
1. Loads the MovieLens dataset (9742 movies)
2. Converts movie genres into numbers using TF-IDF
3. Calculates similarity between all movies using Cosine Similarity
4. Returns top 10 most similar movies

## 🛠️ Tech Stack
- **Python** — core language
- **Pandas** — data loading and processing
- **Scikit-learn** — TF-IDF and cosine similarity
- **Streamlit** — web interface

## 📦 Installation

1. Clone the repo
git clone https://github.com/yourusername/ml-movie-recommender

2. Install dependencies
pip install pandas scikit-learn streamlit

3. Download the MovieLens dataset
https://grouplens.org/datasets/movielens/latest/
Place movies.csv and ratings.csv in the project folder

4. Run the app
streamlit run app.py

## 📁 Project Structure
ml-movie-recommender/
├── app.py              # Streamlit web UI
├── recommender.py      # ML recommendation engine
├── movies.csv          # Movie dataset
├── ratings.csv         # Ratings dataset
└── README.md

## 🎯 Features
- Search any movie by name
- Case insensitive search
- Handles movies not in dataset gracefully
- Modern glassmorphism UI
- Top 10 recommendations
