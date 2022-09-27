import speech_recognition as spr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

listener = spr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
        with spr.Microphone() as mic:
            print("listening....")
            listener.adjust_for_ambient_noise(mic, duration=0.1)
            voice = listener.listen(mic)
            command = ''
            try:
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
            except spr.UnknownValueError:
                talk('did not understand')
            except spr.RequestError:
                talk("Sorry")
            return command
def run_alexa(command):
        if 'alexa' in command:
            command = command.replace('alexa', '')
            if 'play' in command:
                song = command.replace('play', '')
                pywhatkit.playonyt(song)
            if 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is' + time)
            if 'how are you' in command:
                talk('i am fine')
            if 'tell me about' in command:
                try:
                    look_for = command.replace('tell me about', '')
                    info = wikipedia.summary(look_for, 1)
                    talk(info)
                except:
                    print("not found")
            if 'send whatsapp message' in command:
                pywhatkit.sendwhatmsg("+8801865099408", "Hi",12,25)        
            
while True:
    command = take_command()
    if 'shut down' in command:
                talk('shutting down')
                break    
    run_alexa(command)
