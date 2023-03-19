# to be used in windows
import win32api
# import win32console
# import win32gui
import win32con
import pythoncom
import pyWinhook as pyHook
import time
import os

letters = {
    "a":"ש",
    "b":"נ",
    "c":"ב",
    "d":"ג",
    "e":"ק",
    "f":"כ",
    "g":"ע",
    "h":"י",
    "i":"ן",
    "j":"ח",
    "k":"ל",
    "l":"ך",
    "m":"צ",
    "n":"מ",
    "o":"ם",
    "p":"פ",
    "q":"",
    "r":"ר",
    "s":"ד",
    "t":"א",
    "u":"ו",
    "v":"ה",
    "w":"",
    "x":"ס",
    "y":"ט",
    "z":"ז",
    ",":"ת",
    ".":"ץ",
    ";":"ף",
    " ":" ",
}

backspace_count = 0
events_count = 0 

class MyExeption(Exception):
    pass


main_thread_id = win32api.GetCurrentThreadId()
combo = set()
captured_string = ''

def translate(string):
    global letters
    
    translated = ''
    print(f'string to translate {string}')
    for i in range(len(string)):
        for k in letters:
            if string[i] == k:
                translated += (letters[string[i]])
    
    return translated


def OnKeyboardEventDown(event):
    global events_count
    global captured_string
    global backspace_count
    # print(event.Ascii)
    events_count += 1
    
    # print(events_count)
    if event.Ascii == 23: # ctrl+w to translate
        data = translate(captured_string)
        # print('ctrl + r')

    if event.Ascii == 13:
        captured_string += "\n"

    if event.Ascii == 3 or event.Ascii == 96: # ctrl+c or ctrl+r 
        # print('Process ended')
        win32api.Beep(3000,10)
        win32api.PostQuitMessage(1)
       
    if event.Ascii >= 32:
        captured_string += chr(event.Ascii)

    if backspace_count == 0 or events_count > 1:
        backspace_count += 1  
        # print(backspace_count)
        if event.Ascii == 8: 
            try:
                captured_string = captured_string.rstrip(captured_string[-1])
            except:
                print('no string')
        
    # print('MessageName: %s' % event.MessageName)
    # print('Message: %s' % event.Message)
    # print('Time: %s' % event.Time)
    # print('Window: %s' % event.Window)
    # print('WindowName: %s' % event.WindowName)
    # print('Ascii: %s' % event.Ascii, chr(event.Ascii))
    # print('Key: %s' % event.Key)
    # print('KeyID: %s' % event.KeyID)
    # print('ScanCode: %s' % event.ScanCode)
    # print('Extended: %s' % event.Extended)
    # print('Injected: %s' % event.Injected)
    # print('Alt %s' % event.Alt)
    # print('Transition %s' % event.Transition)

#   print('---')
    os.system('cls')
    print(captured_string)
    try:
        print(data)
    except:
        pass
    return True


def OnKeyboardEventUp(event):
    global captured_string
    global backspace_count
    global events_count
    # print(event.Key)    
    if backspace_count > 0:
        backspace_count = 0
        if event.Ascii == 8: 
            backspace_count = 0 
    
    
    events_count = 0
    return True

    

hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEventDown

hm.KeyUp = OnKeyboardEventUp

hm.HookKeyboard()

if __name__ == '__main__':
    pythoncom.PumpMessages()
