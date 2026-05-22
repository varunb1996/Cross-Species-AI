import os
import librosa
from tqdm import tqdm

from embedding_tool import generate_embedding
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# -----------------------------------
# QDRANT CONFIG
# -----------------------------------

COLLECTION_NAME = "animal_sounds"

client = QdrantClient(path="qdrant_storage")

from qdrant_client.models import VectorParams, Distance

# Create collection if not exists
collections = client.get_collections().collections

collection_names = [c.name for c in collections]

if COLLECTION_NAME not in collection_names:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )

    print(f"Created collection: {COLLECTION_NAME}")

# -----------------------------------
# AUDIO ROOT
# -----------------------------------

AUDIO_ROOT = "data/audio"

# -----------------------------------
# INGEST
# -----------------------------------

points = []

point_id = 0

for species in os.listdir(AUDIO_ROOT):

    species_folder = os.path.join(AUDIO_ROOT, species)

    if not os.path.isdir(species_folder):
        continue

    print(f"\nProcessing species: {species}")

    for file in tqdm(os.listdir(species_folder)):

        if not file.endswith((".wav", ".mp3")):
            continue

        file_path = os.path.join(species_folder, file)

        try:

            # Load audio
            audio, sr = librosa.load(
                file_path,
                sr=16000
            )

            # Generate embedding
            embedding = generate_embedding(audio, sr)

            # Store point
            point = PointStruct(
                id=point_id,
                vector=embedding.tolist(),
                payload={
                    "species": species,
                    "file_name": file,
                    "path": file_path
                }
            )

            points.append(point)

            point_id += 1

        except Exception as e:

            print(f"Failed on {file}")
            print(e)

# -----------------------------------
# UPLOAD TO QDRANT
# -----------------------------------

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print("\nDone ingesting audio!")
print(f"Total files stored: {len(points)}")