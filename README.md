# Message Spam Script

This script will continuously spam messages with a toggle button.

```python
import pyautogui
import time

def spam_toggle():
    global spamming
    spamming = not spamming

spamming = False

def spam_messages():
    global spamming
    while True:
        if spamming:
            pyautogui.typewrite('spam message')
            pyautogui.press('enter')
            time.sleep(0.1)

spam_messages()
To bind the spam_toggle function to a button, you can use a GUI library like tkinter to create a graphical user interface with a button that calls the spam_toggle function when clicked.
Note: This script is for educational purposes only and should not be used for illegal activities such as spamming. Always respect the terms of service of the applications you use and the privacy of others.
