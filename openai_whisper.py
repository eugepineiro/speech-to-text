import whisper
# https://github.com/openai/whisper
model = whisper.load_model("large")
result = model.transcribe("audios/dalle.mp3")
print(result["text"])