
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/roxy/PycharmProjects/Mobile-Pi/build/assets/frame2")


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

canvas.create_rectangle(
    236.0,
    586.0,
    354.0,
    660.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
