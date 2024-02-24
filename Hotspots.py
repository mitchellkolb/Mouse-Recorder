
import os
import pyautogui
import time, keyboard
import customtkinter as ctk
from tkinter import ttk

from pynput import mouse
from pynput.mouse import Listener, Button, Controller

#  ctrl alt q             to run the python file



#Setting up Window
app = ctk.CTk()
# Calculate window position to center the GUI in the middle of the users screen dynamically
window_width = 500
window_height = 250
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
app.resizable(False, False)

app.title("HotSpots")
app.attributes("-topmost", True)

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


 
#GUI button Particulars
custom_font = ("Arial", 13, "bold")

startRun = ctk.CTkButton(app, text="Record", font=custom_font, command=replayMM, width=75, height=50)
startRun.pack(side="left", padx=15, pady=10)

startRun = ctk.CTkButton(app, text="Replay", font=custom_font, command=replayMM, width=75, height=50)
startRun.pack(side="left", padx=10, pady=10)

savedRun = ctk.CTkButton(app, text="Saved", font=custom_font, command=savedFunction, width=75, height=50)
savedRun.pack(side="left", padx=10, pady=10)

dropDownValues = ["option 1", "option 2"]
combobox_var = ctk.StringVar(value="option 2")
combobox = ctk.CTkComboBox(app, values=["option 1", "option 2"], command=combobox_callback, variable=combobox_var)

combobox_var.set("option 2")
combobox.pack_forget()


app.mainloop()









def moveAndClik():
    pyautogui.moveTo(xPos, yPos, duration=1)
    pyautogui.click()

    pyautogui.move(0,-distanceToMoveUp)
    pyautogui.click()

#time.sleep(2)

"""
while True:    
    location = pyautogui.position()
    print(location)
    time.sleep(0.1)
"""

# top left is 0,0
# bottom right is screen size
    
