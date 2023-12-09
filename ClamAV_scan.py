import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

class clam_scan():

    def scan_directory():
      # Set the directory path to /media/roxy
      # directory_path = '/media/roxy'
      directory_path = '/home/roxy/Downloads/mal'

      # Check if the path is a directory
      if os.path.isdir(directory_path):
          # Check if the script has read access to the directory
          if os.access(directory_path, os.R_OK):
              # Run the clamscan command and capture the output
              global proc
              proc = subprocess.Popen(['clamscan', '--recursive', '-l', 'clamav.log', directory_path], stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)

              # Display the output in a new window
              output_window = tk.Toplevel(root)
              output_window.title('Scan Summary')
              output_text = scrolledtext.ScrolledText(output_window)
              output_text.pack()

              # Create a new thread to read the output and display it in the window
              threading.Thread(target=read_output, args=(proc, output_text)).start()

              # Add a button to close the window and terminate the subprocess
              close_button = tk.Button(output_window, text='Close', command=lambda: close_window(proc, output_window))
              close_button.pack()
          else:
              print('The script does not have read access to the directory')
      else:
          print('The specified path is not a directory')

    def read_output(proc, output_text):
      while True:
          output = proc.stdout.readline()
          if output == '' and proc.poll() is not None:
             break
          if output:
             output_text.insert(tk.END, output)
             output_text.see(tk.END)

    def close_window(proc, window):
      # Terminate the subprocess
      proc.terminate()

      # Close the window
      window.destroy()

# Create the main window
root = tk.Tk()
root.title('ClamAV Scanner')

# Create a button to start the scan
scan_button = tk.Button(root, text='Scan Directory', command=scan_directory)
scan_button.pack()

# Start the main loop
root.mainloop()
