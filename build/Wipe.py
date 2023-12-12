from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Scrollbar, Text, END
import sys
from tkinter import simpledialog
from getpass import getpass

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame3")


def on_button_click(file_path):
    subprocess.Popen(["python3", file_path])
    sys.exit()

def on_button_wipe():
    script_path = "wipe.sh"  # Replace with the actual path to your shell script
#    password = get_password()
#    if password and check_password(password):
#
#
#
#         try:
#             result = subprocess.check_output(["bash", script_path], universal_newlines=True)
#             text_widget.insert(END, result)  # Use END to insert the result at the end of the Text widget
#         except subprocess.CalledProcessError as e:
#             text_widget.insert(END, f"Error: {e.output}")
#     else:
#         text_widget.insert(END, "Incorrect password or no password entered.\n")
#
# def get_password():
#     password = simpledialog.askstring("Password", "Enter password:")
#     return password
#
# def check_password(password):
#     # Add your logic to check the password, e.g., compare it with a stored password
#     stored_password = "your_stored_password"
#     return password.strip() == stored_password

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
    outline="")

canvas.create_text(
    300.0,
    100.0,
    anchor="nw",
    text="USB wipe mode has been selected",
    fill="#000000",
    font=("Inter", 40 * -1)
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
    x=472.0,
    y=600.0,
    width=120.0,
    height=80.0
)

# button to wipe the file
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_wipe(),
    relief="flat"
)
button_2.place(
    x=687.0,
    y=600.0,
    width=120.0,
    height=80.0
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
