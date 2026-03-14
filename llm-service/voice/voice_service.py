"""
voice_service.py

Handles speech recognition and text-to-speech.
Supports English, Telugu, and Hindi.
"""

import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import uuid
import time

recognizer = sr.Recognizer()


def listen_to_user():
    """
    Capture voice input from microphone
    """

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    # Try multiple languages
    languages = ["en-IN", "te-IN", "hi-IN"]

    for lang in languages:

        try:
            text = recognizer.recognize_google(audio, language=lang)

            print("You said:", text)

            return text

        except:
            continue

    return ""


def speak_response(text, lang="en"):
    """
    Convert text response to speech
    """

    filename = f"voice_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=text, lang=lang)

    tts.save(filename)

    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()

    pygame.mixer.quit()

    time.sleep(0.3)

    os.remove(filename)