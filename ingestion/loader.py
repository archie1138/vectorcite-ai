from importlib import metadata
from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document

def load_docs_from_directory(dir_path : str) :
    documents = []

    for file_path in Path(dir_path).glob("*.pdf") :
        reader = PdfReader(file_path)

        for page in reader.pages :
            text = page.extract_text()

            if text : 
                documents.append(
                    Document(
                        page_content=text,
                        metadata={'source' : str(file_path), 'page_num' : page.page_number + 1}
                    )
                )

    print(f"Loaded {len(documents)} pages from {dir_path} ")
    return documents

    


if __name__ == "__main__" :
    docs = load_docs_from_directory('../data')

    for doc in docs[:3] :
        print(f"Source : {doc.metadata['source']}")
        print(f"Content Preview of page {doc.metadata['page_num']} : {doc.page_content[:200]}")


