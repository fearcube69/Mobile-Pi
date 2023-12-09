import customtkinter as ctk
import subprocess

# Create the main window
app = ctk.CTk()

# Set the title of the window
app.title("Welcome to Mobile Pi Scanner")

# Set the color of the widgets
ctk.set_default_color_theme("blue")

# Create a label with the title in the middle of the window
title_label = ctk.CTkLabel(app, text="Welcome to Mobile Pi Scanner", fg_color='white', bg_color='blue',
                           font=("Helvetica", 20))
title_label.pack(pady=20)


# Define a function to execute a Python script
def execute_script(script):
    subprocess.call(["python3", script])


# Create four buttons at the bottom of the window
button1 = ctk.CTkButton(app, text="Format USB", command=lambda: execute_script("Format_USB.py"))
button2 = ctk.CTkButton(app, text="Clam AV scan", command=lambda: execute_script("ClamAV_scan.py"))
button3 = ctk.CTkButton(app, text="Virustotal scan", command=lambda: execute_script("VT_scan.py"))
button4 = ctk.CTkButton(app, text="Update", command=lambda: execute_script("Update.py"))

# Pack the buttons at the bottom of the window with 20px space between them
button1.pack(side=ctk.LEFT, fill=ctk.X, padx=20)
button2.pack(side=ctk.LEFT, fill=ctk.X, padx=20)
button3.pack(side=ctk.LEFT, fill=ctk.X, padx=20)
button4.pack(side=ctk.LEFT, fill=ctk.X, padx=20)

# Start the main loop
app.mainloop()
