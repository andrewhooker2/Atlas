from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid

import config

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

    my_collection = "my-collection"

    try:
        first_collection = qdrant_client.recreate_collection(
            collection_name=my_collection,
            vectors_config=models.VectorParams(size=config.openai_vector_dimension, distance=models.Distance.COSINE)
        )
        print("Creating a Collection ... ")
        print("Collection Name: ", first_collection)
    except Exception as e:
        print(f"Error: {e}")

    # Might try this:
    # client.create_collection(
    #     collection_name="{collection_name}",
    #     vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE),
    # )


def create_points_batch(embedding, message_id):
    uuid_value = uuid.uuid4()
    qdrant_client.upsert(
        collection_name=config.qdrant_collection,
        points=models.Batch(
            ids=uuid_value,
            vectors=embedding.tolist()
        )
    )


def create_point(embedding, point_id, message_id):
    uuid_value = uuid.uuid4()

    print("Embedding: ")
    print(embedding)

    qdrant_client.upsert(
        collection_name=config.qdrant_collection,
        points=[
            models.PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "response_id": message_id
                }
            )
        ]
    )


def temp_create_point(embedding, point_id, message_id, ai_response):
    uuid_value = uuid.uuid4()

    qdrant_client.upsert(
        collection_name=config.qdrant_collection,
        points=[
            models.PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "response_id": message_id,
                    "message": ai_response
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
        score_threshold=0
    )

    print(search)
