# A simple repo which shows you how you can run LLMs offline / locally on your laptop 

## Setup

#### Make sure you have ollama installed locally (https://ollama.com/)

`ollama run llama3` 

#### Setup Python environment

```
pipenv shell

pip install -r requirements.txt
```

#### There are three variants 

1. LLM with UI (Gradio)

```
python main.py
```

head over to [http://127.0.0.1:7860]

![LLM with UI (Gradio)](assets/gradio-screenshot.png)


2. LLM without UI (Console)
   
```
python run-without-ui.py
```

![LLM without UI (Console)](assets/console-screenshot.png)


3. Quite and Fast with Open WebUI (suggested)

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

head over to [http://127.0.0.1:3000]

![LLM with Open WebUI](assets/openwebui-screenshot.png)

