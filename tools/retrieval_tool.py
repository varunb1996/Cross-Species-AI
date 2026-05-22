from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

import uuid

# Qdrant in-memory DB
client = QdrantClient(path="qdrant_storage")

COLLECTION_NAME = "species_vectors"

# Create collection
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE
    ),
)


def insert_embedding(
    embedding,
    metadata
):

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload=metadata
            )
        ]
    )


def search_similar(query_embedding):

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding.tolist(),
        limit=5
    )

    similarities = []

    for result in search_result.points:

        payload = result.payload

        similarities.append({
            "species": payload.get("species", "unknown"),
            "path": payload.get("path", ""),
            "score": result.score
        })

    return similarities