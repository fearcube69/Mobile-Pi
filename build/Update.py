import subprocess
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/roxy/PycharmProjects/Mobile-Pi/build/assets/frame2")

def on_button_click(file_path):
    subprocess.run(["python3"], file_path)
    sys.exit()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    216.0,
    fill="#4DBFFF",
    outline="")

canvas.create_text(
    304.0,
    100.0,
    anchor="nw",
    text="System Update have been selected",
    fill="#000000",
    font=("Inter", 40 * -1)
)

#Return to main menu
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("Main.py"),
    relief="flat"
)
button_1.place(
    x=464.0,
    y=600.0,
    width=120.0,
    height=80.0
)

#Update button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("run update scripts"),
    relief="flat"
)
button_2.place(
    x=698.0,
    y=600.0,
    width=120.0,
    height=80.0
)
window.resizable(False, False)
window.mainloop()
