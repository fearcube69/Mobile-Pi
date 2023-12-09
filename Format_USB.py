#To fix :
# Sudo part of the bash script

import subprocess
import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()

# Define the function to run the bash script
def run_bash_script():
 # Define the path of the bash script
 bash_script_path = "wipe.sh"

 # Run the bash script and capture the output
 process = subprocess.Popen(["bash", bash_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 output, error = process.communicate()

 # Display the output in the text widget
 output_text.insert(tk.END, output.decode('utf-8'))

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(root)
output_text.pack()

# Create a close button to close the window
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack()

# Run the bash script when the window is created
run_bash_script()

# Run the Tkinter main loop
root.mainloop()
