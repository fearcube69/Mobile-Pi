import os
import requests
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
from datetime import datetime

class VirusTotalScanner:

    def __init__(self, root):
        self.root = root
        self.root.title('VirusTotal File Scanner')
        self.status_label = tk.Label(self.root, text='')
        self.status_label.pack()
        self.api_key = '1aaf691a692202eae64669abde34e58bf2839d6138c8b6d8fe0e0b7b37137259'  # Replace with your VirusTotal API key

    def open_file_dialog(self):
        files = filedialog.askopenfilenames(initialdir='', title='Select Files',
                                             filetypes=(('All Files', '*.*'), ('Text Files', '*.txt')))

        if files:
            self.status_label.config(text='Files selected')

            # Zip the selected files if size is less than 650MB
            with zipfile.ZipFile('../selected_files.zip', 'w') as zipf:
                for file in files:
                    file_size = os.path.getsize(file) / (1024 * 1024)  # Get file size in MB
                    if file_size < 650:
                        zipf.write(file, arcname=os.path.basename(file))
                    else:
                        messagebox.showwarning('File Size Exceeded',
                                               f'{os.path.basename(file)} exceeds 650MB and cannot be zipped.')

            self.status_label.config(text='Selected files zipped successfully')

            # Create a new thread to perform the VirusTotal scan
            threading.Thread(target=self.upload_and_scan).start()
        else:
            self.status_label.config(text='No files selected')

    def upload_and_scan(self):
        # Upload the zip file to VirusTotal
        url = 'https://www.virustotal.com/api/v3/files'
        headers = {'x-apikey': self.api_key}

        with open('../selected_files.zip', 'rb') as file:
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            scan_id = response.json()['data']['id']
            self.status_label.config(text=f'Successfully uploaded file to VirusTotal. Scan ID: {scan_id}')
            scan_result = self.get_scan_result(scan_id)
            self.display_scan_result(scan_result)
            self.log_scan_result(scan_result)
        else:
            self.status_label.config(text='Error uploading file to VirusTotal')

    def get_scan_result(self, scan_id):
        # Retrieve scan result from VirusTotal
        url = f'https://www.virustotal.com/api/v3/analyses/{scan_id}'
        headers = {'x-apikey': self.api_key}

        self.status_label.config(text='Waiting for scan completion...')

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['data']['attributes']['stats']
        else:
            self.status_label.config(text='Error retrieving scan result from VirusTotal')
            return None

    def display_scan_result(self, scan_result):
        if scan_result:
            result_text = '\n'.join(f'{key}: {value}' for key, value in scan_result.items())

            # Create a Text widget to display the result
            report_widget = scrolledtext.ScrolledText(self.root)
            report_widget.insert(tk.END, result_text)

            # Add the Text widget to the GUI
            report_widget.pack()
            self.status_label.config(text='Scan completed')

    def log_scan_result(self, scan_result):
        # Log the scan result to a file
        log_filename = 'scan_log.txt'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_filename, 'a') as log_file:
            log_file.write(f'\nTimestamp: {timestamp}\n')
            if scan_result:
                log_file.write('\n'.join(f'{key}: {value}' for key, value in scan_result.items()))
                log_file.write('\n' + '-' * 50 + '\n')

    def close_window(self, window):
        # Terminate the subprocess
        self.proc.terminate()

        # Close the window
        window.destroy()


# Create the main window
root = tk.Tk()
virus_total_scanner = VirusTotalScanner(root)

# Create a button to open the file dialog and start the scan
scan_button = tk.Button(root, text='Scan Files with VirusTotal', command=virus_total_scanner.open_file_dialog)
scan_button.pack()

# Start the main loop
root.mainloop()
