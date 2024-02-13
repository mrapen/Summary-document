import g4f

def SummarizeWithGPT(document: list[str], document_type: str, analysis_purpose: str, response_format: str, additional_requirements: str)->str:
    
    if len(document) == 0 or document_type == "" or analysis_purpose == "" or response_format == "" or additional_requirements == "":
        return

    summary = ""

    for n in range(len(document)):
        page = document[n]
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 
                f"""Ви - чат gpt-система, яка може аналізувати документи і надавати резюме або звіти.
                Я дам вам написаний мною документ, а ви повинні проаналізувати його за наступними параметрами: 
                Тип документа: {document_type} 
                Мета аналізу: {analysis_purpose} 
                Формат відповіді: {response_format} 
                Додаткові вимоги: {additional_requirements}"""},
                {"role": "user", "content": f"Проаналізуйте та узагальніть цей документ: {page}"},
                ],
        )
        for part in response:
            summary += part
        summary += "\n"
    
    return summary
    
