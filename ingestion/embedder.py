import os
from pathlib import Path
from uuid import uuid4
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

load_dotenv()

QDRANT_PATH = "./qdrant_db" 
COLLECTION_NAME = "vectorCite_docs"
VECTOR_SIZE = 3072

def get_embeddings() : 
    embeddings = GoogleGenerativeAIEmbeddings(
        model='gemini-embedding-2-preview',
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )

    return embeddings


def create_vector_store(chunks, path : str = QDRANT_PATH) :
    embeddings = get_embeddings()

    # Creating the Directory (ignores if already Directory exists)
    Path(path).mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=path)

    existing_collections = [c.name for c in client.get_collections().collections]

    if COLLECTION_NAME  not in existing_collections :
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
        )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )

    uuids = [str(uuid4()) for _ in range(len(chunks))]
    vector_store.add_documents(documents=chunks, ids=uuids)

    print(f"Stored {len(chunks)} chunks in Qdrant database at path : {path}")
    return vector_store 


def load_vector_store(path : str = QDRANT_PATH) :

    embeddings = get_embeddings()
    client = QdrantClient(path=path)

    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )


if __name__ == '__main__' :
    from ingestion.loader import load_docs_from_directory
    from ingestion.chunker import chunk_documents

    docs = load_docs_from_directory("./data")
    chunks = chunk_documents(docs)
    create_vector_store(chunks=chunks)