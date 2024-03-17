import pyttsx3 #text to speech conversion library
import speech_recognition as sr
import datetime #tells us current date and time
import pyaudio

engine = pyttsx3.init('sapi5') #microsoft speech api
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<17:
        speak("Good afternoon")

    elif hour>=17 and hour<23:
        speak("Good evening")

    else:
        speak("Good night")
    speak("I am Robin, how may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User siad: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__ == '__main__':
    speak("Hi Aashita nice to see you")
    wishMe()
    takeCommand()

    #logic for executing tasks based on query