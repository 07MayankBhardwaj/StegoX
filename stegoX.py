import stegano
from stegano import lsb
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import string
import hashlib
import secrets

root = Tk()
root.title("StegoX - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#333333") 

filename = None  


def generate_key():
    """Generate a unique private key."""
    letters = string.ascii_letters
    digits = string.digits
    key = ''.join(random.choices(letters + digits, k=16))
    return key


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG File", ".jpg"), ("All file", ".*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    global lbl  
    lbl = Label(f, image=img, bg="black")
    lbl.place(x=40, y=10)
    lbl.image = img

def Hide():
    global secret
    message = text1.get("1.0", END)
    key = secrets.token_hex(16) 
    hash_key = hashlib.sha256(key.encode()).hexdigest()  
    with open("Private_key.txt", "w") as f:
        f.write(hash_key)  
    with open("Public_key.txt", "w") as f:
        f.write(hash_key)
    secret = lsb.hide(filename, message)  
    secret.save("./Output/hidden.png")

def Show():
    global filename
    with open("Private_key.txt", "r") as f:
        hash_key = f.read()

    with open("Public_key.txt", "r") as f:
        public_key = f.read()

    if hash_key == public_key:
        try:
            filename = "./Output/hidden.png"
            clear_message = lsb.reveal(filename)
            text1.delete("1.0", END)
            text1.insert(END, clear_message)
        except ValueError:
            text1.delete("1.0", END)
            text1.insert(END, "Error: Incorrect Key")
    else:
        text1.delete("1.0", END)
        text1.insert(END, "Error: Incorrect Public Key")

def save():
    secret.save("./Output/hidden.png")

#icon
image_icon = PhotoImage(file="./assets/favicon.png")  
root.iconphoto(False, image_icon)

# logo
logo = PhotoImage(file="./assets/logo.png")
Label(root, image=logo, bg="#333333").place(x=10, y=0)

Label(root, text="STEGOX", bg="#2f4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first Frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lb1 = Label(f, bg="black")  
lb1.place(x=40, y=10)

# second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)  
text1.configure(yscrollcommand=scrollbar1.set)

# third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3,text="Open Image",width=10, height=2,font="arial 14 bold",bg="#1e88e5", fg="white",command=showimage) .place (x=20,y=30)
Button(frame3, text="Save Image",width=10, height=2, font="arial 14 bold",bg="#1e88e5", fg="white",command=save) .place (x=180, y=30)
Label(frame3, text="Picture, Image, Photo File",bg="#2f4155", fg="yellow").place(x=20,y=5)

# fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button (frame4, text="Hide Data",width=10,height=2,font="arial 14 bold",bg="#1e88e5", fg="white",command=Hide) .place (x=20, y=30)
Button(frame4,text="Show",width=10,height=2,font="arial14bold",bg="#1e88e5", fg="white",command=Show).place(x=180,y=30)
Label (frame4, text="Picture, Image, Photo File",bg="#2f4155", fg="yellow").place(x=20,y=5)

root.mainloop()