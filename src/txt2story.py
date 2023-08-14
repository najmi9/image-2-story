import google.generativeai as palm
from dotenv import load_dotenv
import os

def txt2story(context: str) -> str :
    load_dotenv()
    prompt = f"\
        You are a story teller\
        you can generate a short story based on the given simple narrative, the story must funny and understandable in 250 tokens.\
        CONTEXT: {context}\
        STORY:\
    "
    palm.configure(api_key=os.getenv('PALM_API_KEY'))
    response = palm.generate_text(prompt=prompt)
    result = response.result

    return result
