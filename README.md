# 🎵 Taylor Swift Mood-Based Music Recommender

An interactive **Streamlit app** that recommends Taylor Swift songs based on your mood or song preferences. It uses **TF-IDF** and **cosine similarity** to recommend similar songs and visualizes audio features with a **radar chart**.

---

## 🚀 Features

- 🎧 **Mood-based filtering** (Happy, Sad, Dance, Chill, etc.)
- 🔍 **Song-based recommendations** using text similarity
- 📊 **Radar chart visualization** of song audio features
- 💾 Uses `.pkl` files for fast loading (via `joblib`)

---

## 🗂️ Project Structure

```
music_recommender_project/
│
├── data/
│   └── taylor_swift_spotify.csv      # Your dataset (you add this)
│
├── models/
│   ├── data_cleaned.pkl              # Cleaned dataset
│   ├── tfidf_matrix.pkl              # TF-IDF feature matrix
│   └── cosine_sim_score.pkl          # Similarity scores
│
├── main.py                           # Streamlit app
├── preprocess.py                     # Preprocessing & model saving
├── recommendation.py                 # Recommendation logic
└── README.md                         # Project documentation
```

---

## 📥 Dataset

Copy your dataset file:
```
taylor_swift_spotify.csv
```
into the `data/` folder.

---

## ⚙️ Setup & Usage

### 1. 📦 Install Required Libraries

```bash
pip install streamlit pandas scikit-learn joblib plotly
```

### 2. 🧼 Preprocess Data (Only Once)

```bash
python preprocess.py
```

This will generate `.pkl` files in the `models/` folder.

### 3. 🚀 Run the App

```bash
streamlit run main.py
```

---

## 📊 Mood Filters Supported

| Mood             | Audio Feature Conditions                            |
|------------------|------------------------------------------------------|
| Happy 😊         | `valence > 0.7`                                      |
| Sad 😢           | `valence < 0.3`                                      |
| Dance 💃         | `danceability > 0.7`                                 |
| Chill 🧘         | `acousticness > 0.7` and `energy < 0.4`              |
| Energetic 🔥     | `energy > 0.8`                                       |
| Instrumental 🎻  | `instrumentalness > 0.5`                             |

---

## 📈 Visuals

- Radar chart compares audio features like `energy`, `danceability`, `valence`, etc.
- Interactive mood filtering and song selection UI.

---

## ✨ Credits

Developed by **Sri Ram M**  
Powered by: `Streamlit`, `scikit-learn`, `plotly`, `pandas`

---

## 📄 License

This project is for educational use only. All rights to original audio data belong to their respective copyright holders.