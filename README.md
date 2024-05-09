# AI-Language-Translator

This is a simple language translator application built using Python and Tkinter GUI toolkit. It utilizes the OpenAI GPT-3 model for text translation and synthesis and the Google Speech Recognition API for speech-to-text conversion.

## Features

- Translate text from one language to another using OpenAI GPT-3 model.
- Convert translated text into speech using OpenAI TTS model.
- Recognize speech input from microphone and convert it to text.
- Play translated text as audio.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages can be installed via pip:
  - tkinter
  - speech_recognition
  - openai
  - pygame
  - langdetect
- In 'translator.py' replace 'YOUR_API_KEY' with a valid OpenAI api key

## Usage

1. Run the `translator.py` file to launch the application.
2. Enter the text you want to translate in the "Enter Text" field.
3. Specify the target language in the "Enter target language" field.
4. Click on the "Translate" button to translate the text.
5. To input text via speech, click on the "Speech Input" button and speak into the microphone.
6. Click on the "Play Translated Audio" button to listen to the translated text as audio.
7. The translation will be displayed in the text widget located at the bottom of the gui.

## Credits

- This application utilizes the OpenAI GPT-3 and TTS models for text translation and synthesis.
- Speech recognition is performed using the Google Speech Recognition API.
- The GUI is built using the Tkinter library in Python.
