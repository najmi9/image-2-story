# Image Story Teller

A simple web application that generates a story from an uploaded image. Built with Streamlit and Huggingface.

## Features

- Upload an image and get a story generated based on the image.
- The story is also converted to speech, which you can listen to directly from the app.

## How It Works

1. The uploaded image is processed to generate a caption using the Salesforce's `blip-image-captioning-base` model.
2. The generated caption is then used as a context to create a short story using Google's PALM API.
3. The generated story is converted to speech using the `espnet/kan-bayashi_ljspeech_vits` model.

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/najmi9/image-2-story
```

2. Navigate to the project directory:

```bash
cd image-2-story
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory and add the following:

```
UPLOAD_FOLDER=path_to_upload_directory
PALM_API_KEY=your_palm_api_key
```

Replace `path_to_upload_directory` with the path where you want to save uploaded images and `your_palm_api_key` with your actual PALM API key.

5. Run the Streamlit app:

```bash
streamlit run main.py
```

## Usage

1. Open the provided URL in your web browser.
2. Upload an image using the file uploader.
3. Wait for the story to be generated and listen to the audio.

## Credits

- Developed by [Imad Nami](https://twitter.com/najmi_imad)
- Source code available on [Github](https://github.com/najmi9/image-2-story)

## Models Used

- Image to text: [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- Text to story: [Google PALM API](https://makersuite.google.com/)
- Text to speech: [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits)
