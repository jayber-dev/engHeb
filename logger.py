from pynput.keyboard import Listener,KeyCode
from pynput import keyboard
import binascii
import codecs

def press(key):
 
    try:
        pass
        # print(key.char)
    except:
        data = str(key)
        try:
            print(ord(data))
            if ord(data) == 3:
                print('combination was pressed')
        except:
            print(data)
        

    

with Listener(on_press=press) as li:
    li.join()


