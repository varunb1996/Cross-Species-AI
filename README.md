# 🐋 Cross-Species Communication Intelligence System

An AI-powered bioacoustic intelligence system for understanding and comparing animal vocalizations using transformer-based audio embeddings and vector similarity search.

---

# 🚀 Features

- Animal sound understanding
- Semantic similarity search
- Cross-species vocal clustering
- Transformer-based audio embeddings
- Qdrant vector database integration
- Streamlit interactive UI
- Real audio ingestion pipeline
- Upload custom animal audio files

---

# 🧠 Tech Stack

## AI / ML
- Transformers
- Wav2Vec2
- NumPy
- Librosa
- Scikit-learn

## Backend / Retrieval
- Qdrant Vector Database

## Frontend
- Streamlit

## Utilities
- Python
- tqdm

---

# 📂 Supported Species

Current dataset includes:

- Bird
- Cat
- Dog
- Lion

The system can easily be extended with additional species.

---

# ⚙️ How It Works

1. Audio is uploaded or loaded from dataset
2. Audio is resampled to 16kHz
3. Transformer model generates embeddings
4. Embeddings are stored in Qdrant
5. Similar sounds are retrieved using vector similarity search
6. Results are visualized in Streamlit

---

# 📊 Current Capabilities

- Semantic audio retrieval
- Cross-species sound comparison
- Embedding analysis
- Similarity scoring
- AI-powered bioacoustic indexing

---

# 🧩 Problems Solved During Development

- Sampling-rate mismatches
- Embedding pipeline refactoring
- Qdrant API compatibility issues
- Streamlit runtime errors
- Audio ingestion failures
- Payload formatting problems
- Vector retrieval debugging
- Dynamic upload support

---

# ▶️ Run the Project

## Install dependencies

```bash
pip install -r requirements.txt
```

## Ingest dataset

```bash
python -m tools.ingest_audio
```

## Launch Streamlit app

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

- Animal emotion classification
- Real-time audio streaming
- Multi-modal learning
- Spectrogram visualization
- LLM-powered interpretation
- Wildlife monitoring dashboard
- Audio clustering visualization

---

# 👨‍💻 Author

Varun Bukka

AI/ML Engineer | NLP | Computer Vision | Bioacoustics AI | Vector Databases
