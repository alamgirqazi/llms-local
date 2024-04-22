import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'
custom_prompt = 'Best football player at liverpool ?'
llm_model = 'llama3'  # mistral:7b, mistral:latest, llama2


def api_response(custom_prompt):
    data = {'model': llm_model,
            'prompt': custom_prompt,
            'stream': False
            }
    result = requests.post(url, data=json.dumps(data))
    data = json.loads(result.text)

    return data['response']


ui = gr.Interface(
    fn=api_response,
    inputs=["text"],
    outputs=["text"],)


ui.launch()
