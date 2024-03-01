from openai.types.chat import ChatCompletion
from qdrant_client import QdrantClient
from qdrant_client.http import models
from embedding import gen_embedding
from datetime import datetime
import typing
import config
import uuid

# Set up your client
qdrant_client = QdrantClient(
    url=config.qdrant_url,
    api_key=config.qdrant_api_key,
)


def collection_status():
    collection_info = qdrant_client.get_collection(collection_name=config.qdrant_collection)
    list(collection_info)


def create_collection():
    vectors_config = models.VectorParams(
        size=config.openai_vector_dimension,
        distance=models.Distance.COSINE
    ),

    try:
        first_collection = qdrant_client.recreate_collection(
            collection_name=config.qdrant_collection,
            vectors_config=models.VectorParams(size=config.openai_vector_dimension, distance=models.Distance.COSINE)
        )
    except Exception as e:
        print(f"Collection Creation Error: {e}")


def create_points_batch(conversation: typing.List[typing.Dict[str, str]]):
    try:
        points = []
        for item in conversation:
            # Using this for a filler for now
            embedding = [.01]
            # Check for embedding in the message
            if item['role'] == 'system':
                continue
            if 'embedding' not in item and item['role'] != 'system':
                embedding = gen_embedding(item['content'])

            points.append(
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "role": item['role'],
                        "message": item['content'],

                    },
                )
            )
        test = qdrant_client.upsert(
            collection_name=config.qdrant_collection,
            points=points
        )

    except Exception as e:
        print(f"Collection Batching Error: {e}")


def create_point(embedding: list[float], response: ChatCompletion):
    qdrant_client.upsert(
        collection_name=config.qdrant_collection,
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "message": response.choices[0].message.content,
                    "role": response.choices[0].message.role,
                    "time": datetime.now(),
                }
            )
        ]
    )


def search_similar_vectors(embedding):
    search = qdrant_client.search(
        collection_name=config.qdrant_collection,
        query_vector=embedding,
        with_vectors=False,
        with_payload=True,
        score_threshold=0.8
    )
    return search
