# import os
# import requests
# import tkinter as tk
# from tkinter import scrolledtext, messagebox, filedialog
#
# # Replace 'your-api-key' with your actual VirusTotal API key
# api_key = '1aaf691a692202eae64669abde34e58bf2839d6138c8b6d8fe0e0b7b37137259'
#
# def scan_file():
#   # Open a dialog box to select a file
#   file_path = filedialog.askopenfilename()
#
#   # Check if the path is a file
#   if os.path.isfile(file_path):
#       # Check if the script has read access to the file
#       if os.access(file_path, os.R_OK):
#           # Send a POST request to the VirusTotal API for file scanning
#           with open(file_path, 'rb') as f:
#               files = {'file': f}
#               data = {'apikey': api_key}
#               response = requests.post('https://www.virustotal.com/api/v3/files', files=files, data=data)
#
#           # Check if the request was successful
#           if response.status_code == 200:
#               # Display the response in a new window
#               output_window = tk.Toplevel(root)
#               output_window.title('Scan Summary')
#               output_text = scrolledtext.ScrolledText(output_window)
#               output_text.insert(tk.END, response.json())
#               output_text.pack()
#           else:
#               messagebox.showerror('Error', 'Failed to scan file')
#       else:
#           messagebox.showerror('Error', 'The script does not have read access to the file')
#   else:
#       messagebox.showerror('Error', 'The specified path is not a file')
#
# # Create the main window
# root = tk.Tk()
# root.title('VirusTotal Scanner')
#
# # Create a button to start the scan
# scan_button = tk.Button(root, text='Scan File', command=scan_file)
# scan_button.pack()
#
# # Start the main loop
# root.mainloop()

# import os
# import requests
# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext
#
#
# # Function to scan file with VirusTotal API
# def scan_file():
#     # Open file dialog to select file
#     file_path = filedialog.askopenfilename()
#
#     # Check if file was selected
#     if not file_path:
#         return
#
#     # Send a POST request to the VirusTotal API for file scanning
#     with open(file_path, 'rb') as f:
#         files = {'file': f}
#         headers = {'x-apikey': '1aaf691a692202eae64669abde34e58bf2839d6138c8b6d8fe0e0b7b37137259'}
#         response = requests.post('https://www.virustotal.com/api/v3/files', files=files, headers=headers)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Display the response in a new window
#         output_window = tk.Toplevel(root)
#         output_window.title('Scan Summary')
#         output_text = scrolledtext.ScrolledText(output_window)
#         output_text.insert(tk.END, response.json())
#         output_text.pack()
#     else:
#         # Print the response from the VirusTotal API
#         print(response.json())
#         messagebox.showerror('Error', 'Failed to scan file')
#
#
# # Create main window
# root = tk.Tk()
#
# # Create button to scan file
# button_scan = tk.Button(root, text="Scan File", command=scan_file)
# button_scan.pack()
#
# # Run main loop
# root.mainloop()

import os
import requests
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import time


# Function to scan file with VirusTotal API
def scan_file():
    # Open file dialog to select file
    file_path = filedialog.askopenfilename()

    # Check if file was selected
    if not file_path:
        return

    # Send a POST request to the VirusTotal API for file scanning
    with open(file_path, 'rb') as f:
        files = {'file': f}
        headers = {'x-apikey': '1aaf691a692202eae64669abde34e58bf2839d6138c8b6d8fe0e0b7b37137259'}
        response = requests.post('https://www.virustotal.com/api/v3/files', files=files, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the id of the scan
        scan_id = response.json()['data']['id']

        # Wait for the scan to complete
        while True:
            # Send a GET request to the VirusTotal API to check the status of the scan
            response = requests.get(f'https://www.virustotal.com/api/v3/analyses/{scan_id}', headers=headers)

            # Check if the scan is complete
            if response.json()['data']['attributes']['stats']['harmless'] > 0:
                break

            # Wait for 5 seconds before checking the status again
            time.sleep(5)

        # Display the scan result in a new window
        output_window = tk.Toplevel(root)
        output_window.title('Scan Result')
        output_text = scrolledtext.ScrolledText(output_window)
        output_text.insert(tk.END, response.json())
        output_text.pack()
    else:
        # Print the response from the VirusTotal API
        print(response.json())
        messagebox.showerror('Error', 'Failed to scan file')


# Create main window
root = tk.Tk()

# Create button to scan file
button_scan = tk.Button(root, text="Scan File", command=scan_file)
button_scan.pack()

# Run main loop
root.mainloop()
