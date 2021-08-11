import pyttsx3
import pyaudio
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import time
import numpy as np
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from youtube_search import YoutubeSearch
import smtplib
import subprocess
import json
import requests
from googlesearch import search
from datetime import date
from PyDictionary import PyDictionary
from covid import Covid
import pyjokes
# import wolframalpha
#sapi5 is a microsoft voice recognition tool
engine=pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# Set 0 for male 1 for female
engine.setProperty('voice',voice[0].id)

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#can also combine with todo list for updates reminding

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir,Nice to see you again.")
        print("Good Morning Sir,Nice to see you again.")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir,Nice to see you again.")
        print("Good afternoon Sir,Nice to see you again.")
    else:
        speak("Good Evening Sir,Nice to see you again.")
        print("Good Evening Sir,Nice to see you again.")
    speak("I am Lucifer, Your Personal Assistant. How may I help you?")
    print("I am Lucifer, Your Personal Assistant. How may I help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Ok Sir,Let me recognize your command.")
        speak("Ok Sir,Let me recognize your command.")
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command: {query}\n")

    except Exception:
        # print(e)  
        # if exception as e then error will also be displayed.  
        print("Say that again Sir, please...") 
        speak("Say that again Sir,Please...") 
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for excuting tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia')
            print('searching wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)
        elif "can do" in query:
            print("Sir, I can open your favourite websites as well as search wikipedia for you. Not only this, I can also open softwares which you use like excel,visual studio,pycharm,calculator, and also search google and youtube for you. If there is something I dont know,Do let me know Sir") 
            speak("Sir, I can open your favourite websites as well as search wikipedia for you. Not only this, I can also open softwares which you use like excel,visual studio,pycharm,calculator, and also search google and youtube for you.If there is something I dont know,Do let me know Sir")  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            time.sleep(5)
        elif 'open google' in query:
            webbrowser.open("google.com")
            time.sleep(5)
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            time.sleep(5)
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            time.sleep(5)
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(5)
        elif 'open github' in query:
            webbrowser.open("github.com")
            time.sleep(5)
        elif 'open mail' in query:
            webbrowser.open("gmail.com")
            time.sleep(5)
        elif 'open internshala' in query:
            webbrowser.open("internshala.com")
            time.sleep(5)
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            time.sleep(5)
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            time.sleep(5)
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
            time.sleep(5)
        elif 'news' in query:
            speak('Here are some headlines from the News,Happy reading')
            webbrowser.open("ndtv.com")
            time.sleep(6)
        elif 'wish me again' in query:
            hour=int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Morning Sir,Nice to see you again.")
                print("Good Morning Sir,Nice to see you again.")
            elif hour>=12 and hour<18:
                speak("Good afternoon Sir,Nice to see you again.")
                print("Good afternoon Sir,Nice to see you again.")
            else:
                speak("Good Evening Sir,Nice to see you again.")
                print("Good Evening Sir,Nice to see you again.")
        elif 'date' in query:
            today = date.today() 
            print("Today date is: ", today) 
            speak(f"Today date is: {today}")
        elif 'play music' in query:
            print("opening spotify")
            speak("opeing soptify,Sir")
            os.system('start spotify')
            time.sleep(5)
        elif 'open notepad' in query:
            print("opening notepad")
            speak('opening notepad, Sir')
            time.sleep(5)
            os.system("start notepad")
        elif 'how are you' in query:
            speak("Absolutely Fine,Sir")
        elif 'who are you' in query:
            speak("I am a unique bird that lived for five or six centuries in the Arabian desert, after this time burning itself on a funeral pyre and rising from the ashes with renewed youth to live through another cycle.! HAHA")
            speak("Kidding ,I am just a simple desktop assistant to serve you,Sir")
        elif 'open command prompt' in query:
            print("opening Command Prompt")
            speak('opening Command Prompt, Sir')
            os.system("start cmd")
            time.sleep(5)
        elif 'open visual studio code' in query:
            print("opening VS code")
            speak('opening VS code, Sir')
            codePath = "C:\\Users\\punee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            time.sleep(5)
        elif 'open visual studio' in query:
            print("opening VS ")
            speak('opening Visual studio, Sir')
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)
            time.sleep(5)
        elif 'open pycharm' in query:
            print("opening Py Charm ")
            speak('opening Py charm, Sir')
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
            time.sleep(5)
        elif 'search google' in query:
            try:
                speak("What do want me to search,Sir")
                search=takeCommand()
                print("Searching...")
                speak("Sir,here are results which i found for you.")
                webbrowser.open(f'https://www.google.com/search?q= {search}')
                time.sleep(5) 
            except Exception as e:
                print(e)
                speak("Sorry Sir,Unable to search at this moment")
        elif 'the meaning' in query:
            try:
                speak("sure sir, which word")
                dictionary=PyDictionary()
                print (dictionary.meaning(takeCommand()))                
                speak(dictionary.meaning(takeCommand()))
                time.sleep(5)

            except Exception as e:
                speak("Try again,sir")                

        
        elif 'open Word' in query:
            print("opening Word ")
            speak('opening Word, Sir')
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
            time.sleep(5)
        elif 'open powerpoint' in query:
            print("opening Powerpoint ")
            speak('opening Powerpoint, Sir')
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
            time.sleep(5)
        elif 'open excel' in query:
            print("opening excel ")
            speak('opening excel, Sir')
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
            time.sleep(5)
        elif 'open calculator' in query:
            print("opening calculator ")
            speak('opening calculator, Sir')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            time.sleep(5)
        elif 'open wordpad' in query:
            print("opening wordpad ")
            speak('opening wordpad, Sir')
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
            time.sleep(5)
        elif 'covid report' in query:
            try:
                speak("Sir, Covid reports of which country?")
                print("Sir, Covid reports of which country?")
                covid=Covid()
                p=takeCommand()
                cases=covid.get_status_by_country_name(p)
                print("Sir, here are your desired reports")
                speak("Sir, here are your desired reports")
                for x in cases:
                    print(x,"-->",cases[x])
            except Exception as e:
                print("Sorry sir, please repeat")
                speak("Sorry sir, please repeat")

        # elif 'ask' in query:
        #     speak('I can answer to computational and geographical questions  and what question do you want to ask now')
        #     question=takeCommand()
        #     app_id="V4P7RP-JH4UUGH4X8"
        #     client = wolframalpha.Client('R2K75H-7ELALHR35X')
        #     res = client.query(question)
        #     answer = next(res.results).text
        #     speak(answer)
        #     print(answer)


        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke) 
            speak(My_joke) 
  

        elif 'weather' in query:
            try:
                speak("Sir,Weather of which city?")
                city_name= takeCommand()
                
                print(f"City Name: {city_name}\n")
                API_KEY="259d0008ecdc499a5b714ff60ac16c3c"
                
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                URL = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
                response = requests.get(URL)
