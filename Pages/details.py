from tkinter import*
from PIL import Image,ImageTk
from Stock import stock_win
from supplier import supplier_win


class Details_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Cafe Management System")
        self.root.geometry("1223x597+300+125")
        
        back=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/bg.png")
        back=back.resize((1223,597),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(back)
        
        lbl=Label(self.root,image=self.photoimage,bd=2,relief=RIDGE)
        lbl.place(x=0,y=0)
        
        self.Clogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Cup.png")
        self.Clogo=self.Clogo.resize((50,50),Image.Resampling.LANCZOS)
        self.Clogo=ImageTk.PhotoImage(self.Clogo)
        
        lbl_title=Label(self.root,text="Details",image=self.Clogo,compound=LEFT,font=('Snap ITC',30,'bold'),bg="#1f77b4",fg="white")
        lbl_title.place(x=0,y=0,width=1223,height=60)
        
        self.Slogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/logo.jpg")
        self.Slogo=self.Slogo.resize((250,250),Image.Resampling.LANCZOS)
        self.Slogo=ImageTk.PhotoImage(self.Slogo)
        
        lbl_S=Button(self.root,image=self.Slogo,command=self.supplier_Details,bd=2,relief=RIDGE)
        lbl_S.place(x=300,y=200)
        
        self.Stlogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/stocklogo.jpg")
        self.Stlogo=self.Stlogo.resize((250,250),Image.Resampling.LANCZOS)
        self.Stlogo=ImageTk.PhotoImage(self.Stlogo)
        
        lbl_Stock=Button(self.root,image=self.Stlogo,command=self.stock_Details,bd=2,relief=RIDGE)
        lbl_Stock.place(x=700,y=200)
        
        

    

                
    def stock_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=stock_win(self.new_window)
        
    def supplier_Details(self):
        self.new_window=Toplevel(self.root)
        self.app=supplier_win(self.new_window)
        


if __name__=="__main__":
    root=Tk()
    obj=Details_win(root)
    root.mainloop()
        
