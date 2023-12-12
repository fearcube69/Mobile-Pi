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

window.geometry("1024x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=1024,
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
    command=lambda: on_button_click("Wipe.py"),
    relief="flat"
)
button_1.place(
    x=164,
    y=400,
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
    x=740,
    y=400,
    width=120.0,
    height=80.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    144.0,
    fill="#4DBFFF",
    outline=""
)

canvas.create_text(
    274.0,
    50.0,
    anchor="nw",
    text="Welcome To Mobile Pi Scanner",
    fill="#000000",
    font=("Inter", 30 * -1)
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
    x=452,
    y=400,
    width=120.0,
    height=80.0
)

# Commented out the fourth button to fit within the screen size
# button_image_4 = PhotoImage(
#     file=relative_to_assets("button_4.png"))
# button_4 = Button(
#     image=button_image_4,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: on_button_click("Update_.py"),
#     relief="flat"
# )
# button_4.place(
#     x=740.0,
#     y=400.0,
#     width=120.0,
#     height=80.0
# )

window.resizable(False, False)
window.mainloop()