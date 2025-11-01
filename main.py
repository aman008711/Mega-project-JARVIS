import speech_recognition as sr
import  webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import wikipediaapi
import random
import JOKES
import os
from apps import apps



#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "45cc22d1ca024fda8676adfe305e7b43"

def speak(text):
    engine.say(text)
    engine.runAndWait()
wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="JarvisAssistant/1.0 (Aman; contact: amnk304086@gmail.com)"
)

def processCommand(c):
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
       speak("opening google")
    elif "open facebook" in c.lower():
       webbrowser.open("https://facebook.com")
       speak("opening facebook")
    elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
       speak("opening youtube")
    elif "open linkedIn" in c.lower():
       webbrowser.open("https://linkedIn.com")
       speak("opening LinkedIn")
    elif "open instagram" in c.lower():
       webbrowser.open("https://instagram.com")
       speak("opening instagram")
    elif "news" in c.lower():
        speak("Fetching latest news headlines...")
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        r = requests.get(url)
        data = r.json()
        # print(data)  # 🔍 Debug line to see what’s returned

        if data.get("status") == "ok":
            articles = data.get("articles", [])
            if articles:
                for article in articles[:5]:
                    title = article.get("title")
                    if title:
                        speak(title)
                        # print(title)
                        time.sleep(0.5)
            else:
                speak("No articles found. Try again later or change the country code.")
        else:
            msg = data.get("message", "Unknown error.")
            speak(f"News API error: {msg}")
            print("News API error:", msg)
    elif c.lower().startswith("play"):
        song_name = c[5:].strip().lower()  # "play " ke baad ka text
        found = False
        for key in musicLibrary.music:
            if key.lower() == song_name:
                webbrowser.open(musicLibrary.music[key])
                speak(f"Playing {key}")
                found = True
                break
        if not found:
         speak("Song not found in your library")

    # time and date queries
    elif "time" in c.lower():
        from datetime import datetime
        now = datetime.now()
        # format time like '07:45 PM'
        time_str = now.strftime("%I:%M %p")
        speak(f"The time is {time_str}")

    elif "date" in c.lower():
        from datetime import datetime
        today = datetime.today()
        # format date like 'Tuesday, October 28, 2025'
        date_str = today.strftime("%A, %B %d, %Y")
        speak(f"Today is {date_str}")

    elif "tell" in c.lower() and "joke" in c.lower():
        try:
            # Try to get a joke from the API
            response = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?safe-mode&type=single")
            if response.status_code == 200:
                joke_data = response.json()
                if joke_data.get("type") == "single":
                    speak(joke_data["joke"])
                else:
                    # If API fails or returns unexpected format, use fallback jokes
                    speak(random.choice(JOKES))
            else:
                speak(random.choice(JOKES))
        except Exception as e:
            # If any error occurs, use fallback jokes
            speak(random.choice(JOKES))

    #search wikipedia artificial intelligence
    elif "search wikipedia" in c.lower():
            query = c.lower().replace("search wikipedia", "").strip()
            if query:
                page = wiki.page(query)
                if page.exists():
                    # Get the first two sentences of the summary
                    summary = page.summary.split('. ')[:2]
                    summary = '. '.join(summary) + '.'
                    speak(f"According to Wikipedia: {summary}")
                else:
                    speak(f"Sorry, I couldn't find any Wikipedia article about {query}")
            else:
                speak("Please specify what you want to search on Wikipedia")
                
    elif "shutdown" in c.lower():
     speak("Shutting down your system, goodbye!")
     os.system("shutdown /s /t 5")   # /s = shutdown, /t 5 = 5 second delay
    
    
    elif "open" in c.lower():
     app_name = c.lower().replace("open", "").strip()

    found = False
    for key in apps.keys():
        if app_name in key.lower():  # partial match allowed
            speak(f"Opening {key}")
            try:
                os.startfile(apps[key])
            except Exception as e:
                speak("Sorry, I couldn't open it.")
                print("Error:", e)
            found = True
            break

if __name__ == "__main__":
    def verify_user():
        speak("Before starting, please tell me your name")
        try:
            with sr.Microphone() as source:
                print("Listening for name verification...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
                name = recognizer.recognize_google(audio)
                print(f"Name received: {name}")
                
                if name.lower() == "my name is aman":
                    speak("Identity verified. Welcome back, boss!")
                    return True
                else:
                    speak("Access denied. You are not authorized to use this system.")
                    return False
        except Exception as e:
            print(f"Error during name verification: {e}")
            speak("Sorry, I couldn't verify your name. Please try again.")
            return False

    def wish_me():
        hour = int(time.strftime("%H"))
        if hour < 12:
            greet = "Good Morning"
        elif hour < 18:
            greet = "Good Afternoon"
        else:
            greet = "Good Evening"
        speak(f"{greet}, Boss! I am Jarvis.")

    # First verify the user
    speak("Jarvis initializing...")
    if not verify_user():
        exit()
    
    # If verification successful, proceed with greeting
    wish_me()

    while True:
    #listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
           with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source, timeout=2, phrase_time_limit=2)
           word = r.recognize_google(audio)
           print(f"You said: {word}")
           if(word.lower() == "jarvis"):
               time.sleep(0.3)
               speak("Hello, BOSS")
               #listen for command
               with sr.Microphone() as source:
                   print("Jarvis Active...")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)
           
               processCommand(command)
                   

        except Exception as e:
            print("Error; {0}".format(e))

    

    
   






