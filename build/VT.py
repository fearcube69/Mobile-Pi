from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Text, END
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"  # Update the path accordingly


def on_button_click(file_path):
    subprocess.run(["python3", file_path])


def on_button_click2():
    # Replace this with the actual path to your text file
    text_file_path = "scan_log.txt"

    with open(text_file_path, "r") as file:
        text_content = file.read()

    # Clear existing text in the Text widget
    text_widget.delete(1.0, END)

    # Insert new text into the Text widget
    text_widget.insert(END, text_content)


# def on_button_scan():
#     # Replace this with the actual path to your text file
#     text_file_path = "../VT_scan.py"
#
#     with open(text_file_path, "r") as file:
#         text_content = file.read()


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
    text="Virus Total Scan has been Selected",
    fill="#000000",
    font=("Inter", 40 * -1)
)

# Return to the main menu button
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
    x=352.0,
    y=600.0,
    width=120.0,
    height=80.0
)

# Scan button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("../VT_scan.py"),
    relief="flat"
)
button_2.place(
    x=579.0,
    y=600.0,
    width=120.0,
    height=80.0
)

# View scan history button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click2(),
    relief="flat"
)
button_3.place(
    x=810.0,
    y=600.0,
    width=120.0,
    height=80.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    640.0,
    378.5,
    image=entry_image_1
)
text_widget = Text(
    window,
    wrap="word",
    font=("Inter", 12),
    bg="#B8E1EA",
    bd=0,
    highlightthickness=0,
    relief="flat"
)
text_widget.place(x=352.0, y=216.0, width=576.0, height=323.0)

window.resizable(False, False)
window.mainloop()
