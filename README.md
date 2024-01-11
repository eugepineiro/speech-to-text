# Speech To Text

## An Automatic Speech Recognition AI agent

Provides speech recognition from audio file

### Requirements
- Python 3 
- Dependecies in ```poetry.lock``` file
- Hugging Face / Open AI accounts, configure environment variables ```HUGGINGFACEHUB_API_TOKEN```/```OPENAI_API_KEY``` 

### Installation

#### Using Poetry
```bash
poetry install
```
NOTE: Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. In no case, it should be installed in the environment of the project that is to be managed by Poetry.

#### Or using pip 
```bash
$> pip install -r requirements.txt
```

### Execution 
```bash
python3 ./main.py
```