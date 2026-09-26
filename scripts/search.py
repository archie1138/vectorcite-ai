import sys
from ingestion.embedder import  load_vector_store


def search(query : str, k : int = 4) :
    vector_store = load_vector_store()

    results = vector_store.similarity_search_with_score(query=query, k=k)

    for (doc, score) in results : 
        print(f"# Score : {score} \n## Page num : {doc.metadata['page_num']} \n### Content : {doc.page_content}")




if __name__ == "__main__" :
    query = sys.argv[1] if len(sys.argv) > 1 else "tell about character function giving examples"
    search(query=query)