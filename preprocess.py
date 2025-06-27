import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

def clean_data(csv_path, save_dir='models'):
    df = pd.read_csv(csv_path).dropna()
    df['text'] = df['name'] + " " + df['album']
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['text'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    os.makedirs(save_dir, exist_ok=True)
    joblib.dump(df, f"{save_dir}/data_cleaned.pkl")
    joblib.dump(tfidf_matrix, f"{save_dir}/tfidf_matrix.pkl")
    joblib.dump(cosine_sim, f"{save_dir}/cosine_sim_score.pkl")

if __name__ == "__main__":
    clean_data("data/taylor_swift_spotify.csv")