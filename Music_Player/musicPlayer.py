
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
import os
import time
from mutagen.mp3 import MP3
from tkinter import filedialog

mixer.init()

class musicplayer:
    def __init__(self,Tk):
        self.root =Tk
        self.root.title('Music Player')
        self.root.geometry('700x400')
        self.root.configure(background= 'white')
         
        #open_file function
        
        def open_file():
            global filename
            filename= filedialog.askopenfilename()
        
        #menu
        self.menubar = Menu(self.root)
        self.root.configure(menu=self.menubar)
        
        self.submenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=open_file)
        self.submenu.add_command(label='Exit',command=self.root.destroy)
        
        #Adding Label....
        self.label1 = Label(text='Select ana Play',bg='black',fg='white',font=28).place(x=50,y=40)
       
        def songinf():
            self.label1['text'] ='Current Music:- ' + os.path.basename(filename)
        
        self.label = Label(text="Let's feel it")
        self.label.pack(side=BOTTOM,fill=X)
        
        
        #Adding left image....
        self.left_photo = Image.open('images/music.jpg')
        self.resized = self.left_photo.resize((500,210))
        self.l_img = ImageTk.PhotoImage(self.resized)
        left_photo = Label(self.root, image=self.l_img,bg='white').place(x=240,y=60,width=500,height=250 )
        
        #adding image--
        self.image = Image.open('images/img1.jpg')
        self.resize_image = self.image.resize((200,200))
        self.img = ImageTk.PhotoImage(self.resize_image)
        photo = Label(self.root,image=self.img,bg='white').place(x=50,y=70)
        
        #Creating button functions:..
        def stop():
            global stop
            stop = TRUE
            mixer.music.stop()
            self.label['text']= 'Music Stopped...'
            
        def play():
            try:
                paused or stop
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label['text']='Music Playing....'
                except:
                    messagebox.showerror("Error","File not found")
            else:
                mixer.music.unpause()
                self.label['text'] = 'Music Playing...'
            

            
        def pause():
            global paused
            paused =TRUE
            mixer.music.pause()
            self.label['text']='Music Paused...'
        
        
        #Creating Buttons...
        #play_button...
        
        self.photo_btn1 = Image.open('images/play.jpg')
        self.r_btn1 = self.photo_btn1.resize((30,30))
        self.p_btn1= ImageTk.PhotoImage(self.r_btn1)
        photo_btn1 = Button(self.root,image=self.p_btn1,bg='white',command=play,bd=0).place(x=65,y=320)
        
        #pause_button...
        
        self.photo_btn2 = Image.open('images/pause.png')
        self.r_btn2 = self.photo_btn2.resize((30,30))
        self.ps_btn2 = ImageTk.PhotoImage(self.r_btn2)
        photo_btn2 = Button(self.root,image=self.ps_btn2,bg='white',command=pause,bd=0).place(x=115,y=320)
        
        # stop_button,,,
        
        self.photo_btn3 = Image.open('images/stop.png')
        self.r_btn3 = self.photo_btn3.resize((30,30))
        self.ps_btn3 = ImageTk.PhotoImage(self.r_btn3)
        photo_btn3 = Button(self.root,image=self.ps_btn3,bg='white',command=stop,bd=0).place(x=165,y=320)
        
        
        #volume button function
        def mute():
            self.scale.set(0)
            self.photo_btn4 = Image.open('images/mute.jpg')
            self.r_btn4 =self.photo_btn4.resize((30,30))
            self.v_btn = ImageTk.PhotoImage(self.r_btn4)
            vol_btn = Button(self.root,image=self.v_btn,bg='white',bd=0,command=unmute).place(x=450,y=320)
            
        #unmute
        def unmute():
            self.scale.set(25)
            self.mute = Image.open('images/vol.png')
            self.r_mute = self.mute.resize((30,30))
            self.mute_img = ImageTk.PhotoImage(self.r_mute)
            mute_img = Button(self.root,image = self.mute_img,bg='white',bd=0,command=mute).place(x=450,y=320)
                    
            
        
        #function for volume bar...
        def volume(vol):
            volume = int(vol)/100
            mixer.music.set_volume(volume)
           
        
        
        #vol button
        self.photo_btn4 = Image.open('images/vol.png')
        self.r_btn4 =self.photo_btn4.resize((30,30))
        self.v_btn = ImageTk.PhotoImage(self.r_btn4)
        vol_btn = Button(self.root,image=self.v_btn,bg='white',bd=0,command=mute).place(x=450,y=320)
        
        
        #volume bar
        self.scale = Scale(self.root,from_=0,to=100,orient=HORIZONTAL,bg='white',bd=0,length=160,command=volume)
        self.scale.set(25)
        self.scale.place(x=500,y=320)
        
        
root =Tk()
obj = musicplayer(root)
root.mainloop()
