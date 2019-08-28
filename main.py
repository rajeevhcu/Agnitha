import speech_recognition as sr


def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something")
        audio = r.listen()
        print("Time over, Thank You!")

    try:
        print("Text" + r.recognize_google(audio, language='hi-IN'))
    except:
        pass


if __name__ == "__main__":
    speech()
