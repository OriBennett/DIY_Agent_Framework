# DIY_Agent_Framework
an LLM agent framework built from the ground up

You can ask it basic prompts using a local LLM, Groq or OpenAi (and is extensible to more LLMs easily):
![basic prompt](https://github.com/user-attachments/assets/b4250c7a-9b16-4830-bad2-f5e225953d21)

The modles can use tools:
![tool use](https://github.com/user-attachments/assets/df87d38f-c2ae-48f8-8ab7-05687e0eef58)
I've included 2 tools, a reverser and a calculator.

This is an agent framework, it can also chain calls:
![can chain calls](https://github.com/user-attachments/assets/07afff2f-9c52-4f74-88b5-5f77d142b191)


Installation instructions in Bash:

Create a virtual environment:
python -m venv .venv

Activate the virtual environment:
source .venv/Scripts/activate

Install dependancies:
pip install -r requirements.txt

Add a .env file and add your Groq API key: GROQ_API_KEY = gsk_... (you can get a Groq key here: https://console.groq.com/keys)

Run main.py:
python main.py


If you want to use a different LLM, you can uncomment the relavent section in main.py