# checking the status code of the request
                if response.status_code == 200:
   # getting data in the json format
                    data = response.json()
   # getting the main dict block
                    main = data['main']
   # getting temperature
                    temperature = main['temp']
   # getting the humidity
                    humidity = main['humidity']
   # getting the pressure
                    pressure = main['pressure']
   # weather report
                    report = data['weather']
                    print(f"{city_name:-^30}")
                    print(f"Temperature: {temperature}")
                    print(f"Humidity: {humidity}")
                    print(f"Pressure: {pressure}")
                    print(f"Weather Report: {report[0]['description']}")
                    speak(f"Sir,Weather of")
                    speak(f"{city_name:-^30}")
                    speak(f"Temperature: {temperature}")
                    speak(f"Humidity: {humidity}")
                    speak(f"Pressure: {pressure}")
                    speak(f"Weather Report: {report[0]['description']}")
            except Exception as e:
                speak("Sorry,HTTP error")
                print(e)
                

        # elif 'locate number' in query:
        #     phone_number1 = phonenumbers.parse("+918567805002")
        #     print(phone_number1)
        #     print(geocoder.description_for_number(phone_number1,'en'))
        #     print(carrier.name_for_number(phone_number1,'en')) 
        #     phone_number2 = phonenumbers.parse("+918567805002")
        #     print(geocoder.description_for_number(phone_number2,'en'))

        elif 'shut up' in query:
            print("Sir,That was rude. CALM DOWN")
            speak("Sir,That was rude. CALM DOWN")
        # elif 'I am Punjabi' in query:
            # speak("If you are punjabi, then I am also assistant of a punjabi. BEWARE")
        elif 'are you with me' in query:
            print("Till the time you dont terminate me,Sir")
            speak("Till the time you dont terminate me,Sir")
        elif 'search youtube' in query:
            try:
                speak("What do you want to search on youtube,sir")
                results=takeCommand()
                speak("Here is what i found")
                print("RESULTS:")
                webbrowser.open(f"https://www.youtube.com/results?search_query={results}")
                time.sleep(5)
            except Exception as e:
                print(e)
                speak("Sir,there was an error")





        # enable first settings of gmail by using less secure acess then try sending email
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "to@gmail.com"    
                sendEmail(to, content)
                print("Your request to send an email to you has been completed. Please verify!")
                speak("Your request to send an email to you has been completed. Please verify!")
            except Exception as e:
                print(e)
                print("Sorry Sir, There was an error in sending an email. Email sending FAILED")
                speak("Sorry Sir, There was an error in sending an email. Email sending FAILED")
        


        elif ('bye' or 'quit' or 'exit') in query:
            print("Goodbye Sir,Takecare and Have a nice time . Hope to see you soon")
            speak("Goodbye Sir,Takecare and Have a nice time . Hope to see you soon")
            break

        else:
            print("Sorry sir, The command given by you is not supported. I will make sure it will also be available soon")
            speak("Sorry sir, The command given by you is not supported. I will make sure it will also be available soon")
        



