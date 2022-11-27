import os
import time

import pyautogui
from datetime import datetime
import translators as ts
import speech_recognition as sr
import datetime
from gtts import gTTS
from playsound import playsound
import requests
from kamala_translator import kamala_talk_de, kamala_talk_cn
import home_automation
from PIL import Image

# crypto currency api
crypto_api = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin&vs_currencies=usd'


# converts speech to text
def kamala_listen():
    # create reconiger
    listen = sr.Recognizer()
    # what we speak should be on a source
    with sr.Microphone() as mic:
        print('listening...')
        listener = listen.listen(mic)
        text = ''
        try:
            text = listen.recognize_google(listener)
        except sr.RequestError as re:
            print(re)
        except sr.UnknownValueError as uv:
            print(uv)
        except sr.WaitTimeoutError as we:
            print(we)
    text = text.lower()
    return text


# converts text to speech
def kamala_talk(text):
    # create audio file
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='en')
    # save file
    tts.save(file_name)
    # play file
    playsound(file_name)
    # remove file
    os.remove(file_name)


def translators(text, lang_listen):
    if lang_listen == 'china':
        kamala_talk_de(ts.google(text, from_language='en', to_language='cn'))
    if lang_listen == 'germany':
        kamala_talk_cn(ts.google(text, from_language='en', to_language='de'))


# take screenshot
def screenshot():
    screeshot = pyautogui.screenshot()
    save = "F:/"
    screeshot.save(save+"_screenshot.png")


def openscreenshot():
    filename = "F:/_screenshot.png"
    img = Image.open(filename)
    img.show(img)

# creating reply function based on input text
def kamala_reply(text):
    # small talk
    try:
        if 'kamala' in text or 'kamla' in text:
            if 'what' in text and 'name' in text:
                kamala_talk('my name is komola. and i am your personal assistant')

            # crypto information
            elif 'bitcoin' in text and 'price' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('The current price of bitcoin in USD is ' + str(crypto_json['bitcoin']['usd']))
            elif 'litecoin' in text and 'price' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('The current price of litecoin in USD is ' + str(crypto_json['litecoin']['usd']))
            elif 'ethereum' in text and 'price' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('The current price of ethereum in USD is ' + str(crypto_json['ethereum']['usd']))

            # basic talk
            elif 'time' in text:
                time = datetime.datetime.now().strftime('%I:%M %p')
                kamala_talk('Current time is ' + time)
            elif 'how are you' in text:
                kamala_talk('i am doing good. what about you?')
                small = kamala_listen()
                while 'good' in small:
                    kamala_talk('glad to hear')
                    break
            # home controll
            elif 'light' in text and 'on' in text:
                home_automation.led_on()
                kamala_talk('light turned on ')
            elif 'light' in text and 'off' in text:
                home_automation.led_off()
                kamala_talk('light turned off')
            elif 'fan' in text and 'on' in text:
                home_automation.fan_on()
                kamala_talk('fan turned on')
            elif 'fan off' in text:
                home_automation.fan_off()
                kamala_talk('fan turned off ')
            # screenshot
            elif 'screenshot' in text and 'take' in text:
                screenshot()
                kamala_talk('screenshot has been taken')
            elif 'open' in text and 'screenshot' in text:
                openscreenshot()
                kamala_talk('screenshot opened')
        # google translator
            elif 'translate' in text:
                kamala_talk('sure, what language you want to translate?')
                lang_listen = kamala_listen()
                print(lang_listen)
                while True:
                    while True:
                        if lang_listen == 'china':
                            kamala_talk('tell me what you want to translate')
                            break
                        if lang_listen == 'germany':
                            kamala_talk('tell me what you want to translate')
                            break
                        else:
                            kamala_talk('i dont speak with that language')
                            lang_listen = kamala_listen()
                    text_to = kamala_listen()
                    print(text_to)
                    if text_to != 'turn off translator':
                        translators(text_to, lang_listen)
                    else:
                        kamala_talk('translator is off. what else can i do for you?')
                        break
            # voice assistant shut down
            elif 'stop' in text:
                kamala_talk('it was pleasure to help you. i wish you a wonderful day')
            else:
                kamala_talk('excuse me i did not get that. can u please repeat it?')
    except UnicodeDecodeError as UN:
        print(UN)


# execution of voice assistant
def execution():
    kamala_talk('Hi i am your personal voice assistant. when you need me just call me with my name kamala')
    while True:
        listen_kamala = kamala_listen()
        print(listen_kamala)
        kamala_reply(listen_kamala)
        if 'kamala stop' in listen_kamala:
            break
