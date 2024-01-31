import whisper
from audio_handler import *
from text_handler import save_to_file
# https://github.com/openai/whisper

AUDIO_PATH = "audios/BARBARA_ALICIA_ROJAS_ABURTO_2.MP3"

def transcribe(audio_file):
    return model.transcribe(f"{AUDIO_PATH}_trimmed_channel_2.mp3")


model = whisper.load_model("large")

result_agent = model.transcribe(f"{AUDIO_PATH}_trimmed_channel_2.mp3")

print(result_agent["text"])

save_to_file(result_agent["text"], "result.txt")