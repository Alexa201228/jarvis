from datetime import datetime

import speech_recognition as sr
from random import choice

from speech_engine import speak
from utils import opening_text


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='ru-ru')
        if not 'стоп' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night miss, take care!")
            else:
                speak('Have a good day miss!')
            exit()

    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query
