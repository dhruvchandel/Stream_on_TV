#importing libraries
import tkinter
import webbrowser
from PIL import Image
from tkinter import Button
import pyautogui
import os 

z=pyautogui.size()
# Resolution Of Screen
x = z[0]
y = z[1]


def displaylogoyoutube(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","youtube.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo					# Bohot imp step thaa dimaag kharab  http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# print('executed')

def displaylogonetflix(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","netflix.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# print('executed')

def displaylogoprimevideo(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","primevideo.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# print('executed')

def displaylogohulu(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","hulu.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# print('executed')

def displaylogotwitch(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","twitch.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# print('executed')

def displaylogodisneyplus(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","disneyplus.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
	# window.mainloop()
	# print('executed')
