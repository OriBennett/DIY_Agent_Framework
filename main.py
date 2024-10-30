


from agents.agent import Agent
from models.model_service import ModelService
from models.openai_models import OpenAIModel
from models.ollama_models import OllamaModel
from tools.basic_calculator import basic_calculator
from tools.reverser import reverse_string


tools = [basic_calculator, reverse_string]


# Uncoment below to run with OpenAI
# model_service = OpenAIModel
# model_name = 'gpt-3.5-turbo'
# stop = None

# Uncomment below to run with Ollama
# model_service = OllamaModel
# model_name = 'llama3:instruct'
# stop = "<|eot_id|>"

#uncomment below to run with any AI
model_service = ModelService
model_name = "groq"
stop = None



agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

while True:
    prompt = input("Ask me anything: ")
    if prompt.lower() == "exit":
        break

    agent.work(prompt)
