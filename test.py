import os
import pyautogui
import time
import customtkinter as ctk

from pynput import mouse
 
# List to store recorded mouse events
recorded_events = []

# Variable to indicate whether recording is ongoing
recording = False

# Function to record mouse clicks and positions
def record_mouse_clicks(x, y, button, pressed):
    if recording and pressed:
        recorded_events.append((x, y, button, pressed))

# Function to start recording mouse events
def start_recording():
    global recording
    global recorded_events
    recorded_events = []  # Clear previous recorded events
    recording = True
    # Start the mouse event listener
    listener = mouse.Listener(on_click=record_mouse_clicks)
    listener.start()

# Function to stop recording mouse events
def stop_recording():
    global recording
    recording = False

# Function to replay recorded mouse events
def replay_recorded_events():
    for event in recorded_events:
        x, y, button, pressed = event
        pyautogui.click(x=x, y=y, button=button)

# Setting up Window
app = ctk.CTk()
app.geometry("400x150+1100+0")
app.title("HotSpots")
app.attributes("-topmost", True)

# GUI button Particulars
custom_font = ("Arial", 18, "bold")

startRun = ctk.CTkButton(app, text="Start", font=custom_font, command=start_recording, width=100, height=50)
startRun.pack(side="left", padx=10, pady=10)

stopRun = ctk.CTkButton(app, text="Stop", font=custom_font, command=stop_recording, width=100, height=50)
stopRun.pack(side="left", padx=10, pady=10)

savedRun = ctk.CTkButton(app, text="Play", font=custom_font, command=replay_recorded_events, width=100, height=50)
savedRun.pack(side="left", padx=10, pady=10)

app.mainloop()
