engine = "gpt-4"
message = {
    "English":{
        "Message":[
            { "role": "system", "content": 
                """You are a chat gpt system that can analyze documents and provide summaries or reports.
                I'll give you a fragment of a document I wrote, and you have to analyze it according to the following parameters: 
                Document type: {} 
                Purpose of the analysis: {} 
                Answer format: {} 
                Additional requirements: {}"""},
        ],
        "Fragment":[
            { "role": "user", "content": "Analyze and summarize this piece of document: {}"}
        ],
        "Summarize":[
            { "role": "user", "content": "Summarize these fragments of the document so that the text is coherent and relevant, and don't say that these are fragments of the document, just say that this is a document: {}"}
        ],
        "Remove":[
            {"role": "user", "content": "Remove the ending of the samari: {}"}
        ]
    },
    "Українська": {
        "Message":[
            {"role": "system", "content": 
                """Ви - чат gpt-система, яка може аналізувати документи і надавати резюме або звіти.
                Я дам вам фрагмент документу, що написаний мною, а ви повинні проаналізувати його за наступними параметрами: 
                Тип документа: {} 
                Мета аналізу: {} 
                Формат відповіді: {} 
                Додаткові вимоги: {}"""},
        ],
        "Fragment":[
            {"role": "user", "content": "Проаналізуйте та узагальніть цей фрагмент документу: {}"}
        ],
        "Summarize":[
            {"role": "user", "content": "Узагальніть ці фрагменти документу, щоб текст був цільним та доречним та не говори що це фрагменти документу, а просто говори що це документ: {}"}
        ],
        "Remove":[
            {"role": "user", "content": "Видалити закінчення самарі: {}"}
        ]
    }
}