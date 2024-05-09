# Import Libraries
import tkinter as tk
import speech_recognition as sr
from openai import OpenAI
import pygame
from pathlib import Path
import langdetect

# Initialize OpenAI client
client = OpenAI(api_key='YOUR_API_KEY')

# Function to translate text
def translate():

    # Get text and target language from input fields
    text = text_entry.get("1.0", "end-1c")
    target_language = language_entry.get()

    # Request translation from OpenAi GPT-3 model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a language translator"},
            {"role": "user", "content": text},
            {"role": "assistant", "content": f"Translate '{text}' to {target_language}"}
        ]
    )

    # Get translation from response
    translation = response.choices[0].message.content

    # Set Translation text in GUI
    set_translation_text(translation)

    # Convert translation to speech and play audio
    tts(translation)

# Function to play MP3 file
def play_mp3(file_path):

    # Initialize pygame
    pygame.init()

    # Load the MP3 file
    pygame.mixer.music.load(file_path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the MP3 to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Quit pygame
    pygame.quit()

# Funciton to convert text to speech
def tts(translation):

    # Create path for speech file
    speech_file_path = Path(__file__).parent / "speech.mp3"

    # Request speech synthesis from OpenAI tts model
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=translation
    )

    # Save audio to file
    with open("tts.mp3", "w") as file:
        pass

    response.stream_to_file("tts.mp3")

    # Play audio
    play_mp3("tts.mp3")


# Function to convert speech to text
def speech_to_text():

    # Initialize pygame
    pygame.mixer.init()

    # PLay sound to indicate start of voice recognition
    pygame.mixer.music.load("ding.wav")
    pygame.mixer.music.play()

    # Clear text entry field
    text_entry.delete("1.0", tk.END)

    recognizer = sr.Recognizer()
    
    # Use microphone as audio source
    with sr.Microphone() as source:

        # Adjust for ambient sound
        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        # Listen for audio input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Recognize speech using google speech recognition
        text = recognizer.recognize_google(audio)

        # Detect spoken language
        detected_lang = langdetect.detect(text)

        print("Detected Language: ", detected_lang)

        # Insert recognized text into text entry field
        text_entry.insert(tk.END, text,detected_lang)  
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Request error; {0}".format(e))

# Function to play translated audio
def play_translated_audio():
    play_mp3("tts.mp3")

# Function to set translation text
def set_translation_text(translation):
    translation_text.delete(1.0, tk.END)
    translation_text.insert(tk.END, translation)
    

# Create a Tkinter window
window = tk.Tk()
window.title("Text Translator")

# Set window size
window.geometry("600x400")

# Text entry for input
text_label = tk.Label(window, text="Enter Text:")
text_label.pack()
text_entry = tk.Text(window, height=10,width=50, wrap="word", font=("Helvetica", 15))
text_entry.pack()

# Language entry for target language
language_label = tk.Label(window, text="Enter target language:")
language_label.pack()
language_entry = tk.Entry(window)
language_entry.pack()

# Button to trigger translation
translate_button = tk.Button(window, text="Translate", command=translate)
translate_button.pack()

# Button for speech input
speech_button = tk.Button(window, text="Speech Input", command=speech_to_text)
speech_button.pack()

# Button to play translated audio
play_audio_button = tk.Button(window, text="Play Translated Audio", command=play_translated_audio)
play_audio_button.pack()

# Text widget to display translation
translation_text = tk.Text(window, wrap="word", height=3, width=50, font=("Helvetica", 15))
translation_text.pack()

# Start the GUI main loop
window.mainloop()
