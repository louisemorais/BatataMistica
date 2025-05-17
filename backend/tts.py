import pyttsx3


voice = pyttsx3.init()

voice.setProperty('language', 'pt-br')

def speak(text):
    # Define a voz
    voices = voice.getProperty('voices')
    for v in voices:
        if 'brazil' in v.languages:
            voice.setProperty('voice', v.id)
            break

    # Define a taxa de fala
    voice.setProperty('age', 6)
    voice.setProperty('rate', 200)

    # Fala o texto
    voice.say(text)
    voice.runAndWait()


