import speech_recognition as sr
from guessing_game import recognize_speech_from_mic
import time
import vlc
from sikuli import *
from lackey import *
# player = vlc.MediaPlayer("Status.mp3")
# player.play()
# time.sleep(10)

# a = recognize_speech_from_mic(r, m)

r = sr.Recognizer()
m = sr.Microphone()

global a
a = False

while not a:

    text = recognize_speech_from_mic(r, m)
    compareText = text['transcription']

    if compareText is not None and compareText.lower() == "aniket":
        print("inside loop")
        click("unmute.png")
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new("Status.mp3")
        player.set_media(media)
        player.play()
        time.sleep(1.5)
        duration = player.get_length() / 1000
        print(duration)
        time.sleep(duration)
        click("mute.png")
        a = True
    else:
        print(text['transcription'])

#click("skype.png")
# wait("mute.png", 5)# Maybe the Start menu is slow




