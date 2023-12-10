from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/roxy/PycharmProjects/Mobile-Pi/build/assets/frame1")

def on_button_click(file_path):
    subprocess.run(["python3", file_path])

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
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
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    216.0,
    fill="#4DBFFF",
    outline=""
)

canvas.create_text(
    295.0,
    100.0,
    anchor="nw",
    text="Clam AV Scan have been Selected",
    fill="#000000",
    font=("Inter", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("/home/roxy/PycharmProjects/Mobile-Pi/build/Main.py"),  # Replace with the actual path to main.py
    relief="flat"
)
button_1.place(
    x=344.0,
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=580.0,
    y=600.0,
    width=120.0,
    height=80.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=816.0,
    y=600.0,
    width=120.0,
    height=80.0
)

canvas.create_rectangle(
    344.0,
    216.0,
    920.0,
    541.0,
    fill="#B8E1EA",
    outline=""
)

window.resizable(False, False)
window.mainloop()
