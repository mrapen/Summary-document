import pypandoc
import PyPDF2

def ConvertToText(file_path) -> list[str]:
    
    file_type = file_path.split('.')[-1]

    if "pdf" == file_type:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        document = [page.extract_text().lower() for page in pdf_reader.pages]
    else:
        document = pypandoc.convert_file(file_path, "plain").split("\f")
    
    return document
