import os
from langchain_community.llms.openai import OpenAI
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings
import src.config as cfg

class Summarization:
    """This class is only for summarizing documents using AI"""
    def __init__(self):
        if os.environ.get("OPENAI_API_KEY"):
            OpenAI.openai_api_key = os.environ.get("OPENAI_API_KEY")
        elif os.path.exists("api_key.txt"):
            with open("api_key.txt", "r", encoding="utf-8") as f:
                OpenAI.openai_api_key = f.read().strip()
        else:
            raise ValueError("OPENAI_API_KEY is not set and api_key.txt is not found")
        self.splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=1000,
            chunk_overlap=200
        )
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large"  # або інша доступна модель
        )
        # Ініціалізація LLM для сумаризації
        self.llm = OpenAI(model_name=cfg.model ,temperature=0)
        
    def summarize_with_ai(self, document,
                        additional_requirements: str,
                        prompt_lang: str)->str:

        if len(document) == 0:
            return ""

        split_docs = self.splitter.split_documents(document)
    
        # Індексування усіх шматків у FAISS
        vectorstore = FAISS.from_texts(
            [doc.page_content for doc in split_docs],
            self.embeddings
        )
        # Перетворимо на retriever для подальшого пошуку
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    

        # Отримуємо релевантні документи (тут просто всі кращі k=5)
        docs_to_summarize = retriever.get_relevant_documents("")

        fragment_summary_template = cfg.message[prompt_lang]["Fragment"]

        map_prompt = PromptTemplate(
            template=fragment_summary_template,
            input_variables=["text"]
        )

        overall_summary_template = cfg.message[prompt_lang]["Summarize"]

        if additional_requirements == "":
            combine_prompt = PromptTemplate(
                template=overall_summary_template,
                input_variables=["summaries"]
            )
            chain = load_summarize_chain(
                self.llm,
                chain_type="map_reduce",
                map_prompt=map_prompt,
                combine_prompt=combine_prompt,          
                token_max=1500
            )
        else:
            overall_summary_template += cfg.message[prompt_lang]["Additional"].format(additional_requirements)
            combine_prompt = PromptTemplate(
                template=overall_summary_template,
                input_variables=["summaries"]
            )
            chain = load_summarize_chain(
                self.llm,
                chain_type="map_reduce",
                map_prompt=map_prompt,
                combine_prompt=combine_prompt,          
                token_max=1500
            )
        # Запускаємо ланцюг сумаризації
        return chain.run(docs_to_summarize)    