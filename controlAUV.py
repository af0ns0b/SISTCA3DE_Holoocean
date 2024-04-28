from pynput import keyboard 
import numpy as np 
 
# up/ down - i, k 
# yaw left/right- j, l 
# forward/backward - w, s 
# strafe - a,s 
 
pressed_keys = list() 
force = 25  # value that will be set to the thrusters 
 
 
def on_press(key):  # function that handles when you press a key 
    global pressed_keys 
    if hasattr(key, 'char'): 
        pressed_keys.append(key.char) 
        pressed_keys = list(set(pressed_keys)) 
 
 
def on_release(key):  # function that handles when you release a key 
    global pressed_keys 
    if hasattr(key, 'char'): 
        pressed_keys.remove(key.char) 
 
 
# function that listens to when there is a change on the keyboard 
listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
listener.start() 
 
 
def parse_keys(keys, val): 
    command = np.zeros(8)  # set 8 possible positions to zero 
    if 'i' in keys: 
        command[0:4] += val  # go up (0 to 4) 
    if 'k' in keys: 
        command[0:4] -= val  # go down (0 to 4) 
    if 'j' in keys: 
        command[[4, 7]] += val  # rotate to the left (4 and 7) 
        command[[5, 6]] -= val  # rotate to the left (5 and 6) 
    if 'l' in keys: 
        command[[4, 7]] -= val  # rotate to the right (4 and 7) 
        command[[5, 6]] += val  # rotate to the right (5 and 6) 
    if 'w' in keys: 
        command[4:8] += val  # go forward (4 to 8) 
    if 's' in keys: 
        command[4:8] -= val  # go backwards (4 to 8) 
    if 'a' in keys: 
        command[[4, 6]] += val  # go left (4 and 6) 
        command[[5, 7]] -= val  # go left (5 and 7) 
    if 'd' in keys: 
        command[[4, 6]] -= val  # go right (4 and 6) 
        command[[5, 7]] += val  # go right (5 and 7) 
 
    return command 
