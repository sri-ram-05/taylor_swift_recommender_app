import joblib

def load_models(model_dir='models'):
    df = joblib.load(f"{model_dir}/data_cleaned.pkl")
    cosine_sim = joblib.load(f"{model_dir}/cosine_sim_score.pkl")
    return df, cosine_sim

def get_recommendations(song_name, df, cosine_sim, top_n=5):
    idx = df[df['name'].str.lower() == song_name.lower()].index
    if idx.empty:
        return []
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return df.iloc[[i[0] for i in sim_scores]][['name', 'album', 'popularity']]