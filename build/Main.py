# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/roxy/PycharmProjects/Mobile-Pi/build/assets/frame4")


def on_button_click(file_path):
    subprocess.Popen(["python3", file_path])
    sys.exit()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
#window.attributes('-fullscreen', True)
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("Wipe.py"),  # Replace with the actual path to main.py
    relief="flat"
)
button_1.place(
    x=145.0,
    y=600.0,
    width=120.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("VT.py"),
    relief="flat"
)
button_2.place(
    x=667.0,
    y=600.0,
    width=120.0,
    height=80.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    216.0,
    fill="#4DBFFF",
    outline="")

canvas.create_text(
    349.0,
    100.0,
    anchor="nw",
    text="Welcome To Mobile Pi Scanner",
    fill="#000000",
    font=("Inter", 40 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("Clam.py"),
    relief="flat"
)
button_3.place(
    x=406.0,
    y=600.0,
    width=120.0,
    height=80.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("Update.py"),
    relief="flat"
)
button_4.place(
    x=928.0,
    y=600.0,
    width=120.0,
    height=80.0
)
window.resizable(False, False)
window.mainloop()
