import chromadb

client = chromadb.Client()
collection = client.create_collection("assistant_memory")

def save_memory(text):
    collection.add(
        documents=[text],
        ids=[str(len(collection.get()["ids"]))]
    )

def recall_memory(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results["documents"]
