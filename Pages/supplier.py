from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import re

class supplier_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Cafe Management System")
        self.root.geometry("1223x597+300+125")

        self.Clogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Cup.png")
        self.Clogo=self.Clogo.resize((40,40),Image.Resampling.LANCZOS)
        self.Clogo=ImageTk.PhotoImage(self.Clogo)
        
        self.var_id=StringVar()
        x=random.randint(1000,9999)
        self.var_id.set(str(x))
        self.var_company=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        
        lbl_title=Label(self.root,text="Supplier Registration",image=self.Clogo,compound=LEFT,font=('Snap ITC',30,'bold'),bg="#1f77b4",fg="white")
        lbl_title.place(x=0,y=0,width=1223,height=40)
        
        frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Supplier Details",font=('times new roman',12,'bold'),padx=2)
        frame.place(x=5,y=50,width=425,height=539)
        
        com_name=Label(frame,text="Company Name:",font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        com_name.grid(row=0,column=0,sticky='w')
        e3_name=ttk.Entry(frame,width=29,textvariable=self.var_company,font=('Bahnschrift',13,'bold'))
        e3_name.grid(row=0,column=1)
        
        supplier_id=Label(frame,text="Supplier ID:",font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        supplier_id.grid(row=1,column=0,sticky='w')
        e1_id=ttk.Entry(frame,width=29,textvariable=self.var_id,font=('Bahnschrift',13,'bold'),state="readonly")
        e1_id.grid(row=1,column=1)
        
        supplier_name=Label(frame,text="Supplier Name:",font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        supplier_name.grid(row=2,column=0,sticky='w')
        e2_name=ttk.Entry(frame,width=29,textvariable=self.var_name,font=('Bahnschrift',13,'bold'))
        e2_name.grid(row=2,column=1)
        
        lblMobile=Label(frame,text="Contact No:",font=('Bahnschrift', 13,"bold"),padx=2,pady=6)
        lblMobile.grid(row=3,column=0,sticky='w')
        txtMobile=ttk.Entry(frame,textvariable=self.var_contact,font=('Bahnschrift', 13, "bold"), width=29)
        txtMobile.grid(row=3,column=1)
        
        lblEmail=Label(frame,font=('Bahnschrift', 13, "bold"),text="Email:", padx=2, pady=6)
        lblEmail.grid(row=4,column=0,sticky='W')
        txtEmail=ttk.Entry(frame,textvariable=self.var_email, font=('Bahnschrift', 13, "bold"), width=29)
        txtEmail.grid(row=4,column=1)
        
        address=Label(frame,text="Address :",font=('Bahnschrift',13,'bold'),padx=2,pady=6)
        address.grid(row=5,column=0,sticky='w')
        e3_address=ttk.Entry(frame,width=29,textvariable=self.var_address,font=('Bahnschrift',13,'bold'))
        e3_address.grid(row=5,column=1)
        
        btn_frame=Frame(frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)

        Reset_button=Button(btn_frame,text="Clear",cursor="hand2",command=self.reset,font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Reset_button.grid(row=0,column=3,padx=1)

        Update_button=Button(btn_frame,text="Update",command=self.update,cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Update_button.grid(row=0,column=1,padx=1)

        Delete_button=Button(btn_frame,text="Delete",command=self.delete,cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Delete_button.grid(row=0,column=2,padx=1)

        Add_button=Button(btn_frame,text="Save",command=self.add_data,cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Add_button.grid(row=0,column=0,padx=1)

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details ",font=('times new roman',12,'bold'),padx=2)
        table_frame.place(x=435,y=50,width=786,height=539)

        lblSearch=Label(table_frame,text="Search By:",font=('Bahnschrift',13,'bold'),bg="#4d636d",fg='white')
        lblSearch.grid(row=0,column=0,sticky='w',padx=2)

        combo_search=ttk.Combobox(table_frame,font=('Bahnschrift',13,'bold'),width=24,state='readonly')
        combo_search['value']=('Company Name','Supplier_Id')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(table_frame, font=('Bahnschrift', 13, "bold"), width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        search_button=Button(table_frame,text="Search",cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        search_button.grid(row=0,column=3,padx=1)

        Show_button=Button(table_frame,text="Show All",cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Show_button.grid(row=0,column=4,padx=1)

        show_frame=Frame(table_frame,bd=2,relief=RIDGE)
        show_frame.place(x=0,y=50,width=780,height=450)

        scroll_x=ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(show_frame,orient=VERTICAL)

        self.Supplier_Detail_table=ttk.Treeview(show_frame,column=("company","id","name","contact","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   
        scroll_x.pack(side='bottom',fill=X)
        scroll_y.pack (side='right',fill=Y)

        scroll_x.config(command=self.Supplier_Detail_table.xview)
        scroll_y.config(command=self.Supplier_Detail_table.yview)

        self.Supplier_Detail_table.heading("company",text="Company Name")
        self.Supplier_Detail_table.heading("id",text="Supplier Id")
        self.Supplier_Detail_table.heading("name",text="Supplier Name")
        self.Supplier_Detail_table.heading("contact",text="Contact No")
        self.Supplier_Detail_table.heading("email",text="Email")
        self.Supplier_Detail_table.heading("address",text="Address")

        self.Supplier_Detail_table["show"]="headings"

        self.Supplier_Detail_table.column("company",width=150)
        self.Supplier_Detail_table.column("id",width=100)
        self.Supplier_Detail_table.column("name",width=150)
        self.Supplier_Detail_table.column("contact",width=100)
        self.Supplier_Detail_table.column("email",width=150)
        self.Supplier_Detail_table.column("address",width=150)

        self.Supplier_Detail_table.pack(fill=BOTH,expand=1)
        self.Supplier_Detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        btn_img=Frame(frame,bd=2,relief=RIDGE)
        btn_img.place(x=0,y=303,width=412,height=210)

        self.Slogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/logo.jpg")
        self.Slogo=self.Slogo.resize((405,200),Image.Resampling.LANCZOS)
        self.Slogo=ImageTk.PhotoImage(self.Slogo)

        lbl_S=Label(btn_img,image=self.Slogo,bd=2,relief=RIDGE)
        lbl_S.grid(row=0,column=0)

    def validate_fields(self):
        contact = self.var_contact.get()
        if not re.fullmatch(r"\d{10}", contact):
            messagebox.showerror("Invalid Input", "Contact number must be 10 digits.", parent=self.root)
            return False
        email = self.var_email.get()
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Input", "Please enter a valid email.", parent=self.root)
            return False
        return True

    def add_data(self):
        if self.var_contact.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.validate_fields():
            return
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into supplier values(%s,%s,%s,%s,%s,%s)",(
                    self.var_company.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Supplier has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from supplier")
        store=my_cursor.fetchall()
        if len(store)!=0:
            self.Supplier_Detail_table.delete(*self.Supplier_Detail_table.get_children())
            for i in store:
                self.Supplier_Detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Supplier_Detail_table.focus()
        content=self.Supplier_Detail_table.item(cursor_row)
        row=content["values"]
        self.var_company.set(row[0])
        self.var_id.set(row[1])
        self.var_name.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_address.set(row[5])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        elif not self.validate_fields():
            return
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
            my_cursor=conn.cursor()
            my_cursor.execute("update supplier set company=%s,name=%s,contact=%s,email=%s,address=%s where id=%s",(
                self.var_company.get(),
                self.var_name.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Supplier details has been updated successfully",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Cafe Management System","Do you want to delete this supplier details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
            my_cursor=conn.cursor()
            query="delete from supplier where id=%s"
            value=(self.var_id.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return

    def reset(self):
        self.var_company.set("")
        self.var_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_id.set(str(x))

if __name__=="__main__":
    root=Tk()
    obj=supplier_win(root)
    root.mainloop()
