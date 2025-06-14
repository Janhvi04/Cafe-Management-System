from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Dashboard import CMS

class login_win:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("1400x850+10+10")
        self.root.state('zoomed')
        
        self.img1 = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/food.png")
        lbl_bg = Label(self.root, image=self.img1)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame = Frame(self.root, width=930, height=610, bg="#f0ffff")
        frame.place(x=470, y=100)
        
        self.img = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/img.png")
        frame_img = Label(frame, image=self.img, bg='#f0ffff')
        frame_img.place(x=10, y=40)
        
        self.icon = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/icon.png")
        fra_logo = Label(frame, image=self.icon, bg='#f0ffff')
        fra_logo.place(x=680, y=80)
        
        heading = Label(frame, text="Sign in", fg='black', bg='#f0ffff', font=('Arial', 19, 'bold'))
        heading.place(x=680, y=168)
        
        user = Label(frame, text='Username', bg='#f0ffff', font=('yu gothic ui', 17, 'bold'), fg='black')
        user.place(x=560, y=225)

        user_icon = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/user.png")
        Label(frame, image=user_icon, bg='#f0ffff').place(x=570, y=257)

        self.user_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg='#f0ffff', fg='black', font=('yu gothic ui', 14, 'bold'))
        self.user_entry.place(x=597, y=255, width=270)

        user_line = Canvas(frame, width=300, height=2.0, bg='black', highlightthickness=0)
        user_line.place(x=570, y=280)
        
        code = Label(frame, text='Password', bg='#f0ffff', font=('yu gothic ui', 17, 'bold'), fg='black')
        code.place(x=560, y=315)

        code_icon = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/lock.png")
        Label(frame, image=code_icon, bg='#f0ffff').place(x=570, y=345)

        self.code_entry = Entry(frame, highlightthickness=0, relief=FLAT, bg='#f0ffff', fg='black', font=('yu gothic ui', 14, 'bold'), show='*')
        self.code_entry.place(x=597, y=345, width=270)
        
        def show():
            hide_button = Button(frame, image=hide_image, bg='#f0ffff', bd=0, activebackground='#f0ffff', cursor='hand2', command=hide, relief=FLAT)
            hide_button.place(x=840, y=345)
            self.code_entry.config(show='')

        def hide():
            show_button = Button(frame, image=show_image, bg='#f0ffff', bd=0, activebackground='#f0ffff', cursor='hand2', command=show, relief=FLAT)
            show_button.place(x=840, y=345)
            self.code_entry.config(show='*')
            
        show_image = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Openeye.png")
        hide_image = PhotoImage(file="C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Closeeye.png")

        show_button = Button(frame, image=show_image, bg='#f0ffff', bd=0, activebackground='#f0ffff', cursor='hand2', command=show, relief=FLAT)
        show_button.place(x=840, y=345)

        code_line = Canvas(frame, width=300, height=2.0, bg='black', highlightthickness=0)
        code_line.place(x=570, y=370)
        
        log_btn = Button(frame, width=25, pady=8, text='Login', command=self.login, bg='black', fg='white', border=0, font=('Arial', 13))
        log_btn.place(x=600, y=415)

    def login(self):
        username = self.user_entry.get().strip()
        password = self.code_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        if len(username) < 4 or len(password) < 4:
            messagebox.showerror("Error", "Username and password must be at least 4 characters long")
            return
        if not username.isalnum():
            messagebox.showerror("Error", "Username must be alphanumeric (no special characters)")
            return
        import re
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@#$%^&+=!]{4,}$', password):
            messagebox.showerror("Error", "Password must contain letters and numbers")
            return

        if username == "Unicafe" and password == "cafe0011":
            messagebox.showinfo("Success", "Welcome to our cafe management system")
            self.root.withdraw()
            self.app = CMS(self, Toplevel(self.root))
        else:
            messagebox.showerror("Error", "Incorrect username or password")


if __name__ == "__main__":
    root = Tk()
    obj = login_win(root)
    root.mainloop()
