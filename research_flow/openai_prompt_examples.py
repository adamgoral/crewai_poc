import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')
model_name = os.getenv('OPENAI_MODEL_NAME')

def get_completion(prompt, model=model_name):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

prompt = input("Please enter a prompt: ")
print(get_completion(prompt))