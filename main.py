# This code is written by Senadhi

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import schedule
import time
from UnzipFiles import unzipfiles
from DeleteUnwantedFiles import deleteunwantedfiles
from CreateFolder import createfolder
from RemoveColumn import removeColumn
from DownloadZip import downloadfiles
from DeleteZipfiles import deletezipfiles

root = Tk()
root.title('Weather Data Collector')


def onclick():
    messagebox.showinfo(" Weather Data Collector ", "Rainfall Data Downloading... This may take few minutes... Do not "
                                                    "close the browsers ")
    createfolder()
    # downloadfiles()
    unzipfiles()
    deletezipfiles()
    deleteunwantedfiles()
    removeColumn()
    messagebox.showinfo(" Weather Data Collector ", "You can find the Downloaded Rainfall Data in "
                                                    "C:/Users/Public/Weather Data Collector")


def onclick1():
    messagebox.showinfo(" Weather Data Collector ", "Coming Soon")


# Create a Canvas
canvas = Canvas(root, height=500, width=700)
canvas.pack(fill="both", expand=True)
canvas.grid(columnspan=3, rowspan=3)

# Add Buttons
button1 = Button(root, text="Download Rainfall Data", font=("Raleway", 11), bg="#477acc", fg="white", height=2,
                 width=20,
                 command=onclick)
button1.grid(column=0, row=1)
button1 = Button(root, text="Download Ground Water Data", font=("Raleway", 11), bg="#477acc", fg="white", height=2,
                 width=22,
                 command=onclick1)
button1.grid(column=1, row=1)
button1 = Button(root, text="Download Streamflow Data", font=("Raleway", 11), bg="#477acc", fg="white", height=2,
                 width=20,
                 command=onclick1)
button1.grid(column=2, row=1)

# Add Header
header = Label(root, text="Weather Data Collector", font=("Raleway", 45), fg="#477acc")
header.grid(columnspan=3, column=0, row=0)

# Add Footer
footer = Label(root, text="copyright 2021 ICT Project JCUB", font=("Raleway", 10), fg="#477acc")
footer.grid(columnspan=3, column=0, row=2)


# button = Button
# button_window = canvas.create_window(200, 400, anchor="nw", window=button)
# button = Button(root, text='Download Ground Water Data', font=40, command=onclick1)
# button_window = canvas.create_window(400, 400, anchor="nw", window=button)
# button = Button(root, text='Download Streamflow Data', font=40, command=onclick1)
# button_window = canvas.create_window(700, 400, anchor="nw", window=button)

def resizer(e):
    global bg, resized_bg, new_bg
    # open Image
    bg = Image.open("C://Users//udari//PycharmProjects//pythonProject1//bg.png")
    # Resize the Image
    resized_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
    # Define the image
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add to tha canvas
    canvas.create_image(0, 0, image=new_bg, anchor="nw")

    # Add text to the canvas
    # canvas.create_text(350, 200, text="Weather Data Collector", font=("Helvetica", 45), fill="#477acc")
    # Add text to the canvas
    # canvas.create_text(350, 350, text="copyright 2021 ICT Project JCUB", font=("Helvetica", 10), fill="#477acc")


root.bind('<Configure>', resizer)

root.mainloop()


def updatefiles():
    # downloadfiles()
    unzipfiles()
    deletezipfiles()
    deleteunwantedfiles()
    removeColumn()


# updatefiles() will run every Monday at 6.00 am
schedule.every().monday.at('06:00').do(updatefiles)

while 1:
    schedule.run_pending()
    time.sleep(1)
