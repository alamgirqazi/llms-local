import requests
import json

url = 'http://localhost:11434/api/generate'

custom_prompt = 'Best football player at liverpool ?'
llm_model = 'llama3'  # mistral:7b, mistral:latest, llama2

data = {'model': llm_model,
        'prompt': custom_prompt,
        'stream': False
        }

# Making the POST request
result = requests.post(url, data=json.dumps(data))

result_text = result.text
data = json.loads(result_text)
print(data['response'])
