import tkinter as tk
from tkinter import ttk
import subprocess
import re
# import ClamAV_scan
#import Format_USB
# import Update
# import VT_scan

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Wipe_USB, ClamAV_scan, VT_scan, System_Update):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Main Menu", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=5, padx=20, pady=10)

        button1 = ttk.Button(self, text="Wipe USB",
                             command=lambda: controller.show_frame(Wipe_USB))

        # putting the button in its place by
        # using grid
        button1.grid(row=21, column=2, padx=5, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Clam AV",
                             command=lambda: controller.show_frame(ClamAV_scan))

        # putting the button in its place by
        # using grid
        button2.grid(row=21, column=4, padx=5, pady=10)

        # button for VT scan option
        button3 = ttk.Button(self, text="VT",
                             command=lambda: controller.show_frame(VT_scan))

        button3.grid(row=21, column=6, padx=5, pady=10)

        # button for updating the system
        button4 = ttk.Button(self, text="Update",
                             command=lambda: controller.show_frame(System_Update))

        button4.grid(row=21, column=8, padx=5, pady=10)


        button4 = ttk.Button(self, text="Update",
                             command=lambda: controller.show_frame(System_Update))

        button4.grid(row=21, column=8, padx=5, pady=10)
# second window frame page1
import subprocess
import re
import tkinter as tk
from tkinter import ttk

class Wipe_USB(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)

       # Title lable
       label = ttk.Label(self, text="USB wipe mode", font=LARGEFONT)
       label.grid(row=0, column=5, padx=20, pady=10)

        #buttons
       button1 = ttk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame(StartPage))
       button1.grid(row=3, column=1, padx=5, pady=10)

       button2 = ttk.Button(self, text="USB wipe", command=self.run_format_usb)
       button2.grid(row=3, column=2, padx=5, pady=10)

   def run_format_usb(self):
       subprocess.Popen(["python", "Format_USB.py"])

       # button3 = ttk.Button(self, text="Check Format USB",
       #                      command=self.check_usb_mount)
       # button3.grid(row=3, column=3, padx=5, pady=10)
       #
       # button4 = ttk.Button(self, text="Page 4",
       #                     command=lambda: controller.show_frame(VT_scan))
       # button4.grid(row=3, column=4, padx=5, pady=10)

       self.check_usb_mount()

# Check USB
   def check_usb_mount(self):
       result = subprocess.run(['df', '-hT'], stdout=subprocess.PIPE)
       output = result.stdout.decode('utf-8')
       for line in output.split('\n'):
           if '/media/roxy' in line:
               match = re.search(r'(\w+)\s+/media/roxy', line)
               if match:
                  fs_type = match.group(1)
                  print(f"USB device is mounted to /media/roxy with file system type {fs_type}")
               else:
                  print("USB device is mounted to /media/roxy but file system type could not be determined")
               break
       else:
           print("USB device is not mounted to /media/roxy")



# third window frame page2
class ClamAV_scan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Main Menu", font=LARGEFONT)

        # Back to Main menu

        label.grid(row=0, column=5, padx=20, pady=10)

        button1 = ttk.Button(self, text="Main Menu",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=1, padx=5, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Begin Scan",
                             command=lambda: controller.show_frame())

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=2, padx=5, pady=10)

        # button for VT scan option
        button3 = ttk.Button(self, text="View Scan Reports",
                             command=lambda: controller.show_frame())

        button3.grid(row=3, column=3, padx=5, pady=10)

        # button for updating the system
        button4 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.show_frame())

        button4.grid(row=3, column=4, padx=5, pady=10)

class VT_scan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Main Menu", font=LARGEFONT)

        # Back to Main menu
        label.grid(row=0, column=5, padx=20, pady=10)

        button1 = ttk.Button(self, text="Main Menu",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=1, padx=5, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame())

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=2, padx=5, pady=10)

        # button for VT scan option
        button3 = ttk.Button(self, text="Page 3",
                             command=lambda: controller.show_frame(VT_scan))

        button3.grid(row=3, column=3, padx=5, pady=10)

        # button for updating the system
        button4 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.show_frame(VT_scan))

        button4.grid(row=3, column=4, padx=5, pady=10)

class System_Update(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Main Menu", font=LARGEFONT)

        # Main menu

        label.grid(row=0, column=5, padx=20, pady=10)

        button1 = ttk.Button(self, text="Main Menu",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=1, padx=5, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame())

        # # putting the button in its place by
        # # using grid
        # button2.grid(row=3, column=2, padx=5, pady=10)
        #
        # # button for VT scan option
        # button3 = ttk.Button(self, text="Page 3",
        #                      command=lambda: controller.show_frame(VT_scan))
        #
        # button3.grid(row=3, column=3, padx=5, pady=10)
        #
        # # button for updating the system
        # button4 = ttk.Button(self, text="Page 4",
        #                      command=lambda: controller.show_frame(VT_scan))
        #
        # button4.grid(row=3, column=4, padx=5, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
