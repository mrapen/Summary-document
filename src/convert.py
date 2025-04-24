from langchain_community.document_loaders import (
    TextLoader, UnstructuredPDFLoader, UnstructuredHTMLLoader,
    Docx2txtLoader
)

def convert_to_text(file_path):
    """The function converts a document file to text"""
    file_type = file_path.split('.')[-1]

    if "pdf" == file_type:
        loader = UnstructuredPDFLoader(file_path)
        document = loader.load()
    elif "txt" == file_type:
        loader = TextLoader(file_path)
        document = loader.load()
    elif "html" == file_type:
        loader = UnstructuredHTMLLoader(file_path)
        document = loader.load()
    elif "doc" == file_type or "docx" == file_type:
        loader = Docx2txtLoader(file_path)
        document = loader.load()
    else:
        return []
    return document

