import datetime
import os
import smtplib
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyautogui as pg


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
terminate = ['close', 'end', 'bye', 'terminate', 'turn off', 'quit']
days = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday',
        4: 'thursday', 5: 'friday', 6: 'saturdaay'}
t_o = {'Sai Charan': 'ksaicharanreddy2002@gmail.com',
       'Yashwanth': 'yashwanthravulapally@gmail.com',
       'Geethika': 'geethikareddyjinna@gmail.com',
       }
contact = {'Sai Charan': '+919676606241',
           'Yashwanth': '+919392336430',
           'Geethika': '+919866840542',
           }
global query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
        print("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
        print("Good Evening sir!")
    return speak("I am your PersonalAssistant Please tell me how may I assist you")


def tell_me_time():
    now = datetime.datetime.now().time()
    hr = datetime.datetime.now().hour
    if hr < 12:
        speak(f'it is morning and the time is{datetime.datetime.now().hour}{int(datetime.datetime.now().minute)} a m')
        print(f'it is morning and the time is{datetime.datetime.now().hour}:{int(datetime.datetime.now().minute)} am')
    elif hr > 12 and hr < 16:
        speak(
            f'it is afternoon and the time is {int(datetime.datetime.now().hour) - 12} {int(datetime.datetime.now().minute)} p m')
        print(
            f'it is afternoon and the time is {int(datetime.datetime.now().hour) - 12}:{int(datetime.datetime.now().minute)} pm')
    else:
        speak(f'it is evening and the time is {datetime.datetime.now().hour}{int(datetime.datetime.now().minute)} p m')
        print(f'it is evening and the time is{datetime.datetime.now().hour}:{int(datetime.datetime.now().minute)} pm')


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        time.sleep(3)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query


def take_query():
    while True:
        global query
        query = takeCommand()
        query = query.lower()
        print(query)
        if "open" in query:
            # query=query.replace('open','opening')
           speak(query)
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kiradamsaicharanreddy2002@gmail.com', 'ApplicationDevelopment2022')
    server.sendmail('kiradamsaicharanreddy2002@gmail.com', t_o[person], content)
    server.close()


def display_date():
    m = {1: 'january', 2: 'febrauary', 3: 'march', 4: 'april', 5: 'may', 6: 'june',
         7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    yr = int(datetime.datetime.now().year)
    mon = int(datetime.datetime.now().month)
    too_day = datetime.datetime.now().day
    speak(f'The date is {too_day} of {m[mon]} {yr} ')
    print(f'The date is {too_day} of {m[mon]} {yr} ')


def open_browser():
    webbrowser.open("www.google.com")


def search_results(query):
    query = query.replace("search", "")
    speak(f'opening {query}')
    global url
    url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq=" + (
        str(query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)
    
    #     pywhatkit.playonyt(query1)


if __name__ == "__main__":
    wishMe()
    while True:
        take_query()
        if 'open youtube' in query:
            speak('what do you want to open:')
            take_query()
            url = "https://www.youtube.com/=" + str(query)
            print(query)
            time.sleep(5)
            webbrowser.open_new(url)
            speak('opeining youtube')
            print('opening youtube')
        elif 'open google' in query:
            open_browser()
            print('opening google')
        elif 'close google' in query:
            os.system("taskkill /im chrome.exe /f")
        elif query == 'open tab':
            tab_res = take_query()
            webbrowser.open_new_tab(tab_res)
        elif 'time' in query:
            tell_me_time()
        elif query in terminate:
            speak('ok sir.. i will take a leave')
            print('ok sir.. i will take a leave')
            break
        elif query == "send mail":
            speak('to whom do you want to send mail: ')
            person = input("enter ?")
            print(person)
            to = t_o[person].lower()
            speak('enter the content')
            content = input("enter ?")
            sendEmail(to, content)
            speak('mail sent successfully')
        elif query != 'none' and 'search' in query:
            search_results(query)
        if query == 'who made you':
            speak('i was made by saicharan')
            print('i was made by saicharan')
        elif query == 'are you single':
            speak('i am in relationship with wifi')
        # elif 'play' in query:
        #     speak('what do you like me to play')
        #     query1=takeCommand()
        #     play_songs(query1)

        elif 'date' in query:
            display_date()
        elif 'send message' in query:
            speak("Choose the contact")
            person = takeCommand()
            speak('enter the hour')
            hr = int(input('enter the hour 24 format:'))
            speak('enter the minute')
            mi = int(input("enter the minute:"))
            pywhatkit.sendwhatmsg(contact[person], 'This is an automated message sent from saicharan"s machine',hr, mi)
            pg.press('esc')
            pg.press('enter')

        elif 'minimise' in query:
            pg.hotkey('win', 'down')
        elif 'close app' in query:
            speak('closing application')
            pg.hotkey('alt', 'f4')
        elif 'shift' in query:
            speak('ok..sir')
            pg.hotkey('alt', 'tab')
        elif 'copy' in query:
            pg.hotkey('ctrl', 'c')
            speak('copied')
        elif 'paste' in query:
            pg.hotkey('ctrl', 'v')
            speak('Done sir')
        elif 'cut' in query:
            pg.hotkey('ctrl', 'x')
        elif 'screen' in query:
            pg.hotkey('win', 'PrtScr')
            speak('Took screen shot sir...')
            print('Took screen shot sir...')
        elif 'open application' == query:
            speak('which application do you want to open me sir')
            app = takeCommand()
            if 'ide' in app:
                os.startfile(r"C:\Users\kirad\eclipse\java-2022-03\eclipse\eclipse.exe")
                speak('opening eclipse ide sir..')
                print('opening eclipse ide sir..')
            elif 'notepad' == app:
                os.system('notepad.exe')
                speak('opening notepad sir..')
                print('opening notepad sir..')
            elif 'Paint' in app:
                os.startfile('%windir%\\system32\\mspaint.exe')
                speak('opening paint')
                print('opening paint')
            elif 'server' in app:
                os.startfile(r'C:\\xampp\\xampp-control.exe')
                speak('opening xampp server')
            elif 'Notepad plus plus' == app:
                os.startfile(r"C:\\Program Files\\Notepad++\\notepad++.exe")
                speak('opening notepad plus plus')

            elif 'team' in app:
                os.startfile(r"C:\Program Files\TeamViewer\TeamViewer.exe")
                speak('opeining teamviewer')
            elif 'Word' in app:
                os.system('start winword')
                speak('opeining word sir..')
            elif 'Power point' in app:
                os.system('start powerpnt')
                speak('opeing power point sir..')
                print('opeing power point sir..')
            elif 'Excel' in app:
                os.system('start excel')
                speak('opeing excel sir..')
                print('opeing excel sir..')
            elif 'this PC' in app:
                pg.hotkey('win', 'e')
                speak('opeining my computer')
                print('opeining my computer')
            elif 'Brave' in app:
                os.startfile(r"C:\Users\kirad\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe")
                speak('opening brave')
                print('opening brave')
            elif 'code' in app:
                os.startfile(r"C:\Users\kirad\OneDrive\Desktop\Visual Studio Code.lnk")
                speak('opeining vscode')
                print('opeining vscode')
            elif 'Xd' in app:
                os.startfile(r"C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe")
            elif 'Edge' in app:
                os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                speak('opeing Edge')
                print('opeing Edge')
            elif 'Dev' in app:
                os.startfile(r"C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
                speak('opening Dev c plus plus')
                print('opening Dev c plus plus')

            else:
                speak("The application you are trying to open is not available or removed")
                print("The application you are trying to open is not available or removed")
