import torch
import librosa

from transformers import Wav2Vec2Processor
from transformers import Wav2Vec2Model


# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

processor = Wav2Vec2Processor.from_pretrained(
    "facebook/wav2vec2-base-960h"
)

model = Wav2Vec2Model.from_pretrained(
    "facebook/wav2vec2-base-960h"
)


# ---------------------------------------------------
# GENERATE EMBEDDING
# ---------------------------------------------------

def generate_embedding(audio, sr):

    # Convert audio to mono if needed
    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)

    # Resample to 16kHz
    audio_16k = librosa.resample(
        audio,
        orig_sr=sr,
        target_sr=16000
    )

    # Prepare inputs
    inputs = processor(
        audio_16k,
        sampling_rate=16000,
        return_tensors="pt",
        padding=True
    )

    # Generate embedding
    with torch.no_grad():

        outputs = model(**inputs)

    embedding = outputs.last_hidden_state.mean(dim=1)

    return embedding.squeeze().numpy()