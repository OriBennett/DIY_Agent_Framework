import os
from typing import Tuple
from dotenv import load_dotenv
import openai
from groq import Groq

load_dotenv()

class LlmFactory:
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._openai4t = None
        self._openai35 = None
        self._groq = None
        self._local_llama3 = None
        self._local_mistral = None
        
    def get_llm(self, llm_logic_name: str) -> Tuple[openai.OpenAI, str]:
        if (llm_logic_name == "openai4t"):
            if (self._openai4t is None):
                self._openai4t = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            return self._openai4t, "gpt-4-turbo"
        
        if (llm_logic_name == "openai35"):
            if (self._openai35 is None):
                self._openai35 = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            return self._openai35, "gpt-3.5-turbo-0125"
        
        if (llm_logic_name == "groq"):
            if (self._groq is None):
                self._groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
            return self._groq, "llama-3.1-70b-versatile"
        
        if (llm_logic_name == "local_llama3"):
            if (self._local_llama3 is None):
                self._local_llama3 = openai.OpenAI(base_url=os.getenv('LOCAL_BASE_URL', "http://localhost:11434/v1"), api_key="not-needed")
            return self._local_llama3, "llama3"
        
        # if we got here use default
        if (self._local_mistral is None):
            self._local_mistral = openai.OpenAI(base_url=os.getenv('LOCAL_BASE_URL', "http://localhost:11434/v1"), api_key="not-needed")
        return self._local_mistral, "mistral"
        


    

