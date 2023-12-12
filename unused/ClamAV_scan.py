import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading


class clam_scan():

    def __init__(self):
        self.proc = None

    def scan_directory(self):
        # Display "Scanning have been initiated" as the first output
        output_window = tk.Toplevel(root)
        output_window.title('Scan Summary')
        output_text = scrolledtext.ScrolledText(output_window)
        output_text.pack()
        output_text.insert(tk.END, "Scanning have been initiated\n")

        # Set the directory path to /media/roxy
        # directory_path = '/media/roxy'
        directory_path = '/home/roxy/Downloads/mal'

        # Check if the path is a directory
        if os.path.isdir(directory_path):
            # Check if the script has read access to the directory
            if os.access(directory_path, os.R_OK):
                # Run the clamscan command and capture the output
                self.proc = subprocess.Popen(['clamscan', '--recursive', '-l', 'clamav.log', directory_path],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.STDOUT)

                # Create a new thread to read the output and display it in the window
                threading.Thread(target=self.read_output, args=(output_text,)).start()

                # Add a button to close the window and terminate the subprocess
                close_button = tk.Button(output_window, text='Close', command=lambda: self.close_window(output_window))
                close_button.pack()
            else:
                print('The script does not have read access to the directory')
        else:
            print('The specified path is not a directory')

    def read_output(self, output_text):
        while True:
            output = self.proc.stdout.readline()
            if output == b'' and self.proc.poll() is not None:
                break
            if output:
                output_text.insert(tk.END, output.decode('utf-8'))
                output_text.see(tk.END)

    def close_window(self, window):
        # Terminate the subprocess
        self.proc.terminate()

        # Close the window
        window.destroy()


# Create the main window
root = tk.Tk()
root.title('ClamAV Scanner')

# Create an instance of the clam_scan class
scanner = clam_scan()

# Create a button to start the scan
scan_button = tk.Button(root, text='Scan Directory', command=scanner.scan_directory)
scan_button.pack()

# Start the main loop
root.mainloop()
