from llm_factory import LlmFactory
import json

class ModelService:
    def __init__(self, model, system_prompt, temperature=0, stop=None):
        """
        Initializes the model with the given parameters.

        Parameters:
        model (str): The name of the model to use.
        system_prompt (str): The system prompt to use.
        temperature (float): The temperature setting for the model.
        stop (str): The stop token for the model.
        """
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.stop = stop

    def generate_text(self, prompt):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        brain, model_name = LlmFactory.instance().get_llm(self.model)
        response = brain.chat.completions.create(
            model= model_name,
            messages=messages,
            response_format= {"type": "json_object"},
            timeout=10000,
            temperature=self.temperature,
            stream= False,
        )
        response_content = response.choices[0].message.content
        print(f"Response from {self.model}: {response.choices[0].message.content}")
        # Convert response content to JSON object
        try:
            json_response = json.loads(response_content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

        return json_response

        