
import os
import pyautogui
import time, keyboard
import customtkinter as ctk
from tkinter import ttk

from pynput import mouse
from pynput.mouse import Listener, Button, Controller



mouseList = [(1239,368, 1), (1020, 725, 2), (1630, 737, 0.1), (1239,368, 0.5)]


#This moves the mouse from either the local saved record or one from the file
#It should be given a list with the x,y cords and a time duration between points of where the mouse wants to go
def replayMM():
    print("REPLAY MouseMovements")
    # Move the cursor along the desired path
    for x, y, dur in mouseList:
        pyautogui.moveTo(x, y, duration=dur)
        #time.sleep(1)  # Adjust the delay as needed


def recordMM(xPos, yPos):
    print("REPLAY MouseMovements")


def sendMM_toFile(mouseList):
    print("SAVE MouseMovements")

    #Save to file
    with open("savedMouseMovements.txt", 'a') as log:
        try:
            char = mouseList.char
            log.write(char)
        except:
            print("Error saving record")



#Button Functions
def move_in_square():
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Define the coordinates for the square path
    square_path = [(100, 100), (screen_width - 100, 100), (screen_width - 100, screen_height - 100), (100, screen_height - 100)]

    # Move the cursor along the square path
    for x, y in square_path:
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(1)  # Adjust the delay as needed

    # Move the cursor back to the starting position
    pyautogui.moveTo(square_path[0][0], square_path[0][1], duration=0.5)


def other():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)

            if keyboard.is_pressed('space'):  # Check if space bar is pressed
                break

            time.sleep(0.2)

    except KeyboardInterrupt:
        print('\n')


def mouseClick():
    def print_on_left_click(x, y, button, pressed):
        if button == button.left and pressed:
            print("User left-clicked!")

    # Start listening for mouse events
    with Listener(on_click=print_on_left_click) as listener:
        listener.join()
        




def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def listener():
    # Collect events until released
    with mouse.Listener(
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()



def savedFunction():
    print("Viewing Saved Motions")
    combobox.pack(side="bottom", padx=10, pady=10)
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

