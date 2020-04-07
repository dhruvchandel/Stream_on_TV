import webbrowser
from bluedot import *
from signal import pause
import keyboard

# Launching Mock App
# bd = MockBlueDot()
# bd.launch_mock_app()

def Youtube():
    webbrowser.open('https://www.youtube.com', new=0)
#     def bt_controller():
#         def dpad(pos):
#             global it
#             if pos.top:
#                 keyboard.KEY_DOWN
#             elif pos.bottom:
#                 pass
#             elif pos.left:
#                 print("left")
#             elif pos.right:
#                 print("right")
#             elif pos.middle:
#                 pass
        
#         bd.when_pressed = dpad    
    

def Netflix():
    webbrowser.open('https://netflix.com', new=0)

def PrimeVideo():
    webbrowser.open('https://primevideo.com', new=0)

def Hulu():
    webbrowser.open('https://www.hulu.com', new=0)

def DisneyPlus():
    webbrowser.open('https://www.disneyplus.com', new=0)

def Twitch():
    webbrowser.open('https://m.twitch.tv', new=0)
