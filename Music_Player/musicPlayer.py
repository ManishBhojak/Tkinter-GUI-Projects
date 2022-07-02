from numpy import var
import pygame
import tkinter as Tkr
from tkinter.filedialog import askdirectory
import os

musicPlayer=Tkr.Tk()
musicPlayer.title('Music Player')
musicPlayer.geometry("275x450") 

directory = askdirectory()
os.chdir(directory)
songlist=os.listdir()
playlist = Tkr.Listbox(musicPlayer,font='Helvatica 12 bold',bg='cyan',selectmode=Tkr.SINGLE)

for item in songlist:
    position=0
    playlist.insert(position, item)
    position = position+1

pygame.init ()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(Tkr.ACTIVE))
    var.set(playlist.get(Tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

musicPlay = Tkr.Button(musicPlayer,text='Play',font='Helvatica 13 bold',fg='white',bg='red',command=play)
musicStop = Tkr.Button(musicPlayer,text='Stop',font='Helvatica 13 bold',fg='white',bg='green',command=stop)
musicPause = Tkr.Button(musicPlayer,text='Pause',font='Helvatica 13 bold',fg='white',bg='blue',command=pause)
musicUnpause = Tkr.Button(musicPlayer,text='Unpause',font='Helvatica 13 bold',fg='white',bg='purple',command=unpause)

var = Tkr.StringVar()
songtitle = Tkr.Label(musicPlayer,font='Helvatica 13 bold',textvariable=var)

songtitle.pack()
musicPlay.pack(side=Tkr.TOP,fill='both')
musicPause.pack(side=Tkr.TOP,fill='both')
musicUnpause.pack(side=Tkr.TOP,fill='both')
musicStop.pack(side=Tkr.TOP,fill='both')
playlist.pack(fill='both',expand='yes',side=Tkr.BOTTOM)
musicPlayer.mainloop()
