import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import komola_english
import kamala_bangla


def talk(text):
    # create audio file
    file_name = 'audio.mp3'
    tts = gTTS(text=text, lang='en')
    # save file
    tts.save(file_name)
    # play file
    playsound(file_name)
    # remove file
    os.remove(file_name)


talk('Tell me which language you want to listen?')


def listener():
    listen = sr.Recognizer()
    # what we speak should be on a source
    with sr.Microphone() as mic:
        print('listening...')
        listeners = listen.listen(mic)
        text = ''
        try:
            text = listen.recognize_google(listeners)
        except sr.RequestError as re:
            print(re)
        except sr.UnknownValueError as uv:
            print(uv)
        except sr.WaitTimeoutError as we:
            print(we)
    text = text.lower()
    if 'english' in text:
        komola_english.execution()
    elif 'bangla' in text:
        kamala_bangla.execution()
    else:
        talk('i did not understand please say again ')
        listener()

    return text


listener()
