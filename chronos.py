# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
from time import time
from tkinter import *

blind_period = 1200

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        #self.geom="200x200+0+0"
        self.init_window()
        
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def init_window(self):
        self.master.title("John's GUI")
        self.pack(expand=YES, fill=BOTH)
        
        # Create a Menu Bar
        menu=Menu(self.master)
        self.master.config(menu=menu)
        
        # Create the File menu
        file=Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        
        # Create the Game Menu
        game=Menu(menu)
        game.add_command(label='Launch Timer', command=PokerTimerWidget)
        menu.add_cascade(label='Game', menu=game)
        
        #quitButton = Button(self, text="Quit", command=self.client_exit)
        #quitButton.place(x=0, y=0)
        
    def client_exit(self):
        exit()
         
class PokerTimerWidget:
    def __init__(self):
        root = Tk()
        root.title('Poker Timer')
        root.state('zoomed')
        #self.countdown = 1200
        self.countdown = blind_period
        timestr = '{:02}:{:02}'.format(*divmod(self.countdown, 60))
        
        labelfont = ('times', 20, 'bold')
        self.display = Label(root, text=timestr, width=20)
        self.display.config(bg='black', fg='yellow', font=labelfont)
        self.display.pack(expand=YES, fill=BOTH)
        self.display.pack()
        
        self.button = Button(root, text='Paused', command=self.toggle)
        #self.button = Button(root, text=timestr, command=self.toggle)
        self.button.pack(side=BOTTOM,fill=X)
        self.paused = True
        root.mainloop()

    def toggle(self):
        if self.paused:
            self.paused = False
            self.button.config(text='Running')
            self.snaptime = time()
            self.run_timer()
        else:
            self.paused = True
            #self.snaptime = time()
            self.button.config(text='Paused')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.snaptime)
        if delta >= 1:
            self.countdown -= 1
            #self.snaptime = time()    
        timestr = '{:02}:{:02}'.format(*divmod(self.countdown, 60))
        self.display.config(text=timestr)
        self.display.after(1000, self.run_timer)
        
root=Tk()
root.geometry("200x100")
Window(root)
root.mainloop()
