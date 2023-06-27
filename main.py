from pyautogui import moveTo, click, rightClick, write, keyDown, keyUp, hotkey, scroll
import pyautogui
import pyperclip
import re
import time
from threading import Thread, Event
import sys

unmutestoploop = Event()
def send(message1):
    pyautogui.moveTo(189, 20, 0.1)
    pyautogui.click()
    pyautogui.moveTo(1000, 960)
    pyautogui.click()
    mes = re.sub('OpenAI', 'BainBan(Ben)', message1)
    mes2 = re.sub('ChatGPT', "Makise Kurisu (MK)", mes)
    pyperclip.copy(mes2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")
def searchimagine(ce):
    moveTo(800, 10)
    time.sleep(2)
    click()
    moveTo(500, 180)
    time.sleep(2)
    click()
    hotkey("ctrl", "a")
    time.sleep(2)
    write(ce)
    keyDown("ENTER")
    keyUp('ENTER')
    time.sleep(2)
    moveTo(100, 390)
    time.sleep(2)
    rightClick()
    moveTo(150, 590)
    time.sleep(2)
    click()
    time.sleep(2)
    pyautogui.moveTo(189, 20, 0.1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1000, 960)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")
def checkuserperms():
    time.sleep(0.2)
    pyautogui.moveTo(650, 850)
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.moveTo(1550, 580)
    time.sleep(1)
    pyautogui.dragTo(1700, 580, 1)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)
    moveTo(1370, 190)
    time.sleep(0.2)
    pyautogui.click()
    copy = pyperclip.paste()
    print(copy)
    if copy == "admin's nr1 phone number" or copy == "admin's nr2 phone number":
        return "yes"
    elif "what your country code starts with here" not in pyperclip.paste():
        send("A aparut o eroare in a iti verifica permisiunile, incearca din nou acum xx")

    return "no"
def unmute(time34=1, name1="test"):
    time.sleep(time34)
    global unmutestoploop
    unmutestoploop.set()
    time.sleep(3)
    moveTo(1000, 200)
    time.sleep(0.5)
    click()
    time.sleep(0.5)
    moveTo(1800, 400)
    scroll(-600)
    time.sleep(0.5)
    moveTo(1850, 1000)
    click()
    time.sleep(0.5)
    moveTo(1000, 300)
    click()
    time.sleep(1)
    pyautogui.write(f"{name1}")
    time.sleep(1)
    moveTo(1000, 350)
    time.sleep(0.5)
    click()
    time.sleep(0.5)
    moveTo(1100, 380)
    time.sleep(0.5)
    click()
    time.sleep(2)
    moveTo(740, 220)
    time.sleep(0.5)
    click()
    time.sleep(0.5)
    moveTo(1370, 190)
    time.sleep(0.5)
    click()
    unmutestoploop.clear()
    send(f"{name1} si-a luat unmute")
