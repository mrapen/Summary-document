from g4f.client import Client
import src.config as cfg
import copy
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity


class Summarization:
    """This class is only for summarizing documents using AI"""
    def __init__(self):
        # self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.client = Client()

    def summarize_with_ai(self, document,
                        additional_requirements: str,
                        prompt_lang: str)->str:
    
        if len(document) == 0 or additional_requirements == "":
            return ""

        summary_frag = ""

        messsage = { "role": "user", "content": "{}"}

        fragment = cfg.message[prompt_lang]["Fragment"]
        for chunk in document:
            msg = copy.deepcopy(messsage)
            msg["content"] = msg["content"].format(fragment.format(chunk.page_content))
            response = self.client.chat.completions.create(
                model=cfg.model,
                messages=[msg],
                stream=True,
                web_search=False
            )
            summary_frag += response.choices[0].message.content + "\f"
        
        summary = cfg.message[prompt_lang]["Summarize"]
        msg = copy.deepcopy(messsage)
        msg["content"] = msg["content"].format(summary.format(summary_frag, additional_requirements))
        response = self.client.chat.completions.create(
            model=cfg.model,
            messages=[msg],
            stream=True,
            web_search=False
        )

        return response.choices[0].message.content
    
