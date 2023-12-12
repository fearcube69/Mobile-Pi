from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Text, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"  # Update the path accordingly

def on_button_click(file_path):
    subprocess.Popen(["python3", file_path])

def on_button_click2():
    text_file_path = "scan_log.txt"
    with open(text_file_path, "r") as file:
        text_content = file.read()
    text_widget.delete(1.0, END)
    text_widget.insert(END, text_content)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

# Set the window size for 1024x600
window.geometry("1024x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,  # Adjusted height for the smaller screen
    width=1024,  # Adjusted width for the smaller screen
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Use adjusted coordinates and dimensions for the rectangles and text
canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    150.0,  # Adjusted height for the smaller screen
    fill="#4DBFFF",
    outline=""
)

canvas.create_text(
    200.0,  # Adjusted x-coordinate
    75.0,  # Adjusted y-coordinate
    anchor="nw",
    text="Virus Total Scan has been Selected",
    fill="#000000",
    font=("Inter", 20)  # Adjusted font size
)

# Adjusted button positions and sizes
button_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Button(
    image=button_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("Main.py"),
    relief="flat"
).place(
    x=200.0,
    y=450.0,  # Adjusted y-coordinate
    width=100.0,
    height=60.0
)

button_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Button(
    image=button_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click("VT_scan.py"),
    relief="flat"
).place(
    x=400.0,
    y=450.0,  # Adjusted y-coordinate
    width=100.0,
    height=60.0
)

button_3 = PhotoImage(file=relative_to_assets("button_3.png"))
Button(
    image=button_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click2(),
    relief="flat"
).place(
    x=600.0,
    y=450.0,  # Adjusted y-coordinate
    width=100.0,
    height=60.0
)

# Adjusted entry and text widget positions and sizes
text_widget = Text(
    window,
    wrap="word",
    font=("Inter", 12),
    bg="#B8E1EA",
    bd=0,
    highlightthickness=0,
    relief="flat"
)
text_widget.place(x=200.0, y=150.0, width=600.0, height=250.0)

window.resizable(False, False)
window.mainloop()
