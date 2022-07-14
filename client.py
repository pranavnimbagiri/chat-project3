import socket
import sys
from threading import Thread
import select
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os 
import time

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name= None
listbox= None
filepathlabel= None

global song_counter
song_counter=0

for file in os.listfir('shared_files'):
    filename=os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter=song_counter+1

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected!=""):
        infolabel.configure(text="Now Playing:"+song_selected)
    else:
        infolabel.configure(text="")

def stop():
    global song_selected
    pygamemixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infolabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.pause()

def musicWindow():

    print("\n\t\t\t\tMUSIC window")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='lightskyblue')

    selectlabel = label(window,text="select song",bg='lightskyblue',font=("calibri",10))
    selectlabel.place(x=2,y=1)

    listbox=listbox(window,height=10,width=19,activestyle="dotbox",bg="lightskyblue",borderwidth=2,font=("calibri",10))
    listbox.place(x=10,y=10)

    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    playbutton=Button(window,text="play",width=10,bd=1,bg="skyblue",font=("Calibri,10"))
    playbutton.place(x=30,y=200)

    stop=Button(window,text="Stop",bd=1,width=10,bg="skyblue",font=("Calibri",10))
    stop.place(x=200,y=200)

    upload=Button(window,text="Upload",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    upload.place(x=30,y=250)

    ResummeButton=Button(window,text="Resume",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    ResummeButton.place(x=200,y=250)

    pausebutton=Button(window,text="Pause",width=10,bd=1,bg='skyblue',font=("Calibri",10))
    pausebutton.place(x=200,y=250)

    dowwnload=Button(window,text-"Download",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    download.place(x=200,y=250)

    infolabel = label(window,text="",fg="blue",font=("Calibri",8))
    infolabel.place(x=4,y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    musicWindow()

setup()