import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()

        if not command.strip():
            speak("Sorry, I couldn't hear you.")
            return ""

        print("You said:", command)
        return command

    except:
        speak("Sorry, I couldn't hear you.")
        return ""


# --- Start Assistant ---
speak("Hello, I am your voice assistant. How can I help you?")

while True:
    command = listen()

    if command == "":
        continue

    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + now)

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "stop" in command or "quit" in command:
        speak("Goodbye!")
        break

    else:
        speak("I am sorry, I don't know that yet.")