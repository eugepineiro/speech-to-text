import os
import openai
from openai import OpenAI

openai.api_key = os.environ["OPENAI_API_KEY"]

audio_file= open("audios/dalle.mp3", "rb")
transcript = OpenAI().audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)