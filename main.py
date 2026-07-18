import qrcode 
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

DIR = Path(__file__).parent
QR_DIR = DIR / "Generated QRs"

window = Tk()
window.title("QR Code Generator")
window.geometry("332x468")
window.resizable(False,False)
photo = None
def generateQR():
    global photo
    qr = qrcode.QRCode()
    if UrlEntry.get() == "":
        message.config(text="Can't generate empty QR code.", fg='red')
    else:
        qr.add_data(UrlEntry.get().strip())
        img = qr.make_image()
        img.save(QR_DIR / "qrcode.png")
        message.config(text="QR has been successfully generated and saved in the 'QR Code Generator / Generated QRs' as 'qrcode.png'. Make sure to copy it as it will get erased on the next QR code generation.", fg='green')

title = Label(window, text="QR Code\nGenerator",
              font=('times new roman', 20, 'bold'))
enterUrlPrompt = Label(window, text="Enter your URL here", font=('segoe ui', 12))
UrlEntry = Entry(window, width=15)
generateButton = Button(window, text="Generate QR", command=generateQR)
message = Label(window, text="", font=('segoe ui', 11), wraplength=250)

title.place(relx=0.5, anchor='n', y=10)
enterUrlPrompt.place(relx=0.3, y=110, anchor='n')
UrlEntry.place(relx=0.7, y=113, anchor='n')
generateButton.place(relx=0.5, y=150, anchor='n')
message.place(relx=0.5, y=200, anchor='n')
window.mainloop()