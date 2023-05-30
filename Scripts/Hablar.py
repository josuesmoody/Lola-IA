# - Speaking
# Must Install Pyaudio,Pyttsx3

def Hablar(audio):
    import pyttsx3
    fuente = pyttsx3.init('sapi5')
    voces = fuente.getProperty('voices')
    fuente.setProperty('voces',voces[0].id)
    fuente.setProperty('rate',190)
    print(f": {audio}")
    fuente.say(audio)
    fuente.runAndWait()
