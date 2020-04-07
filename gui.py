#importing libraries
import tkinter
import os
import webbrowser
from tkinter import Button
from vidstreamlogos import *
from videostreamservices import * 
from musicstreamservices import *
from musicstreamlogos import *
from settinglogo import *
from gamelogos import *
import pyautogui
from tkinter.ttk import *
from snake import SnakeGame
#from turtle import *
#from random import randrange
#from freegames import square, vector

z = pyautogui.size()
# RESOLUTION OF SCREEN
x = z[0]
y = z[1]

def VidStreamExit(window) :
    window.destroy()

def VideoStreamPage():
    window = tkinter.Toplevel()

    #Setting up the grid
    
    col_count= 9
    row_count= 15

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)
     # Grid setter ended

    window.title("Video Streaming")

    home = Button(window, text="<= Home", command=lambda :VidStreamExit(window))
    home.grid(column=0, row=0, sticky='n,e,w,s')

    youtube = Button(window, text='YouTube', command=Youtube)
    youtube.grid(column=1, columnspan=2, row =2, sticky='n,e,w,s')
    youtube.bind("<Enter>",lambda event,  window=window : displaylogoyoutube(window))

    netflix = Button(window, text='NETFLIX', command=Netflix)
    netflix.grid(column=1,columnspan=2, row =4, sticky='n,e,w,s')
    netflix.bind("<Enter>",lambda event, window=window : displaylogonetflix(window))

    primevideo = Button(window, text='primevideo', command=PrimeVideo)
    primevideo.grid(column=1, columnspan=2, row =6, sticky='n,e,w,s')
    primevideo.bind("<Enter>",lambda event, window=window : displaylogoprimevideo(window))

    hulu = Button(window, text='HULU', command=Hulu)
    hulu.grid(column=1,columnspan=2, row =8, sticky='n,e,w,s')
    hulu.bind("<Enter>",lambda event, window=window : displaylogohulu(window))

    disneyplus = Button(window, text='Disney +', command=DisneyPlus)
    disneyplus.grid(column=1,columnspan=2, row =10, sticky='n,e,w,s')
    disneyplus.bind("<Enter>",lambda event, window=window : displaylogodisneyplus(window))

    twitch = Button(window, text='Twitch', command=Twitch)
    twitch.grid(column=1,columnspan=2, row =12, sticky='n,e,w,s')
    twitch.bind("<Enter>",lambda event, window=window : displaylogotwitch(window))

    window.geometry(str(x)+'x'+str(y))
    window.mainloop()

def MusicStreamPage():
    window = tkinter.Toplevel()

    #Setting up the grid
    
    col_count= 9
    row_count= 15

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)
     # Grid setter ended

    window.title("Music Streaming")

    home = Button(window, text="<= Home", command=lambda :VidStreamExit(window))
    home.grid(column=0, row=0, sticky='n,e,w,s')

    spotify = Button(window, text='Spotify', command=Spotify)
    spotify.grid(column=1, columnspan=2, row =2, sticky='n,e,w,s')
    spotify.bind("<Enter>",lambda event,  window=window : displaylogospotify(window))

    gaana = Button(window, text='Gaana', command=Gaana)
    gaana.grid(column=1,columnspan=2, row =4, sticky='n,e,w,s')
    gaana.bind("<Enter>",lambda event, window=window : displaylogogaana(window))

    soundcloud = Button(window, text='SoundCloud', command=SoundCloud)
    soundcloud.grid(column=1, columnspan=2, row =6, sticky='n,e,w,s')
    soundcloud.bind("<Enter>",lambda event, window=window : displaylogosoundcloud(window))

    amazonmusic = Button(window, text='Amazon Music', command=AmazonMusic)
    amazonmusic.grid(column=1,columnspan=2, row =8, sticky='n,e,w,s')
    amazonmusic.bind("<Enter>",lambda event, window=window : displaylogoamazonmusic(window))

    window.geometry(str(x)+'x'+str(y))
    window.mainloop()


