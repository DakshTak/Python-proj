import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour >= 12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Friday Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone command as input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.pause_threshold = 0.5 #thoda aaram sai sunne ke liye
        r.energy_threshold = 300
        audio = r.listen(mic)

    try:
        print("Recognizing...")
        query = r.recognize_bing(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Pardon please. . .")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentence=1)
            
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'E:\\DAKSH\\My space\\my songs\\Ritviz'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open vscode' in query:
            vscode ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.stratfile(vscode)