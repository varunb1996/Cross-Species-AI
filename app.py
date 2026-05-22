import streamlit as st
import librosa
import soundfile as sf
import tempfile
import numpy as np

from tools.embedding_tool import generate_embedding
from tools.retrieval_tool import search_similar

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Cross-Species Communication Intelligence System",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🐋 Cross-Species Communication Intelligence System")

st.markdown("""
AI system for:

- Animal sound understanding
- Semantic similarity search
- Cross-species vocal clustering
- Audio embedding analysis
""")

# -----------------------------------
# AUDIO UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Animal Audio",
    type=["wav", "mp3"]
)

# -----------------------------------
# PROCESS AUDIO
# -----------------------------------

if uploaded_file is not None:

    st.subheader("Uploaded Audio")

    st.audio(uploaded_file)

    # Save temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:

        tmp_file.write(uploaded_file.read())

        temp_audio_path = tmp_file.name

    # Load audio
    audio, sr = librosa.load(
        temp_audio_path,
        sr=16000
    )

    st.success("Audio loaded successfully!")

    # -----------------------------------
    # GENERATE EMBEDDING
    # -----------------------------------

    embedding = generate_embedding(audio, sr)

    st.success("Embedding generated successfully!")

    # -----------------------------------
    # SEARCH SIMILAR
    # -----------------------------------

    results = search_similar(embedding)

    st.success("Similarity search completed!")

    # -----------------------------------
    # SHOW RESULTS
    # -----------------------------------

    st.header("🔎 Similar Sounds")

    for idx, result in enumerate(results):

        st.subheader(f"Result {idx + 1}")

        st.write(f"Species: {result['species']}")

        st.write(f"Similarity Score: {result['score']:.4f}")

        st.write(f"Audio File: {result['file_name']}")

        # Play similar audio
        try:

            with open(result["path"], "rb") as audio_file:

                audio_bytes = audio_file.read()

            st.audio(audio_bytes)

        except Exception as e:

            st.warning(f"Could not load audio: {e}")

    # -----------------------------------
    # EMBEDDING INFO
    # -----------------------------------

    st.header("📊 Embedding Information")

    st.write(f"Embedding Dimension: {len(embedding)}")

    st.write("First 10 Embedding Values:")

    st.write(np.array(embedding[:10]))