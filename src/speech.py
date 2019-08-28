import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something")
    audio = r.listen()
    print("Time over, Thank You!")

try:
    print("Text" + r.recognize_google(audio, language='hi-IN'))
except:
    pass
