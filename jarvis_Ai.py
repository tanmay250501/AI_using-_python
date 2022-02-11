import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import requests
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshould = 1
        audio = r.listen(source,timeout = 5,phrase_time_limit=5)
        #audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


#to wish you
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir, please tell me how can i help you")

#to search on google
def search_on_google(query):
    kit.search(query)

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tkdsawwalakhe01@gmail.com', 'Tanmay@01')
    server.send_message('tkdsawwalakhe01@gmail.com', to, content)
    server.close()

#send whatsapp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

#play on youtube
def play_on_youtube(video):
    kit.playonyt(video)

#get a random joke
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]




if __name__ == "__main__":
    wish()
    #while True
    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "chrome" in query:
            apath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(apath)

        elif "open calculator" in query:
            cpath = "C:\\Windows\\System32\\calc.exe"
            speak("opening Calculator...")
            os.startfile(cpath)
            

        elif "open command prompt" in query:
            speak("opening command prompt")
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:                   
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music"  in query:
            music_dir = "C:\\project_music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        
        elif "search on wikipedia" in query:
            speak("What should i search on wikipedia , sir?")
            query = takecommand().lower()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takecommand().lower()
            search_on_google(query)
            
            
        elif "open youtube" in query:
            speak("Opening youtube...")
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            speak("Opening Facebook...")
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            speak("Opening Instagram...")
            webbrowser.open("www.instagram.com")

        elif "open brave" in query:
            bpath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            speak("Opening Brave...")
            os.startfile(bpath)

        elif "open google" in query:
            speak("What should i search on google, Sir.")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takecommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "play on youtube" in query:
            speak('What do you want to play on Youtube, sir?')
            video = takecommand().lower()
            play_on_youtube(video)

        elif "email" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "sawwalakhetanmay@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Tanmay")

            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send this email.")

        elif "joke" in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "thanks" in query:
            speak("thanks for choosing me as your personal assistant sir, have a good day.")
            sys.exit()

    
        speak("sir, do you have any other work?")
        