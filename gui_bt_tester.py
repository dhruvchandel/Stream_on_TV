#importing libraries
import tkinter
import webbrowser
from tkinter import Button
from vidstreamlogos import *
from videostreamservices import * 
from musicstreamservices import *
from musicstreamlogos import *
import pyautogui
from bluedot import *
from signal import pause

z = pyautogui.size()
# RESOLUTION OF SCREEN
x = z[0]
y = z[1]

window = 0

def VidStreamExit(window) :
	window.destroy()

def HomePage() :
	global window 
	window = tkinter.Tk()

	window.title("Home")
	window.configure(bg='#000000')

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

	btn_games = Button(window, text="Games")
	btn_games.grid(column=2, row=5, columnspan=4,sticky='n,e,w,s')

	btn_otherapps = Button(window, text="Other Apps")
	btn_otherapps.grid(column=2, row=7, columnspan=4,sticky='n,e,w,s')

	btn_settings = Button(window, text="Settings")
	btn_settings.grid(column=2, row=9, columnspan=4,sticky='n,e,w,s')

	# Below is for the reolution setting of window according to the resolution
	window.geometry(str(x)+'x'+str(y))
	window.mainloop()

HomePage()

style=tkinter.ttk.Style()
style.comfigure('W.TButton',foreground='red')

bd = MockBlueDot()
bd.launch_mock_app()

it=1 
it_min = 0 
it_max = 5  # maximum number of choices offered

def dpad(pos):
    global it
    if pos.top:
        if(it>0):
            it=it-1
        elif(it==0):
            it=it_max   
        print(it) 
    elif pos.bottom:
        if(it<it_max):
            it=it+1
        elif(it==it_max):
            it=it_min
        print(it)
    elif pos.left:
        print("left")
    elif pos.right:
        print("right")
    elif pos.middle:
        print("fire")

if it==2:
    btn_musicstream = Button(window, text="Music Streaming",style='W.TButton', command=MusicStreamPage)
    btn_musicstream.grid(column=2, row=3, columnspan=4, sticky='n,e,w,s')

bd.when_pressed = dpad

pause()

