from tkinter import *
import pyautogui
import tkinter as tk
import time
from win32api import GetSystemMetrics
import keyboard

maxdownmouspos = GetSystemMetrics(1) - 200

def blockkeys():
    keyboard.block_key("f4")
    root.after(500, task)

def on_press(event):
    #print('on_press: event:', event)
    #print('on_press: keysym:', event.keysym)
    print('{0} pressed'.format(event.keysym))

def on_release(event):
    #print('on_release: event:', event)
    #print('on_release: keysym:', event.keysym)
    print('{0} release'.format(event.keysym))

    if event.keysym == 'Escape':
         print("exist program")
         root.destroy()

    if event.keysym == 'Win_L' :
        pyautogui.moveTo(1800, 20)
        pyautogui.click()

def Dragging(event):
    x = root.winfo_pointerx() - root.winfo_rootx()
    y = root.winfo_pointery() - root.winfo_rooty()
    #print(maxdownmouspos)
    if(y > maxdownmouspos):
        pyautogui.moveTo(930, 580)

root = Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
filename = PhotoImage(file ="bg.png")

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

background_label = Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
textBox=Text(root, height=2, width=10)
textBox.pack()
textBox.place(relx=0.5, rely=0.5, anchor=CENTER)
buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
buttonCommit.place(relx=0.5, rely=0.55, anchor=CENTER)

root.bind('<KeyPress>', on_press)
root.bind('<Motion>', Dragging)
root.bind('<KeyRelease>', on_release)
root.after(500, blockkeys)
root.mainloop()


