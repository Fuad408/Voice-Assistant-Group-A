import os
import speech_recognition as sr
import datetime
from gtts import gTTS
from playsound import playsound
import requests
from kamala_translator import kamala_talk_de, kamala_talk_cn
import translators as ts


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
            text = listen.recognize_google(listener, language="bn-BD")
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
    tts = gTTS(text=text, lang='bn')
    # save file
    tts.save(file_name)
    # play file
    playsound(file_name)
    # remove file
    os.remove(file_name)


def translators(text, lang_listen):
    if lang_listen == 'চীন ভাষা':
        kamala_talk_de(ts.google(text, from_language='bn', to_language='cn'))
    if lang_listen == 'জার্মানি':
        kamala_talk_cn(ts.google(text, from_language='bn', to_language='de'))


# creating reply function based on input text
def kamala_reply(text):
    # small talk
    try:
        if 'কমলা' in text or 'কমলার' in text:
            if 'ি' in text and 'নাম' in text:
                kamala_talk('আমার নাম কমলা। এবং আমি তোমার ব্যাক্তিগত ভয়েস সহকারী। ')
            # crypto information
            elif 'বিট কয়েন' in text or 'বিটকয়েন' in text and 'মূল্য' in text or 'দাম' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('মার্কিন ডলারে বিটকয়েনের বর্তমান মূল্য' + str(crypto_json['bitcoin']['usd']))
            elif 'লাইট কয়েন' in text and 'মূল্য' in text or 'দাম' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('আমেরিকান ডলারে লাইট কয়েনের বর্তমান মূল্য' + str(crypto_json['litecoin']['usd']))
            elif 'ইথেরিয়াম' in text and 'মূল্য' in text or 'দাম' in text:
                response = requests.get(crypto_api)
                crypto_json = response.json()
                kamala_talk('আমেরিকান ডলারে ইথেরিয়ামের বর্তমান মূল্য ' + str(crypto_json['ethereum']['usd']))
            elif 'বাজে' in text:
                time = datetime.datetime.now().strftime('%I:%M %p')
                kamala_talk('বর্তমান সময় হচ্ছে' + time)

            # google translator
            elif 'অনুবাদ' in text:
                kamala_talk('অবশ্যই, তোমি কোন ভাষায় অনুবাদ করতে চাও ?')
                lang_listen = kamala_listen()
                while True:
                    while True:
                        if lang_listen == 'চীন ভাষা':
                            kamala_talk('তোমি কি অনুবাদ করতে চাও আমাকে বলো')
                            break
                        if lang_listen == 'জার্মানি':
                            kamala_talk('তোমি কি অনুবাদ করতে চাও আমাকে বলো')
                            break
                        else:
                            kamala_talk('আমি এই ভাষায় কথা বলি না দয়া করে অন্য ভাষা বলো ')
                            lang_listen = kamala_listen()
                    text_to = kamala_listen()
                    if text_to != 'অনুবাদ বন্ধ করো' or text_to != 'কমলা অনুবাদ বন্ধ করো ':
                        translators(text_to, lang_listen)
                    else:
                        kamala_talk('অনুবাদক বন্ধ। আমি তোমার জন্য আর কি করতে পারি?')
                        break
            elif 'বন্ধ হও' in text:
                kamala_talk('তোমাকে সাহায্য করে আনন্দিত হয়েছি। তোমার জন্য শুভ কামনা রইলো। ')
            else:
                kamala_talk('মাফ করবেন আমি বুজতে পারিনি। আপনি পুনরায় বলতে পারবেন কি ?')

    except UnicodeDecodeError as UN:
        print(UN)


# execution of voice assistant
def execution():
    kamala_talk('হাই আমি তোমার ব্যক্তিগত ভয়েস সহকারী. আমার নাম হচ্ছে কমলা।')
    while True:
        listen_kamala = kamala_listen()
        print(listen_kamala)
        kamala_reply(listen_kamala)
        if 'কমলা বন্ধ হও' in listen_kamala:
            break
