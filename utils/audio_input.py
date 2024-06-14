import speech_recognition as sr
import keyboard

def get_audio_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Press and hold the F9 key to start listening...")
    keyboard.wait('F9')
    print("Listening...")

    with mic as source:
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from the service.")
        return None
