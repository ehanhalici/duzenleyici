from pynput.mouse import Listener
from tkinter import *
import pyperclip
import mtranslate
import pyautogui
import time
import threading

pano = ""
temp = ""

click = 0 
select = 0
status = True

pyperclip.copy("")  


def process():
    global pano, temp, status
    #temp ve osBuffer ı temizle
    temp = ""
    pyperclip.copy("") 
    
    #bir yer seçildiyse bunu tempe kopyala
    pyautogui.hotkey('ctrl', 'c')
    temp = pyperclip.paste()

    if temp == "":
        return
    if temp != pano:
        pano = temp
        edit()
        translate()
        status = True

def edit():
    global pano
    pano = "".join(pano.split("-\n"))
    pano = " ".join(pano.split("\n"))

def translate():
    global pano
    pano = mtranslate.translate(pano,"tr","en")

def on_click(x, y, button, pressed):
    global click, pano, temp
    try:
        click = click + 1
        if click == 2:
            click = 0
            process()
    except:
       pass


root = Tk()
root.attributes('-topmost', 'true')
label = Label(root, text="translate text",bg="white")
label.pack()
listener = Listener(on_click=on_click)
listener.start()
while True:
    root.update()
    label.config(text = pano,bg="white", wraplength=700,font=(None,16))
    label.pack()
    time.sleep(0.3)


    

root.destroy()
#with Listener(on_click=on_click) as listener:
#    listener.join()