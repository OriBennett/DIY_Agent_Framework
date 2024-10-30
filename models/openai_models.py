import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

class OpenAIModel:
    def __init__(self, model, system_prompt, temperature):
        self.model_endpoint = 'https://api.openai.com/v1/chat/completions'
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }


    def generate_text(self, prompt):

        payload = {
                    "model": self.model,
                    "response_format": {"type": "json_object"},
                    "messages": [
                        {
                            "role": "system",
                            "content": self.system_prompt
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False,
                    "temperature": self.temperature,
                }
        
        response = requests.post(
            self.model_endpoint, 
            headers=self.headers, 
            data=json.dumps(payload))
        
        response_json = response.json()
        response = json.loads(response_json['choices'][0]['message']['content'])

        print(F"\n\nResponse from OpenAI model: {response}")

        return response