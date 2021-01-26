# This code is written by Senadhi
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from UnzipFiles import unzipfiles
from DeleteUnwantedFiles import deleteunwantedfiles
from main import mergefiles
from CreateFolder import createfolder
from Rename_files import renamefiles


root = Tk()
root.title('Weather Data Collector')
root.iconbitmap(r'C:\Users\udari\PycharmProjects\pythonProject1\icon.png')


def onclick():
    createfolder()
    unzipfiles()
    deleteunwantedfiles()
    renamefiles()
    mergefiles()
    messagebox.showinfo(" Weather Data Collector ", "Weather Data downloaded Successfully")

def onclick1():
    messagebox.showinfo(" Weather Data Collector ", "Coming Soon")


# Create a Canvas
canvas = Canvas(root, height=500, width=700)
canvas.pack(fill="both", expand=True)

# Add Buttons
button = Button(root, text='Download Rainfall Data', font=40, command=onclick)
button_window = canvas.create_window(200, 400, anchor="nw", window=button)
button = Button(root, text='Download Ground Water Data', font=40, command=onclick1)
button_window = canvas.create_window(400, 400, anchor="nw", window=button)
button = Button(root, text='Download Streamflow Data', font=40, command=onclick1)
button_window = canvas.create_window(700, 400, anchor="nw", window=button)


def resizer(e):
    global bg, resized_bg, new_bg
    # open Image
    bg = Image.open('bg.png')
    # Resize the Image
    resized_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
    # Define the image
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add to tha canvas
    canvas.create_image(0, 0, image=new_bg, anchor="nw")
    # Add text to the canvas
    canvas.create_text(700, 300, text="Weather Data Collector", font=("Helvetica", 50), fill="#477acc")
    # Add text to the canvas
    canvas.create_text(700, 650, text="copyright 2021 ICT Project JCUB", font=("Helvetica", 15), fill="#477acc")


root.bind('<Configure>', resizer)

root.mainloop()
