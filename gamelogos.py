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


def displaylogosnake(window):
	Logo = tkinter.PhotoImage(file=os.path.join("logos","snake.png"))
	z = tkinter.Label(window,image = Logo)
	z.image=Logo					# Bohot imp step thaa dimaag kharab  http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
	z.grid(row=4, column=3, rowspan=8, columnspan=8, sticky='n,e,w,s')
