import pyautogui
import time

def spam_toggle():
    global spamming
    spamming = not spamming

spamming = False

def spam_messages():
    while True:
        if spamming:
            pyautogui.typewrite('spam message')
            pyautogui.press('enter')
            time.sleep(0.1)

spam_messages()
