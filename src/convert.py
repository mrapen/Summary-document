import pypandoc
import PyPDF2

def split_text(text: str, max_length=7000):
    
    chunks = []
    current_chunk = ""
    for word in text.split(" "):
        if len(current_chunk) + len(word) < max_length:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    return chunks

def ConvertToText(file_path) -> list[str]:
    
    file_type = file_path.split('.')[-1]

    if "pdf" == file_type:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\f"
        document = split_text(text)
    elif "txt" == file_type:
        with open(file_path) as f:
            lines = f.readlines()
        document = split_text(lines)
    else:
        document = split_text(pypandoc.convert_file(file_path, "plain"))
    
    return document
