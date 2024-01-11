from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage, Text, END, Entry, messagebox
import sys

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame3")
#ok

ABSOLUTE_PATH = Path("/home/roxy/PycharmProjects/Mobile-Pi/build/")
#ABSOLUTE_PATH = Path("~/Mobile-Pi/build/")
ASSETS_PATH = ABSOLUTE_PATH / Path("assets/frame3")

def on_button_click(file_path):
    subprocess.Popen(["python3", file_path])
    sys.exit()

def show_warning():

   return messagebox.askokcancel("Warning", "This operation cannot be undone. Are you sure?")

def on_button_click3(file_path):

    if not messagebox.askokcancel("Warning", "This operation cannot be undone. Are you sure?"):
        print("Operation has been cancelled")
        return

    # Create a subprocess with pipes for both stdin and stdout
    process = subprocess.Popen(["bash", file_path],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)

    # Disable the text_widget for direct input
    text_widget.config(state="disabled")

    try:
        while True:
            # Read output from the subprocess
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break

            # Display the output in the text_widget
            text_widget.config(state="normal")
            text_widget.insert(END, output)
            text_widget.yview(END)  # Autoscroll to the bottom
            text_widget.config(state="disabled")
            text_widget.update()

        # Wait for the subprocess to complete
        process.wait()

        # Capture and display any errors
        error_output = process.stderr.read()
        if error_output:
            text_widget.config(state="normal")
            text_widget.insert(END, f"Error: {error_output}")
            text_widget.yview(END)  # Autoscroll to the bottom
            text_widget.config(state="disabled")
    finally:
        # Enable the text_widget for input
        text_widget.config(state="normal")

def redirect_stdout_to_text_widget():
    sys.stdout = text_widget

def restore_stdout():
    sys.stdout = sys.__stdout__

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

# Adjusted window geometry for a 1024x600 screen
window.geometry("1024x600")
window.configure(bg="#FFFFFF")
# Set the window to full screen, change true or false to enable or disable
window.attributes('-fullscreen', True)

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
    x=360.0,
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
    command=lambda: on_button_click3("wipe.sh"),
    relief="flat"
)
button_2.place(
    x=540.0,  # Adjusted x-coordinate
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

# Entry widget for user input
input_entry = Entry(
    window,
    font=("Inter", 10),
    bd=0,
    highlightthickness=0,
    relief="flat"
)
input_entry.place(x=252.0, y=400.0, width=520.0, height=30.0)  # Adjusted position and size

def on_input_enter(event):
    user_input = input_entry.get().strip()
    if user_input:
        text_widget.config(state="normal")
        text_widget.insert(END, f"\nUser: {user_input}\n")
        input_entry.delete(0, 'end')  # Clear the input entry
        text_widget.config(state="disabled")

# Bind the Enter key to the input entry
input_entry.bind('<Return>', on_input_enter)

window.resizable(False, False)
window.mainloop()