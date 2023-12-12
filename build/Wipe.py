from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Text, simpledialog, END
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame3")

def on_button_click(file_path):
    subprocess.Popen(["python3", file_path])
    sys.exit()

def on_button_click3(file_path):
    try:
        result = subprocess.check_output(["bash", file_path], universal_newlines=True)
        text_widget.delete(1.0, END)
        text_widget.insert(END, result)
    except subprocess.CalledProcessError as e:
        text_widget.delete(1.0, END)
        text_widget.insert(END, f"Error: {e.output}")

def redirect_stdout_to_text_widget():
    sys.stdout = text_widget

def restore_stdout():
    sys.stdout = sys.__stdout__

def get_password():
    password = simpledialog.askstring("Password", "Enter password:")
    return password

def check_password(password):
    stored_password = "your_stored_password"
    return password.strip() == stored_password

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1024x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,  # Adjusted height
    width=1024,  # Adjusted width
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    144.0,  # Adjusted height
    fill="#4DBFFF",
    outline=""
)

canvas.create_text(
    200.0,
    70.0,
    anchor="nw",
    text="USB wipe mode has been selected",
    fill="#000000",
    font=("Inter", 25 * -1)  # Adjusted font size
)

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
    x=372.0,
    y=450.0,  # Adjusted y-coordinate
    width=120.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [redirect_stdout_to_text_widget(), on_button_click3("wipe.sh"), restore_stdout()],
    relief="flat"
)
button_2.place(
    x=532.0,  # Adjusted x-coordinate
    y=450.0,  # Adjusted y-coordinate
    width=120.0,
    height=80.0
)

text_widget = Text(
    window,
    wrap="word",
    font=("Inter", 10),  # Adjusted font size
    bg="#B8E1EA",
    bd=0,
    highlightthickness=0,
    relief="flat"
)
text_widget.place(x=252.0, y=144.0, width=520.0, height=250.0)  # Adjusted position and size

window.resizable(False, False)
window.mainloop()
