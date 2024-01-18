from jiwer import wer
from text_handler import *

WHISPER_TRANSCRIPT_PATH = 'transcripts/dalle_whisper.txt'
MANUAL_TRANSCRIPT_PATH = 'transcripts/dalle_manual.txt'

with open(WHISPER_TRANSCRIPT_PATH) as agent_file:
    whisper_output = agent_file.readlines()

with open(MANUAL_TRANSCRIPT_PATH) as manual_file:
    manual_transcript = manual_file.readlines()

print(whisper_output[0])
print(manual_transcript[0])

word_error_rate = wer(manual_transcript, whisper_output)
print(word_error_rate)

word_error_rate_cleaned = wer(remove_all(manual_transcript), remove_all(whisper_output))
print(word_error_rate_cleaned)