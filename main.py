from tkinter import *
from webbrowser import register
import mysql.connector
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from functools import partial
from PIL import Image
import time
import subprocess

#connecting to the database
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="umesh123",
database="logindb"
)

a = {'VOIX':'virtualbysakshi@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
window = Tk()
global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password') # email id - use any email id whose security/privacy is off
    server.sendmail('email id', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning ") 
        window.update()
        speak("Good Morning !")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon !")
        window.update()
        speak("Good Afternoon !")
    else:
        var.set("Good Evening ")
        window.update()
        speak("Good Evening !")
    speak("Hello, Myself voix! How may I help you ") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.dynamic_energy_adjustment_damping=0.15
        audio = r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn1.configure(bg = 'purple')
    wishme()
    while True:
        btn1.configure(bg = 'purple')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye.Have a productive day")
            btn1.configure(bg = '#800080')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye.Have a productive day")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=5)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set("sorry couldn't find any results")
                    window.update()
                    speak("sorry couldn't find any results")

        elif 'browser' in query:
            var.set('opening '+query[5:])
            window.update()
            speak('opening '+query[5:])
            print(query)
            mycursor = mydb.cursor()
            command=query
            command=command.replace("on","")
            command=command.replace("browser","")
            print(command)
            mycursor.execute("SELECT id FROM commands WHERE command='"+command+"'")
            result=mycursor.fetchall()
            print(result)
            mydb.commit()
            str1 = ''
            for item in result:
                str1 = str1 + str(item)
            print(str1[1:3])
            id=str1[1:3]
            mycursor.execute("SELECT ans FROM commands WHERE id='"+id+"'")
            result=mycursor.fetchall()
            mydb.commit()
            str2 = ''
            for item in result:
                str2 = str2 + str(item)
            str3=str2.replace("(","") 
            str3=str3.replace(")","")
            str3=str3.replace(",","")
            str3=str3.replace("'","")        
            print(str3)
            webbrowser.open(str3)
      
        elif 'on youtube search' in query:
            var.set('opening youtube')
            window.update()
            speak('opening youtube')
            command=query[17:]
            strr=command.replace(" ","+")
            webbrowser.open("https://www.youtube.com/results?search_query="+strr)

        elif 'hello' in query:
            var.set('Hello I am Digitally Expert Voice Assistant Designed for Personalized Automation but u can call me VOIX ')
            window.update()
            speak("Hello I am Digitally Expert Voice Assistant Designed for Personalized Automation but u can call me VOIX.")

        elif 'play music' in query:
            window.update()
            command=query[11:]
            strr=command.replace(" ","-")
            songstr="https://gaana.com/song/"+strr
            print(songstr)
            webbrowser.open(songstr)

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome")
            window.update()
            speak("Welcome")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you . tell me whatever you want to perform ')
            window.update()
            speak('I can do multiple tasks for you . tell me whatever you want to perform ')

        elif 'old are you' in query:
            var.set("I am ancient,I am infinite")
            window.update()
            speak("I am ancient,I am infinite")

        elif 'your name' in query:
            var.set("Myself Digitally Expert Voice Assistant Designed for Personalized Automation but u can call me VOIX.")
            window.update()
            speak('myself Digitally Expert Voice Assistant Designed for Personalized Automation but u can call me VOIX.')

        elif 'application' in query:
            var.set('opening '+query[5:])
            window.update()
            speak('opening '+query[5:])
            mycursor = mydb.cursor()
            command=query
            command=command.replace("application","")
            print(command)
            mycursor.execute("SELECT id FROM commands WHERE command='"+command+"'")
            result=mycursor.fetchall()

            mydb.commit()
            str1 = ''
            for item in result:
                str1 = str1 + str(item)
            print(str1[1:3])
            id=str1[1:3]
            mycursor.execute("SELECT ans FROM commands WHERE id='"+id+"'")
            result=mycursor.fetchall()
            mydb.commit()
            str2 = ''
            for item in result:
                str2 = str2 + str(item)
            str3=str2.replace("(","") 
            str3=str3.replace(")","")
            str3=str3.replace(",","")
            str3=str3.replace("'","")        
            print(str3)
            path = str3
            os.startfile(path)
        elif 'stopwatch' in query:
            second = 0    
            minute = 0    
            hour = 0  
            var.set("Stopwatch has been started")
            window.update()
            speak("Stopwatch has been started")  
            while(True):       
                print('\t\t\t\t-------------')    
                print('\t\t\t\t  %d : %d : %d '%(hour,minute,second))    
                print('\t\t\t\t-------------')    
                time.sleep(1)    
                second+=1    
                if(second == 60):    
                    second = 0    
                    minute+=1    
                if(minute == 60):    
                    minute = 0    
                    hour+=1;    
                os.system('cls')    

        elif 'email to me' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = "How are you??"
                to = a['nehuf02@gmail.com']
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry! I wasn't able to send this email")
                window.update()
                speak("Sorry! I wasn't  able to send this email")

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)
    
    

def mainwindow():
    label2 = Label(window, textvariable = var1, bg = '#00CC99')
    label2.config(font=("Courier", 20))
    var1.set('User Said:')
    label2.pack()

    label1 = Label(window, textvariable = var, bg = '#734f96')
    label1.config(font=("Courier", 20))
    var.set('Welcome')
    label1.pack()
    global frames
    frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
    window.title('VOIX')
    global label
    label = Label(window, width = 500, height = 500)
    label.pack()
    window.after(0, update, 0)

    global btn0 
    btn0= Button(text = 'WISH ME',width = 20, command = wishme, bg = '#99FFFF')
    btn0.config(font=("Courier", 12))
    btn0.pack()
    global btn1
    btn1 = Button(text = 'START',width = 20,command = play, bg = '#99FFFF')
    btn1.config(font=("Courier", 12))
    btn1.pack()
    global btn2
    btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#99FFFF')
    btn2.config(font=("Courier", 12))
    btn2.pack()
    global btn3
    btn3 = Button(text = 'ADD Command',width = 20, command = run, bg = '#99FFFF')
    btn3.config(font=("Courier", 12))
    btn3.pack()

connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="umesh123",database="logindb")
cursordb = connectiondb.cursor()
def run():
    os.system('python addcmd.py')
mainwindow()
window.mainloop() 