def mute(name, time2, reason="None"):
    if name == "Beni" or name == "B" or name == "Ben" or name == "Beni Noul" or name == "Marius" or name == "Mari" or name == "M" or name == 'Ma' or name ==  "Mar" or name == "Mariu":
        send("Scuze, n-ai permisiune pentru a face asta xx")
        return
    else:
        pyautogui.moveTo(689, 877, 0.1)
        pyautogui.moveTo(820, 877, 0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(675, 820, 0.1)
        moveTo(1000, 200)
        time.sleep(1)
        click()
        moveTo(1800, 400)
        time.sleep(1)
        scroll(-600)
        moveTo(1850, 1000)
        time.sleep(1)
        click()
        time.sleep(0.2)
        moveTo(1000, 300)
        click()
        time.sleep(1)
        pyautogui.write(f"{name}")
        time.sleep(1)
        moveTo(1000, 350)
        time.sleep(0.2)
        click()
        time.sleep(0.2)
        moveTo(1100, 450)
        time.sleep(0.2)
        click()
        time.sleep(2)
        moveTo(740, 220)
        time.sleep(0.2)
        click()
        time.sleep(0.2)
        moveTo(1370, 190)
        time.sleep(0.2)
        click()
        send(f"{name} si-a luat mute pentru {time2}s motiv: {reason}")
        global thread
        thread = Thread(target=unmute, args=(int(time2), name))
        thread.start()

def ask(what):
    logo = pyautogui.locateOnScreen('2.png')
    print("start")
    time.sleep(3)
    pyautogui.moveTo(500, 10)
    pyautogui.click()
    moveTo(100, 170)
    click()
    pyautogui.moveTo(1000, 930)
    pyautogui.click()
    pyperclip.copy(what)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")
    time.sleep(10)
    try:
        x = logo.left + 10
        y = logo.top + 10
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click()
    except AttributeError:
        logo = pyautogui.locateOnScreen('copy.png', confidence=0.8)
        x = logo.left + 10
        y = logo.top + 10
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click()
        if not bool(pyperclip.paste().strip()):
            moveTo(100, 70)
            click()
            time.sleep(4)
            ask()

    return
command = "!"
talk = "!talk"
mute1 = "!mute"
unmute1 = "!unmute"
lastmessacommand = False
stop = "!stop"
imagine = "!imagine"
def runspccmd(lastmessage):
    global command, talk, mute1, unmute1, lastmessacommand
    if command in lastmessage:
        if talk in lastmessage:
            lastm = str(lastmessage)
            final = lastm.replace('<span>', "")
            final1 = final.replace('!talk', "")
            final2 = final1.replace('</span>', "")
            ask(final2)
            send(pyperclip.paste())
        elif mute1 in lastmessage:
                if checkuserperms() == "no":
                    print("skj")
                    send("Scuze, n-ai permisiune pentru a face asta xx")
                    return
                else:
                    lastm = str(lastmessage)
                    final = lastm.replace('<span>', "")
                    final1 = final.replace('!mute', "")
                    final2 = final1.replace('</span>', "")
                    split = final2.split(" ", 3)
                    print(split)
                    mute(split[1], split[2], split[3])
        elif stop in lastmessage:
            if checkuserperms() == "yes":
                send("Bot oprit ;( Ne mai vedem xx")
                sys.exit("Bot oprit")
            elif checkuserperms() == "no":
                send("n-ai permisiune sa faci asta xx")
        elif unmute1 in lastmessage:
            if checkuserperms() == "yes":
                try:
                    lastm = str(lastmessage)
                    final = lastm.replace('<span>', "")
                    final1 = final.replace('!unmute', "")
                    final2 = final1.replace('</span>', "")
                    split = final2.split(" ", 2)
                    send("eroare comanda nu poate fi folosita. Me grieu sa fac comanda astia decia oas lsa sas")
                except IndexError:
                    send("eroare comanda nu poate fi folosita. Me grieu sa fac comanda astia decia oas lsa sas")
            else:
                send("n-ai permisiune sa faci asta xx")
        elif imagine in lastmessage:
                    lastm = str(lastmessage)
                    final = lastm.replace('<span>', "")
                    final1 = final.replace('!imagine', "")
                    final2 = final1.replace('</span>', "")
                    split = final2.split(" ", 1)
                    send("sorry, this feature is still in development!")
        else:
            send("""Comanda necunoscuta. Comenzi:
            !talk intrebare
            !mute nume secunde motiv
            !imagine (in development)
            !stop""")



def getlastmessage():
    lm = pyperclip.paste()
    final = lm.replace('<span>', "")
    final2 = final.replace('</span>', "")
    print(final2)
    if "!" in final2:
        runspccmd(final2)
    pyautogui.moveTo(689, 877, 0.1)
    time.sleep(0.2)
    pyautogui.rightClick()
    time.sleep(0.2)
    pyautogui.moveTo(700, 850, 0.1)
    pyautogui.click() 
    time.sleep(0.2)
    pyautogui.keyDown("F2")
    time.sleep(0.2)
    pyautogui.keyUp("F2")
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    pyautogui.moveTo(1900, 140,0.1)
    pyautogui.click()

while True:
    while not unmutestoploop.is_set():
        time.sleep(1.2)
        pyautogui.moveTo(1000, 600)
        pyautogui.scroll(-600)
        getlastmessage()
