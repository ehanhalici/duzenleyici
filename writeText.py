#!/usr/bin/env python
from time import sleep
import pyperclip
import mtranslate
from pynput.mouse import Listener
import pyautogui

pano = ""
temp = ""
file = open('./text',"a")

click = 0 
select = 0

print("program running")
pyperclip.copy("")  

def process():
    global pano, temp
    pyautogui.hotkey('ctrl', 'c')
    temp = pyperclip.paste()
    if temp == "":
        return
    if temp != pano:
        pano = temp
        edit()
        translate()
        #rewrite
        pyperclip.copy(pano)
        writeFile()

def edit():
    global pano
    pano = "".join(pano.split("-\n"))
    pano = " ".join(pano.split("\n"))

def translate():
    global pano
    pano = mtranslate.translate(pano,"tr","en")

def writeFile():
    global file, pano

    file.write(pano)
    file.write('\n')
    file.flush()

def on_click(x, y, button, pressed):
    global click, pano, temp
    try:
        click = click + 1
        if click == 2:
            click = 0
            process()
    except:
       pass

with Listener(on_click=on_click) as listener:
    listener.join()