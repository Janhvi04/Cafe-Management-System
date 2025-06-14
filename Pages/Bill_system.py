from tkinter import*
from tkinter import ttk
from PIL  import Image,ImageTk
from datetime import datetime
import mysql.connector
import random,os
from tkinter import messagebox
from datetime import datetime
import tempfile



class Bill:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1223x597+300+125")
        self.root.title("Cafe Management System")  # Title of window
        self.root.config(bg="white") 
        
        lbl_title=Label(self.root,text="Billing Window", font=('Snap ITC', 40, 'bold'), bg="#1f77b4", fg="white")
        lbl_title.place(x=0,y=0,width=1223,height=60)
        
        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=60,width=1223,height=535)
        
        
        ########## variable #############
        self.c_name=StringVar()
        self.c_contact=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.item_name=StringVar()
        self.price_var=IntVar()
        self.quantity=IntVar()
        self.discount=IntVar()
        self.sub_total=StringVar()
        self.total=StringVar()
        self.discount1=StringVar()
        
        
        
        ######Customer frame #########
        
        cust_frame =LabelFrame(Main_frame, text="Customer Details",font=('times new roman',14,'bold'),bg="white")
        cust_frame.place(x=10,y=3,width=500,height=130)
        
        lbl_name=Label(cust_frame,text="Customer Name :",bg='white',font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        lbl_name.place(x=40,y=7)
        
        e2_name=ttk.Entry(cust_frame,width=29,textvariable=self.c_name,font=('Bahnschrift',13,'bold'))
        e2_name.place(x=180,y=12)

        lbl_no=Label(cust_frame,text="Contact Number :",bg='white',font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        lbl_no.place(x=40,y=50)
        
        e2_no=ttk.Entry(cust_frame,width=29,textvariable=self.c_contact,font=('Bahnschrift',13,'bold'))
        e2_no.place(x=180,y=55)
        
        
        
        ########## Product frame ##############
        pro_frame =LabelFrame(Main_frame, text="Product",font=('times new roman',14,'bold'),bg="white")
        pro_frame.place(x=10,y=135,width=500,height=240)

        self.conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
        self.my_cursor = self.conn.cursor()
        self.my_cursor.execute("SELECT DISTINCT category FROM product")
        categories = self.my_cursor.fetchall()

        self.selected_category = StringVar()

        lbl_cat = Label(pro_frame, text="Select Category :", bg='white', font=('Bahnschrift', 13, 'bold'), padx=2, pady=6)
        lbl_cat.place(x=20, y=0)

        self.combo_lbl_cat = ttk.Combobox(pro_frame,font=('Bahnschrift', 13, 'bold'), width=27, textvariable=self.selected_category, state='readonly')
        self.combo_lbl_cat['values'] = [category[0] for category in categories]  # Populate with category names
        self.combo_lbl_cat.place(x=160, y=5)
        self.combo_lbl_cat.bind("<<ComboboxSelected>>", self.fetch_items)  # Bind event



        lbl_item = Label(pro_frame, text="Item Name :", bg='white', font=('Bahnschrift', 13, 'bold'), padx=2, pady=6)
        lbl_item.place(x=20, y=40)

        self.combo_lbl_item = ttk.Combobox(pro_frame, font=('Bahnschrift', 13, 'bold'), width=27, textvariable=self.item_name, state='readonly')
        self.combo_lbl_item.place(x=160, y=50)

        
        
        lbl_price=Label(pro_frame,text="Price :",bg='white',font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        lbl_price.place(x=20,y=80)
        
        self.combo_lbl_item.bind("<<ComboboxSelected>>", self.fetch_price)  # Bind event for item selection

        
        self.e1_price = ttk.Entry(pro_frame, width=29, font=('Bahnschrift', 13, 'bold'), textvariable=self.price_var, state='readonly')
        self.e1_price.place(x=160, y=90)


        lbl_qn=Label(pro_frame,text="Quantity :",bg='white',font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        lbl_qn.place(x=20,y=120)
        
        e1_qn=ttk.Entry(pro_frame,width=29,textvariable=self.quantity,font=('Bahnschrift',13,'bold'))
        e1_qn.place(x=160,y=130)

        lbl_dis=Label(pro_frame,text="Discount :",bg='white',font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        lbl_dis.place(x=20,y=160)
        
        e1_dis=ttk.Entry(pro_frame,width=29,textvariable=self.discount,font=('Bahnschrift',13,'bold'))
        e1_dis.place(x=160,y=170)
        
        
        ###Iamge1###
        img_1=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Counter.jpg")
        img_1=img_1.resize((500,370),Image.Resampling.LANCZOS)
        self.photo_img1=ImageTk.PhotoImage(img_1)
        
        
        lbl_img1=Label(self.root,image=self.photo_img1)
        lbl_img1.place(x=520,y=80,width=300,height=365)
        
        
        ######### Time And Date #########
        Time_Date=LabelFrame(Main_frame,text="On", font=('times new roman', 14, 'bold'),bg="white", fg="Black")
        Time_Date.place(x=820,y=5,width=385,height=60)
        
        # Get current date and time
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.current_time = datetime.now().strftime("%I:%M %p")  # Change to 12-hour format

        # Update the date and time labels
        Label(Time_Date, text=f"Date: {self.current_date}", font=('times new roman', 14, 'bold'), bg="white").place(x=10, y=0, height=30)
        Label(Time_Date, text=f"Time: {self.current_time}", font=('times new roman', 14, 'bold'), bg="white").place(x=220, y=0, height=30)
        
        
        
        ########### search Bill Number ########
        
        btn_search=Frame(Main_frame,bd=2,bg="white")
        btn_search.place(x=820,y=70,width=385,height=40)
        
        self.lblbill=Label(btn_search,text="Bill Number:",fg="white",bg="#1f77b4",font=('Bahnschrift',12,'bold'),padx=2,pady=6)
        self.lblbill.grid(row=0,column=0,sticky=W,padx=1)
        
        e1_billsearch=ttk.Entry(btn_search,textvariable=self.search_bill,width=15,font=('Bahnschrift',12,'bold'))
        e1_billsearch.grid(row=0,column=1,sticky=W,padx=2)
        
        self.btnsearch=Button(btn_search,text="Search",font=('times new roman',12,'bold'),command=self.find_bill,bg="#1f77b4",fg="white",cursor="hand2",width=13)
        self.btnsearch.grid(row=0,column=2,padx=4)
        
        
        
        
        #### Right bill window #####
        
        Right_Labelframe=LabelFrame(Main_frame,text="Bill Window", font=('times new roman', 14, 'bold'),bg="white", fg="Black")
        Right_Labelframe.place(x=820,y=110,width=385,height=409)
        
        
        scroll_y=Scrollbar(Right_Labelframe,orient=VERTICAL)
        self.textarea=Text(Right_Labelframe,yscrollcommand=scroll_y.set,bg="white",fg="black",font=('times new roman',13,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        
        
        #lbl_Footer = Label(self.root, text="CMS-Cafe Management System | Developed by Siddhi and Janhvi\n", font=('times new roman', 12), bg="#4d636d", fg="white").pack(side='bottom', fill=X)
        
         ########## bill counter frame ##############
        counter_frame =LabelFrame(Main_frame, text="Bill Counter",font=('times new roman',14,'bold'),bg="white")
        counter_frame.place(x=10,y=375,width=800,height=144)
        
        
        sub_total=Label(counter_frame,text="Sub Total:",bg='white',font=('Bahnschrift',12,'bold'),padx=2,pady=6)
        sub_total.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        e1_sub=ttk.Entry(counter_frame,width=15,textvariable=self.sub_total,font=('Bahnschrift',12,'bold'))
        e1_sub.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        dis_total=Label(counter_frame,text="Discount:",bg='white',font=('Bahnschrift',12,'bold'),padx=2,pady=6)
        dis_total.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        e1_dis=ttk.Entry(counter_frame,width=15,textvariable=self.discount1,font=('Bahnschrift',12,'bold'))
        e1_dis.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        total=Label(counter_frame,text="Total:",bg='white',font=('Bahnschrift',12,'bold'),padx=2,pady=6)
        total.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        e1_total=ttk.Entry(counter_frame,width=15,textvariable=self.total,font=('Bahnschrift',12,'bold'))
        e1_total.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        
        ##### Button frame ##########
        
        btn_frame=Frame(counter_frame,bd=2,bg="white")
        btn_frame.place(x=260,y=0)
        
        
        self.btnaddtocart=Button(btn_frame,text="Add To Cart",font=('times new roman',14,'bold'),command=self.AddItem,bg="#1f77b4",fg="white",cursor="hand2")
        self.btnaddtocart.grid(row=0,column=0,padx=10,pady=10)
        
        self.btngenerate=Button(btn_frame,text="Generate Bill",font=('times new roman',14,'bold'),command=self.gen_bill,bg="#1f77b4",fg="white",cursor="hand2")
        self.btngenerate.grid(row=0,column=1,padx=60,pady=10)
        
        self.btnsavebill=Button(btn_frame,text="Save Bill",width=10,font=('times new roman',14,'bold'),command=self.save_bill,bg="#1f77b4",fg="white",cursor="hand2")
        self.btnsavebill.grid(row=0,column=2,pady=10)
        
        self.btnprint=Button(btn_frame,text="Print",width=10,font=('times new roman',14,'bold'),command=self.iprint,bg="#1f77b4",fg="white",cursor="hand2")
        self.btnprint.grid(row=1,column=0)
        
        self.btnclear=Button(btn_frame,text="Clear",width=10,font=('times new roman',14,'bold'),command=self.clear,bg="#1f77b4",fg="white",cursor="hand2")
        self.btnclear.grid(row=1,column=1)
        
        self.btnexit=Button(btn_frame,text="Back",width=10,font=('times new roman',14,'bold'),command=self.back,bg="#1f77b4",fg="white",cursor="hand2")
        self.btnexit.grid(row=1,column=2)
        self.welcome()
        
        self.l=[]
        
            
    
    def AddItem(self):
        if self.item_name.get() == "":
            messagebox.showerror("Error", "Please select the item name",parent=self.root)
            return

        if self.quantity.get() <= 0:
            messagebox.showerror("Error", "Quantity must be greater than 0",parent=self.root)
            return

        if self.discount.get() < 0:
            messagebox.showerror("Error", "Discount cannot be negative",parent=self.root)
            return

        self.n = self.price_var.get()
        self.quantity_value = self.quantity.get()
        self.discount_value = self.discount.get()

        total_price = self.quantity_value * self.n
        discount_amount = (self.discount_value / 100) * total_price
        final_price = total_price - discount_amount

        self.l.append((self.item_name.get(), self.quantity_value, final_price))
        self.textarea.insert(END, f"\n {self.item_name.get()}\t\t{self.quantity_value}\t\t{final_price:.2f}")
        self.update_subtotal()
            
    def update_subtotal(self):
        subtotal = sum(item[2] for item in self.l)
        self.sub_total.set(f"{subtotal:.2f}")
        total_discount = sum((self.discount.get() / 100) * item[2] for item in self.l)
        total = subtotal - total_discount
        self.total.set(f"{total:.2f}")
        self.discount1.set(f"{total_discount:.2f}")
            
        
    def gen_bill(self):
        if not self.l:
            messagebox.showerror("Error", "Please Add To Cart Item",parent=self.root)
            return

        if self.c_name.get() == "" or self.c_contact.get() == "":
            messagebox.showerror("Error", "Customer details are required",parent=self.root)
            return

        if not self.c_contact.get().isdigit() or len(self.c_contact.get()) != 10:
            messagebox.showerror("Error", "Contact number must be 10 digits",parent=self.root)
            return

        self.welcome()
        for item in self.l:
            item_name, quantity, final_price = item
            self.textarea.insert(END, f"\n {item_name}\t\t{quantity}\t\t{final_price:.2f}")
        
        self.textarea.insert(END, "\n====================================")
        self.textarea.insert(END, f"\n Sub Total:\t\t\t{self.sub_total.get()}")
        self.textarea.insert(END, f"\n Discount:\t\t\t{self.discount1.get()}")
        self.textarea.insert(END, f"\n Total:\t\t\t{self.total.get()}")
        self.textarea.insert(END, "\n====================================")
            
    def save_bill(self):
        if self.c_name.get() == "" or self.c_contact.get() == "":
            messagebox.showerror("Error", "Customer details are required before saving bill")
            return

        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op >0:
            self.bill_data=self.textarea.get(1.0,END)
            with open(f"C:/Users/janhavi/OneDrive/Desktop/Cafe/Pages/Bills/{str(self.bill_no.get())}.txt",'w') as f1:
                f1.write(self.bill_data)
            messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        
        
    def find_bill(self):
        found = "no"
        bill_no = self.search_bill.get().strip()
        bill_dir = "C:/Users/janhavi/OneDrive/Desktop/Cafe/Pages/Bills"

        if not bill_no:
            messagebox.showerror("Input Error", "Please enter a bill number to search.")
            return

        for i in os.listdir(bill_dir):
            if i.split(".")[0] == bill_no:
                with open(os.path.join(bill_dir, i), 'r') as f1:
                    self.textarea.delete(1.0, END)
                    for d in f1:
                        self.textarea.insert(END, d)
                found = "yes"
                break  # Exit the loop once the bill is found

        if found == 'no':
            messagebox.showerror("Error", "Invalid Bill No.")

                
                
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_contact.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.item_name.set("")
        self.price_var.set(0)
        self.quantity.set(0)
        self.l=[]
        self.discount.set(0)    
        self.sub_total.set("")
        self.discount1.set("")
        self.total.set("")
        self.welcome()
        
      
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"          Welcome To Cafe Management System")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Contact Number:{self.c_contact.get()}")
        self.textarea.insert(END,f"\n Order Type: Dine")
        self.textarea.insert(END, f"\n Date: {self.current_date}")  # Insert current date
        self.textarea.insert(END, f"\t\t\t Time: {self.current_time}")  # Insert current time
        
        self.textarea.insert(END,"\n====================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n====================================")
        
        
        
    def fetch_items(self, event):
        """Fetch items based on selected category and populate Item combo box."""
        category = self.selected_category.get()
        self.my_cursor.execute("SELECT item_name FROM product WHERE category = %s", (category,))
        items = self.my_cursor.fetchall()
        item_list = [item[0] for item in items]

        self.combo_lbl_item['values'] = item_list  # Update item combo box
        
        
    def fetch_price(self, event):
        """Fetch price based on selected item and display it."""
        item_name = self.item_name.get()
        if item_name:
            self.my_cursor.execute("SELECT item_price FROM product WHERE item_name = %s", (item_name,))
            price = self.my_cursor.fetchone()
            if price:
                self.price_var.set(price[0])  # Update price entry field
            else:
                self.price_var.set("")  # Clear if no price found
                
    def back(self):
        self.root.withdraw()  # Hides the current window instead of destroying it
        import Order_type
        new_window = Toplevel(self.root)  # Create a new window on top of current app
        obj = Order_type.order(new_window)
                        
        
if __name__=="__main__":
    root=Tk()
    obj=Bill(root)
    root.mainloop()
        
        
        