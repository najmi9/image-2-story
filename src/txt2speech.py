from espnet2.bin.tts_inference import Text2Speech
import soundfile as sf
import random

def txt2speech(story: str) -> str :
    model = "espnet/kan-bayashi_ljspeech_vits"
    text2speech = Text2Speech.from_pretrained(model)

    wav = text2speech(story)['wav']
    random_number = random.randint(1, 100000)
    file_path = f"assets/audio-{random_number}.flac"
    sf.write(file_path, wav.numpy(), text2speech.fs, 'PCM_16')

    return file_path

"""
# another way to do it
import requests

def txt2speech(story: str) -> str :
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": story}

    response = requests.post(API_URL, headers=headers, json=payload)
    output =  response.content

    random_number = random.randint(1, 100000)
    file_path = f"assets/audio-{random_number}.flac"
    with open(file_path, "wb") as fp:
        fp.write(output)

    return file_path
"""
