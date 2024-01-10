import os
import sys
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Text, END, Scrollbar, VERTICAL, messagebox

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / "assets/frame1" # Update the path accordingly

ABSOLUTE_PATH = Path("/home/roxy/PycharmProjects/Mobile-Pi/build/")
#ABSOLUTE_PATH = Path("~/Mobile-Pi/build/")
ASSETS_PATH = ABSOLUTE_PATH / Path("assets/frame1")

def on_button_click(file_path):
   subprocess.Popen(["python3", file_path])
   sys.exit()

def get_media_path(username):
   # Assuming media directory is inside the user's home directory
   home_dir = os.path.expanduser("~")
   media_path = os.path.join(home_dir, "media", username)
   return media_path

def on_button_scan():
   # Specify the path to the clamav.log file
   log_file_path = "clamav.log"

   # Display initial message
   text_widget.insert(END, "Scanning has been initiated...\n")
   text_widget.update() # Update the widget to immediately show the message

   # Run ClamAV scan and capture the output
   clamav_output = subprocess.run(["clamscan", "-r", "/home/roxy/Documents"], capture_output=True, text=True)

   # Display the scan output in the Text widget
   text_widget.insert(END, clamav_output.stdout)

   # Append the scan output to the clamav.log file
   with open(log_file_path, "a") as log_file:
       log_file.write(clamav_output.stdout)

def on_button_log():
   # Replace this with the actual path to your text file
   text_file_path = "clamav.log"

   with open(text_file_path, "r") as file:
       text_content = file.read()

   # Clear existing text in the Text widget
   text_widget.delete(1.0, END)

   # Insert new text into the Text widget
   text_widget.insert(END, text_content)

def relative_to_assets(path: str) -> Path:
   return ASSETS_PATH / Path(path)

def toggle_fullscreen(event=None):
   state = not window.attributes('-fullscreen')
   window.attributes('-fullscreen', state)

window = Tk()

window.geometry("1024x600")
window.configure(bg="#FFFFFF")

# Set the window to full screen, change true or false to enable or disable
window.attributes('-fullscreen', True)

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
canvas.create_rectangle(
   0.0,
   0.0,
   1024.0,
   216.0,
   fill="#4DBFFF",
   outline=""
)

canvas.create_text(
   295.0,
   100.0,
   anchor="nw",
   text="Clam AV Scan has been Selected",
   fill="#000000",
   font=("Inter", 30 * -1) # Adjusted font size
)

# Adjusted button placements for a 1024x600 screen
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
   x=244.0,
   y=450.0,
   width=120.0,
   height=80.0
)

button_image_2 = PhotoImage(
   file=relative_to_assets("button_2.png"))
button_2 = Button(
   image=button_image_2,
   borderwidth=0,
   highlightthickness=0,
   command=lambda: on_button_scan(),
   relief="flat"
)
button_2.place(
   x=460.0,
   y=450.0,
   width=120.0,
   height=80.0
)

button_image_3 = PhotoImage(
   file=relative_to_assets("button_3.png"))
button_3 = Button(
   image=button_image_3,
   borderwidth=0,
   highlightthickness=0,
   command=lambda: on_button_log(),
   relief="flat"
)
button_3.place(
   x=660.0,
   y=450.0,
   width=120.0,
   height=80.0
)

# Create a Text widget to display the text
text_widget = Text(
   window,
   wrap="word",
   font=("Inter", 12),
   bg="#B8E1EA",
   bd=0,
   highlightthickness=0,
   relief="flat"
)

scrollbar = Scrollbar(window, orient=VERTICAL, command=text_widget.yview)
scrollbar.place(x=770.0, y=216.0, height=225.0) # Adjusted Scrollbar position

text_widget['yscrollcommand'] = scrollbar.set

text_widget.place(x=244.0, y=216.0, width=536.0, height=225.0) # Adjusted Text widget size

window.resizable(False, False)
window.mainloop()
