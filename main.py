import streamlit as st
from recommendation import load_models, get_recommendations
import pandas as pd
import plotly.graph_objects as go

df, cosine_sim = load_models()

st.set_page_config(page_title="Taylor Swift Music Recommender 🎵",page_icon="🎧", layout="wide")
st.title("🎶 Taylor Swift Mood-Based Music Recommender")

# Mood filter buttons
st.sidebar.header("🎧 Filter by Mood")
mood = st.sidebar.radio("Choose your mood:", [
    "All", "Happy 😊", "Sad 😢", "Dance 💃", "Chill 🧘", "Energetic 🔥",
])

filtered_df = df.copy()
if mood == "Happy 😊":
    filtered_df = df[df["valence"] > 0.7]
elif mood == "Sad 😢":
    filtered_df = df[df["valence"] < 0.3]
elif mood == "Dance 💃":
    filtered_df = df[df["danceability"] > 0.7]
elif mood == "Chill 🧘":
    filtered_df = df[(df["acousticness"] > 0.7) & (df["energy"] < 0.4)]
elif mood == "Energetic 🔥":
    filtered_df = df[df["energy"] > 0.8]

# Song selector
song_list = filtered_df["name"].unique().tolist()
song = st.selectbox("🎵 Select a Song", song_list)

if st.button("🔍 Show Recommendations"):
    recs = get_recommendations(song, df, cosine_sim)
    if len(recs):
        st.success("Here are your recommendations:")
        st.dataframe(recs)
    else:
        st.warning("Couldn't find recommendations for this song.")

# Radar chart for selected song
def plot_song_features(song_data):
    categories = ['acousticness', 'danceability', 'energy', 'speechiness',
                  'instrumentalness', 'liveness', 'valence']
    values = [song_data[col] for col in categories]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=song_data['name']
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        title=f"🎵 Audio Profile: {song_data['name']}"
    )
    return fig

song_row = df[df['name'] == song]
if not song_row.empty:
    st.plotly_chart(plot_song_features(song_row.iloc[0]))

# Show mood-filtered list
with st.expander("🎼 View All Songs in This Mood"):
    st.dataframe(filtered_df[["name", "album"]])