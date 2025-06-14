from tkinter import *
from PIL import Image, ImageTk
from Staff1 import staff_win
from product import product_win
from details import Details_win
from Order_type import order
from Report import CafeReports
from datetime import datetime
from tkinter import messagebox

class CMS:
    def __init__(self,login_page,root):
        self.login_page = login_page
        self.root = root
        self.root.geometry("1400x850+10+10")
        self.root.state('zoomed')
        self.root.title("Cafe Management System")
        self.root.config(bg="white")

        # Title
        self.icon_title = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Cup.png")
        title = Label(self.root, text="Cafe Management System", image=self.icon_title, compound=LEFT,
        font=('Snap ITC', 40, 'bold'), bg="#1f77b4", fg="white", anchor="w", padx=40).place(x=0, y=0, relwidth=1, height=70)



        # Current date and time
        self.lbl_clock = Label(self.root, text="", font=('times new roman', 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_time()  # Call the method to update time

        # Menu
        self.Mlogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Menu.png")
        self.Mlogo = self.Mlogo.resize((250, 250), Image.Resampling.LANCZOS)
        self.Mlogo = ImageTk.PhotoImage(self.Mlogo)

        menu = Frame(self.root, bd=2, relief=RIDGE, bg="#1f77b4")
        menu.place(x=0, y=102, width=300, height=630)

        lbl_Mlogo = Label(menu, image=self.Mlogo, bg="#1f77b4")
        lbl_Mlogo.pack(side='top', fill=X)

        self.icon_home = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/home.png")
        lbl_menu = Label(menu, text="Home", image=self.icon_home, compound=LEFT, padx=10, font=('times new roman', 20, 'bold'), bg="#1f77b4").pack(side='top', fill=X)

        self.Plogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Product.png")
        self.Plogo = self.Plogo.resize((35, 35), Image.Resampling.LANCZOS)
        self.Plogo = ImageTk.PhotoImage(self.Plogo)
        Product_btn = Button(menu, text="Product", command=self.product_Details, image=self.Plogo, compound=LEFT, padx=10, font=('times new roman', 20, 'bold'), bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        self.Blogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Bill.png")
        self.Blogo = self.Blogo.resize((25, 25), Image.Resampling.LANCZOS)
        self.Blogo = ImageTk.PhotoImage(self.Blogo)
        Bill_btn = Button(menu, text="Order", image=self.Blogo, compound=LEFT, padx=10,command=self.Order_win,font=('times new roman', 20, 'bold'), bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        self.Slogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/staff.png")
        self.Slogo = self.Slogo.resize((25, 25), Image.Resampling.LANCZOS)
        self.Slogo = ImageTk.PhotoImage(self.Slogo)
        Staff_btn = Button(menu, text="Staff", command=self.staff_Details, image=self.Slogo, compound=LEFT, padx=10, font=('times new roman', 20, 'bold'), bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        self.Sulogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/supplier.png")
        self.Sulogo = self.Sulogo.resize((25, 25), Image.Resampling.LANCZOS)
        self.Sulogo = ImageTk.PhotoImage(self.Sulogo)
        Supplier_btn = Button(menu, text="Details", image=self.Sulogo, compound=LEFT, command=self.S_Details, padx=10, font=('times new roman', 20, 'bold'), bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        self.Rlogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/report.png")
        self.Rlogo = self.Rlogo.resize((25, 25), Image.Resampling.LANCZOS)
        self.Rlogo = ImageTk.PhotoImage(self.Rlogo)
        Report_btn = Button(menu, text="Report", image=self.Rlogo, compound=LEFT, padx=10, font=('times new roman', 20, 'bold'), command=self.All_Reports,bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        self.Elogo = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Exit.png")
        self.Elogo = self.Elogo.resize((25, 25), Image.Resampling.LANCZOS)
        self.Elogo = ImageTk.PhotoImage(self.Elogo)
        Exit_btn = Button(menu, text="LogOut", image=self.Elogo,command=self.logout,compound=LEFT, padx=10, font=('times new roman', 20, 'bold'), bg='white', bd=3, cursor='hand2').pack(side='top', fill=X)

        # Footer
        lbl_Footer = Label(self.root, text="CMS-Cafe Management System | Developed by Siddhi and Janhvi\n", font=('times new roman', 12), bg="#4d636d", fg="white").pack(side='bottom', fill=X)

        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#1f77b4")
        main_frame.place(x=305, y=102, width=1227, height=630)

        self.about = Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/about.jpg")
        self.about = self.about.resize((1227, 630), Image.Resampling.LANCZOS)
        self.about = ImageTk.PhotoImage(self.about)
        about_btn = Button(main_frame, image=self.about).pack()

    def update_time(self):
        current_time = datetime.now().strftime("%d-%m-%Y       Time: %I:%M:%S %p")  # 12-hour format with AM/PM
        self.lbl_clock.config(text=f"Welcome to Cafe Management System\t\t Date: {current_time}")
        self.lbl_clock.after(1000, self.update_time)  # Update every second

    def staff_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = staff_win(self.new_window)

    def product_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = product_win(self.new_window)

    def S_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_win(self.new_window)
        
        
    def All_Reports(self):
        self.new_window = Toplevel(self.root)
        self.app = CafeReports(self.new_window)
        
    def Order_win(self):
        self.new_window = Toplevel(self.root)
        self.app = order(self.new_window)
            
    def logout(self):
            if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?", parent=self.root):
                self.root.destroy()
                self.login_page.user_entry.delete(0, END)
                self.login_page.code_entry.delete(0, END)
                self.login_page.root.deiconify()  # Show login window again



if __name__ == "__main__":
    root = Tk()
    obj = CMS(root)
    root.mainloop()