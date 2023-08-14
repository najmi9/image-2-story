
from app.src.img2txt import img2txt
from app.src.txt2speech import txt2speech
from app.src.txt2story import txt2story

def img2story(image_path: str)-> str:
    text = img2txt(image_path)
    story = txt2story(text)
    filepath = txt2speech(story)
    return filepath
