import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor

torch.cuda.empty_cache()

device = "cuda" if torch.cuda.is_available() else "cpu"

model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium").to(device)
processor = WhisperProcessor.from_pretrained("openai/whisper-medium") # prepare the input speech into log-mel spctrograms.

inputs = processor.feature_extractor(next(iter(common_voice_es))["audio"]["array"], return_tensors="pt", sampling_rate=16_000).input_features.to("cuda")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="es", task="transcribe")

predicted_ids = model.generate(inputs, max_length=448, forced_decoder_ids=forced_decoder_ids)
processor.tokenizer.batch_decode(predicted_ids, skip_special_tokens=True, normalize=False)[0]