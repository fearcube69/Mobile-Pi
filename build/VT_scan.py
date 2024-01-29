import os
import requests
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
from datetime import datetime
import time

class VirusTotalScanner:
    def __init__(self, root):
        self.root = root
        self.root.title('VirusTotal File Scanner')
        self.status_label = tk.Label(self.root, text='')
        self.status_label.pack()
        self.api_key = ''

    def open_file_dialog(self):
        files = filedialog.askopenfilenames(initialdir='', title='Select Files',
                                            filetypes=(('All Files', '*.*'), ('Text Files', '*.txt')))

        if files:
            self.status_label.config(text='Files selected')

            # Create a new thread to perform the VirusTotal scan
            threading.Thread(target=self.upload_and_scan, args=(files,)).start()
        else:
            self.status_label.config(text='No files selected')

    def upload_and_scan(self, files):
        # Upload the files to VirusTotal
        url = 'https://www.virustotal.com/api/v3/files'
        headers = {'x-apikey': self.api_key}

        for file in files:
            file_size = os.path.getsize(file) / (1024 * 1024)  # Get file size in MB
            if file_size > 650:
                messagebox.showwarning('File Size Exceeded',
                                       f'{os.path.basename(file)} exceeds 650MB and cannot be uploaded.')
                continue

            with open(file, 'rb') as f:
                files = {'file': f}
                response = requests.post(url, headers=headers, files=files)

            if response.status_code == 200:
                scan_id = response.json()['data']['id']
                self.status_label.config(text=f'Successfully uploaded file to VirusTotal. Scan ID: {scan_id}')
                scan_result = self.get_scan_result(scan_id)
                self.display_scan_result(scan_result, files)
                self.log_scan_result(scan_result)
            else:
                self.status_label.config(text='Error uploading file to VirusTotal')

    def get_scan_result(self, scan_id):
        # Retrieve scan result from VirusTotal
        url = f'https://www.virustotal.com/api/v3/analyses/{scan_id}'
        headers = {'x-apikey': self.api_key}

        self.status_label.config(text='Waiting for scan completion...')

        # Countdown timer, 45 seconds is the best
        for i in range(45, -1, -1):
            self.status_label.config(text=f'Waiting for scan completion... {i} seconds remaining')
            self.root.update()
            time.sleep(1)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['data']['attributes']['stats']
        else:
            self.status_label.config(text='Error retrieving scan result from VirusTotal')
            return None

    def display_scan_result(self, scan_result, files):
        if scan_result:
            original_result_text = '\n'.join(f'{key}: {value}' for key, value in scan_result.items())
            maliciousness_percentage = scan_result.get('malicious') / scan_result.get('total') if 'malicious' in scan_result and 'total' in scan_result else None
            maliciousness_text = '\nMaliciousness Percentage: {:.2%}'.format(
                maliciousness_percentage) if maliciousness_percentage is not None else ''

            # Create a Text widget to display the original and new result
            report_widget = scrolledtext.ScrolledText(self.root)
            report_widget.insert(tk.END, original_result_text + maliciousness_text)

            # Add the Text widget to the GUI
            report_widget.pack()
            self.status_label.config(text='Scan completed')

            # Prompt the user with a pop-up dialog
            user_decision = messagebox.askquestion('Delete File?', 'Do you want to delete the file?')

            # Check the user's decision
            if user_decision == 'yes':
                self.delete_files(files)

    def delete_files(self, files):
        try:
            for file in files:
                os.remove(file)
                self.status_label.config(text=f'{os.path.basename(file)} deleted successfully')
        except Exception as e:
            self.status_label.config(text=f'Error deleting files: {str(e)}')

    def log_scan_result(self, scan_result):
        # Log the scan result to a file
        log_filename = 'scan_log_old.txt'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_filename, 'a') as log_file:
            log_file.write(f'\nTimestamp: {timestamp}\n')
            if scan_result:
                log_file.write('\n'.join(f'{key}: {value}' for key, value in scan_result.items()))
                log_file.write('\n' + '-' * 50 + '\n')

    def close_window(self, window):
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
