import speech_recognition as sr

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.9
        audio=r.listen(source)

        try:
            ask=r.recognize_google(audio, language='en-us')
            print(f"you said : {ask}")
        except Exception:
            print("Say tht again...")
            return ""
        return ask
    command()