# 🎵 Taylor Swift Mood-Based Music Recommender 🎤

This project is a **mood-based music recommendation system** built using **Streamlit**, focused entirely on **Taylor Swift's songs**. It allows users to explore and discover Taylor's discography based on their current mood, lyrical themes, or even a specific song.

## 🔍 Features

- 💫 **Mood-Based Filtering** – Get song recommendations based on lyrical sentiment and theme.
- 🔠 **Lyric Search** – Type in any Taylor Swift song and get similar tracks based on lyrical content.
- 🧠 **TF-IDF + Cosine Similarity** – Uses NLP techniques to match songs with similar lyrical meaning.
- 📊 **Interactive UI** – Streamlit-powered interface for a clean and easy-to-use experience.
- 💾 **Optimized Performance** – Uses `.pkl` files to speed up data loading and recommendations.

## 🛠️ Tech Stack

- Python 🐍  
- Pandas & Numpy 📊  
- Scikit-learn 🔍  
- NLTK 🧠  
- Streamlit 🌐  

## 📁 Project Structure

```
📁 music-recommender/
│
├── main.py              # Streamlit app UI
├── preprocess.py        # Data cleaning and preprocessing
├── recommendation.py    # Recommendation engine logic
├── data_cleaned.pkl     # Cleaned lyrics data
├── tfidf_matrix.pkl     # Precomputed TF-IDF matrix
├── cosine_sim_score.pkl # Precomputed similarity scores
└── spotify_millsongdata.csv # Dataset
```

## 📦 Dataset

Based on the `spotify_millsongdata.csv` dataset containing Taylor Swift's song lyrics, titles, artists, and links.