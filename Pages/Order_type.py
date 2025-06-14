from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Bill_system import Bill   # You already imported this class
from Take_Bill import Bill1


class order:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1223x597+300+125")

        # Keep a reference to the background image
        self.bg_image = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/food.png")
        self.bg_image = self.bg_image.resize((1223, 597), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        lbl = Label(self.root, image=self.bg_photo, bd=2, relief=RIDGE)
        lbl.place(x=0, y=0)

        frame = Frame(self.root, width=500, height=500, bg="#f0ffff")
        frame.place(x=650, y=50)

        lbl1 = Label(frame, text="Order Type", font=('times new roman', 27, 'bold'), bg="white")
        lbl1.place(x=170, y=20)

        # Keep a reference to the logo image
        self.logo_image = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/demo2.jpg")
        self.logo_image = self.logo_image.resize((390, 300), Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        lbl_logo = Label(frame, image=self.logo_photo, bd=2, relief=RIDGE)
        lbl_logo.place(x=50, y=80)

        btn = tk.Button(frame, text="Dine", command=self.dine_page,
                        font=('Arial', 27), relief='raised', bd=4)
        btn.place(x=130, y=400)

        btn1 = tk.Button(frame, text="Take", command=self.take_page,
                         font=('Arial', 27), relief='raised', bd=5)
        btn1.place(x=260, y=400)

        
        
  
        
        
    def dine_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Bill(self.new_window)  # Open the Bill class GUI in new window
        
    def take_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Bill1(self.new_window)  # Open the Bill class GUI in new window

if __name__ == "__main__":
    root = Tk()
    obj = order(root)
    root.mainloop()