def GamePage():
    window = tkinter.Toplevel()
    #Setting up the grid
    
    col_count= 9
    row_count= 15

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)
     # Grid setter ended

    window.title("Games")

    home = Button(window, text="<= Home", command=lambda :VidStreamExit(window))
    home.grid(column=0, row=0, sticky='n,e,w,s')
    
    snake = Button(window, text='Snake', command=SnakeGame)
    snake.grid(column=1,columnspan=2, row =2, sticky='n,e,w,s')
    snake.bind("<Enter>",lambda event, window=window : displaylogosnake(window))
    

    window.geometry(str(x)+'x'+str(y))
    window.mainloop()

def OtherAppsPage():
    window = tkinter.Toplevel()
    #Setting up the grid
    
    col_count= 9
    row_count= 15

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)
     # Grid setter ended

    window.title("Other Applications")

    home = Button(window, text="<= Home", command=lambda :VidStreamExit(window))
    home.grid(column=0, row=0, sticky='n,e,w,s')

    window.geometry(str(x)+'x'+str(y))
    window.mainloop()

def SettingsPage():
    window = tkinter.Toplevel()
    #Setting up the grid
    
    col_count= 9
    row_count= 15

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)
     # Grid setter ended

    window.title("Settings")

    home = Button(window, text="<= Home", command=lambda :VidStreamExit(window))
    home.grid(column=0, row=0, sticky='n,e,w,s')
    
    Wifi = Button(window, text='Wi-Fi')#, command=WiFi)
    Wifi.grid(column=1,columnspan=2, row =4, sticky='n,e,w,s')
    Wifi.bind("<Enter>",lambda event, window=window : displaylogowifi(window))
    
    rc = Button(window, text='Remote Control')#, command=WiFi)
    rc.grid(column=1,columnspan=2, row =6, sticky='n,e,w,s')
    rc.bind("<Enter>",lambda event, window=window : displaylogorc(window))
    
    sPeech = Button(window, text='Speech')#, command=WiFi) #maybe use lastpass for it
    sPeech.grid(column=1,columnspan=2, row =8, sticky='n,e,w,s')
    sPeech.bind("<Enter>",lambda event, window=window : displaylogospeech(window))
    
    account = Button(window, text='Account Manager')#, command=WiFi) #maybe use lastpass for it
    account.grid(column=1,columnspan=2, row =10, sticky='n,e,w,s')
    account.bind("<Enter>",lambda event, window=window : displaylogoaccount(window))
    

    window.geometry(str(x)+'x'+str(y))
    window.mainloop()

def HomePage() :
    window = tkinter.Tk()

    window.title("Home")
    window.configure(bg='#FF0000')

    # Setting The Grid
    grid_setter = tkinter.Label(window, text = '')
    grid_setter.grid(column=7, row=11)
    col_count, row_count = window.grid_size()

    for col in range(0,col_count):
        window.grid_columnconfigure(col, minsize=x/col_count)

    for row in range(0,row_count):
        window.grid_rowconfigure(row, minsize=y/row_count)

    # Buttons  

    btn_vidstream = Button(window, text="Video Streaming", command=VideoStreamPage)
    btn_vidstream.grid(column=2, row=1, columnspan=4, sticky='n,e,w,s')

    btn_musicstream = Button(window, text="Music Streaming", command=MusicStreamPage)
    btn_musicstream.grid(column=2, row=3, columnspan=4, sticky='n,e,w,s')

    btn_games = Button(window, text="Games", command=GamePage)
    btn_games.grid(column=2, row=5, columnspan=4,sticky='n,e,w,s')

    btn_otherapps = Button(window, text="Other Apps", command=OtherAppsPage)
    btn_otherapps.grid(column=2, row=7, columnspan=4,sticky='n,e,w,s')

    btn_settings = Button(window, text="Settings", command=SettingsPage)
    btn_settings.grid(column=2, row=9, columnspan=4,sticky='n,e,w,s')

    # Below is for the reolution setting of window according to the resolution
    window.geometry(str(x)+'x'+str(y))
    window.mainloop()

HomePage()





