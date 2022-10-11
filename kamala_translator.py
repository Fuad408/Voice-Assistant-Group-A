import os
from gtts import gTTS
from playsound import playsound

# german translator
def kamala_talk_de(text):
    # create audio file
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='de')
    # save file
    tts.save(file_name)
    # play file
    playsound(file_name)
    # remove file
    os.remove(file_name)


#china translator
def kamala_talk_cn(text):
    # create audio file
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='de')
    # save file
    tts.save(file_name)
    # play file
    playsound(file_name)
    # remove file
    os.remove(file_name)