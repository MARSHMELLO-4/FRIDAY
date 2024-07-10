import speech_recognition as sr
import pyaudio 
import setuptools
import pyttsx3
import webbrowser
import musiclibrary
import openai
from openai.error import RateLimitError

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text : str):
    engine.say(text)
    engine.runAndWait()

def processcommand(c): #c is str here 
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower() :
        webbrowser.open("https://www.youtube.com/")
    elif "open whatsapp" in c.lower() :
        webbrowser.open("https://web.whatsapp.com/") 
    elif c.lower().startswith("play"):
        song = c.lower.split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        speak("i dont know the command")
    
def defineaiprocess(command):
    openai.api_key = "sk-proj-pdPGNQWGtJcip2lI1EnKT3BlbkFJoGywRFgUeVRwn593eyjR"

    try:
        # Generate a chat completion
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": command}
            ]
        )

        # Print the response
        return completion.choices[0].message['content']

    except RateLimitError as e:
        print("Rate limit exceeded. Please check your plan and billing details.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    speak("initializing jarvis.....")
    #wait for the word jarvis
    # obtain audio from the microphone
    while True :
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,timeout = 2.0,phrase_time_limit=1)

            # recognize speech using google 
            print("recognizing...")

            print("jarvis thinks you said " + r.recognize_google(audio))
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("yess tell me how can i help you !!")
                #listen for the command
                with sr.Microphone() as source:
                    print("jarvis is activated .... ")
                    audio = r.listen(source,timeout = 5.0,phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    print("jarvis thinks you said " + command)
                    processcommand(command)

        except Exception as e:
            print("ERROR:{0}".format(0))