# Must Install SpeechRecognition
# Must Install PyAudio (required for microphone input)

import locale
import speech_recognition as sr

def Escuchar():
    locale.setlocale(locale.LC_ALL, 'es_ES')
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Escuchando... ")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 3)

    try:
        print(": Reconociendo... ")
        query = r.recognize_google(audio, language='es-ES')
        print(f": Tu comando: {query}\n")

    except:
        return ""

    return query.lower()
