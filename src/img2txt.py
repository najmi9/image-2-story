
from transformers import pipeline

def img2txt(url: str) -> str :
    model = "Salesforce/blip-image-captioning-base"
    task = "image-to-text"
    image_to_text = pipeline(task, model=model)
    response = image_to_text(url)
    text = response[0]['generated_text']
    return text
