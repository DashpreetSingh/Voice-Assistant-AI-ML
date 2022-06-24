import datetime
import os
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib

webbrowser.open("")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning sir ")
    elif 12 <= hour < 17:
        speak("good afternoon sir ")
    else:
        speak("good evening sir ")

    speak("pheonix online . please tell me how may i help you")


def takeCommand():
    # it take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kunalsingh6650@gmail.com', '@Kunalsingh1')
    server.sendmail('kunalsingh6650@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)
        # browser opening
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube ")

        elif 'google' in query:
            webbrowser.open("google.com")
            speak("opening google ")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook ")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("opening instagram ")

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak("opening github ")


        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            speak("opening whatsapp ")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow ")
        elif 'open youutubemusic' in query:
            webbrowser.open("youtubemusic.com")
            speak("opening youtubemusic ")

        # start TIME
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir, the time is {strTime}")
        # end time

        # EMAIL
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "kishankumar1234638" \
                     "@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("hii my friend i am phoenix. sorry kunal sir is not able to send the mail")
        # END EMAIL

        # SYSTEM APPLICATIONS
        elif 'open vs code' in query:
            codePath = "C:\\Users\\KUNAL SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open pycharm' in query:
            codePath1 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
            os.startfile(codePath1)

        elif 'open code blocks' in query:
            codePath2 = "C:\\Program Files\\codeBlocks\\codeblocks.exe"
            os.startfile(codePath2)

        elif 'open brave ' in query:
            codePath3 = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath3)
        elif 'open sql' in query:
            codePath4 = "C:\\Program Files (x86)\\Microsoft SQL Server\\120\\Tools\Binn\\anagementStudio\\Ssms.exe"
            os.startfile(codePath4)
        elif 'open idle' in query:
            codePath5 = "C:\\Program Files\\Python310\\ythonw.exe" "C:\\Program Files\\Python310\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath5)

        elif 'open microsoft edge' in query:
            codePath6 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath6)
        elif 'open visual studio' in query:
            codePath7 = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Professional\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath7)

    pass