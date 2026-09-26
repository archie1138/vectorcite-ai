from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=512, chunk_overlap=100) :

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)

    for chunk_index, chunk in enumerate(chunks) :
        chunk.metadata["chunk_index"] = chunk_index ; 

    print(f"Split {len(documents)} pages into {len(chunks)} chunks")
    return chunks



if __name__ == '__main__' :
    from ingestion.loader import load_docs_from_directory 

    docs = load_docs_from_directory("./data")
    all_chunks = chunk_documents(documents=docs) 

    if all_chunks : 
        for chunk in all_chunks[:5] :
            print(f"Content preview of chunk {chunk.metadata['chunk_index']} : {chunk.page_content[:200]}")
            print(f"Chunk Source : {chunk.metadata['source']}")

