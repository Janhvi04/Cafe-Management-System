import re
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkcalendar import DateEntry
from tkinter import messagebox

class staff_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Cafe Management System")
        self.root.geometry("1223x597+300+125")
        
        self.var_id=StringVar()
        x=random.randint(0,100)
        self.var_id.set(str(x))
        
        self.var_name=StringVar()
        self.var_gender=StringVar()     
        self.var_address=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_idProof=StringVar() 
        self.var_idnumber=StringVar()
        self.var_dateofjoining=StringVar()
        self.var_salary=StringVar()

        self.Clogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Cup.png")
        self.Clogo=self.Clogo.resize((40,40),Image.Resampling.LANCZOS)
        self.Clogo=ImageTk.PhotoImage(self.Clogo)

        lbl_title=Label(self.root,text="Staff Details",image=self.Clogo,compound=LEFT,font=('Snap ITC',30,'bold'),bg="#1f77b4",fg="white")
        lbl_title.place(x=0,y=0,width=1223,height=40)

        frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Details",font=('times new roman',12,'bold'),padx=2)
        frame.place(x=5,y=50,width=425,height=539)

        # Entries
        Label(frame,text="Staff ID:",font=('Bahnschrift',13,'bold')).grid(row=0,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_id,font=('Bahnschrift',13,'bold'),width=29).grid(row=0,column=1)

        Label(frame,text="Staff Name :",font=('Bahnschrift',13,'bold')).grid(row=1,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_name,font=('Bahnschrift',13,'bold'),width=29).grid(row=1,column=1)

        Label(frame,text="Gender :",font=('Bahnschrift',13,'bold')).grid(row=2,column=0,sticky='w',pady=6)
        combo_gender=ttk.Combobox(frame,textvariable=self.var_gender,font=('Bahnschrift',13,'bold'),width=27,state='readonly')
        combo_gender['value']=('Male','Female','Other')
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        Label(frame,text="Address :",font=('Bahnschrift',13,'bold')).grid(row=3,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_address,font=('Bahnschrift',13,'bold'),width=29).grid(row=3,column=1)

        Label(frame,text="Mobile No:",font=('Bahnschrift',13,'bold')).grid(row=4,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_mobile,font=('Bahnschrift',13,'bold'),width=29).grid(row=4,column=1)

        Label(frame,text="Email:",font=('Bahnschrift',13,'bold')).grid(row=5,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_email,font=('Bahnschrift',13,'bold'),width=29).grid(row=5,column=1)

        Label(frame,text="Id Proof Type:",font=('Bahnschrift',13,'bold')).grid(row=6,column=0,sticky='w',pady=6)
        combo_id=ttk.Combobox(frame,textvariable=self.var_idProof,font=('Bahnschrift',13,'bold'),width=27,state='readonly')
        combo_id['value']=('AdharCard','DrivingLicence','PanCard')
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        Label(frame,text="Id Number:",font=('Bahnschrift',13,'bold')).grid(row=7,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_idnumber,font=('Bahnschrift',13,'bold'),width=29).grid(row=7,column=1)

        Label(frame,text="Date of joining:",font=('Bahnschrift',13,'bold')).grid(row=8,column=0,sticky='w',pady=6)
        DateEntry(frame,textvariable=self.var_dateofjoining,font=("Bahnschrift",13),state="readonly",date_pattern="dd/mm/yyyy").grid(row=8,column=1)

        Label(frame,text="Salary:",font=('Bahnschrift',13,'bold')).grid(row=9,column=0,sticky='w',pady=6)
        ttk.Entry(frame,textvariable=self.var_salary,font=('Bahnschrift',13,'bold'),width=29).grid(row=9,column=1)

        # Buttons
        btn_frame=Frame(frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=410,width=412,height=80)

        Button(btn_frame,text="Save",command=self.Save_data,font=('Bahnschrift',13,'bold'),bg="#1f77b4",fg="white",width=10).grid(row=0,column=0,padx=1)
        Button(btn_frame,text="Update",command=self.update,font=('Bahnschrift',13,'bold'),bg="#1f77b4",fg="white",width=10).grid(row=0,column=1,padx=1)
        Button(btn_frame,text="Delete",command=self.delete,font=('Bahnschrift',13,'bold'),bg="#1f77b4",fg="white",width=10).grid(row=0,column=2,padx=1)
        Button(btn_frame,text="Reset",command=self.reset,font=('Bahnschrift',13,'bold'),bg="#1f77b4",fg="white",width=10).grid(row=0,column=3,padx=1)

        # Table frame (same as yours)
       #Tabel search
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details ",font=('times new roman',12,'bold'),padx=2)
        table_frame.place(x=435,y=50,width=786,height=539)
        
        lblSearch=Label(table_frame,text="Search By:",font=('Bahnschrift',13,'bold'),bg="#4d636d",fg='white')
        lblSearch.grid(row=0,column=0,sticky='w',padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=('Bahnschrift',13,'bold'),width=24,state='readonly')
        combo_search['value']=('Staff Id','Mobile No')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,textvariable=self.txt_search, font=('Bahnschrift', 13, "bold"), width=24)
        txtSearch.grid(row=0,column=2,padx=2)
      
        search_button=Button(table_frame,text="Search",command=self.search,cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        search_button.grid(row=0,column=3,padx=1)
        
        Show_button=Button(table_frame,text="Show All",command=self.fetch_data,cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",fg="white",width=10)
        Show_button.grid(row=0,column=4,padx=1)
        
        
        #show table
        show_frame=Frame(table_frame,bd=2,relief=RIDGE)
        show_frame.place(x=0,y=50,width=780,height=450)
        
        scroll_x=ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(show_frame,orient=VERTICAL)  
        
        self.Staff_Detail_table=ttk.Treeview(show_frame,column=("id","name","gender","address",
                                                                 "mobile","email","idProof","idnumber","dateofjoining","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   
        scroll_x.pack(side='bottom',fill=X)
        scroll_y.pack (side='right',fill=Y) 
        
        
        scroll_x.config(command=self.Staff_Detail_table.xview)
        scroll_y.config(command=self.Staff_Detail_table.yview)
        
        self.Staff_Detail_table.heading("id",text="Staff Id")
        self.Staff_Detail_table.heading("name",text="Staff Name")
        self.Staff_Detail_table.heading("gender",text="Gender")
        self.Staff_Detail_table.heading("address",text="Address")
        self.Staff_Detail_table.heading("mobile",text="Mobile No")
        self.Staff_Detail_table.heading("email",text="Email")
        self.Staff_Detail_table.heading("idProof",text="Id ProofType")
        self.Staff_Detail_table.heading("idnumber",text="Id number")
        self.Staff_Detail_table.heading("dateofjoining",text="Date of joining")
        self.Staff_Detail_table.heading("salary",text="Salary")
        
        self.Staff_Detail_table["show"]="headings"
        
        self.Staff_Detail_table.column("id",width=100)
        self.Staff_Detail_table.column("name",width=150)
        self.Staff_Detail_table.column("gender",width=100)
        self.Staff_Detail_table.column("address",width=150)
        self.Staff_Detail_table.column("mobile",width=120)
        self.Staff_Detail_table.column("email",width=130)
        self.Staff_Detail_table.column("idProof",width=110)
        self.Staff_Detail_table.column("idnumber",width=110)
        self.Staff_Detail_table.column("dateofjoining",width=110)
        self.Staff_Detail_table.column("salary",width=100)
    
        
        self.Staff_Detail_table.pack(fill=BOTH,expand=1)
        self.Staff_Detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        self.fetch_data()

    def validate_inputs(self):
        mobile = self.var_mobile.get()
        email = self.var_email.get()
        idproof = self.var_idProof.get()
        idnum = self.var_idnumber.get()
        salary = self.var_salary.get().strip()   
        
        if (
            not self.var_name.get().strip()
            or not self.var_gender.get().strip()
            or not self.var_address.get().strip()
            or not self.var_mobile.get().strip()
            or not self.var_email.get().strip()
            or not self.var_idnumber.get().strip()
            or not self.var_dateofjoining.get().strip()
            or not salary
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return False

        if not re.fullmatch(r"[6-9]\d{9}", mobile):
            messagebox.showerror("Invalid", "Enter a valid 10-digit mobile number", parent=self.root)
            return False
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid", "Enter a valid email address", parent=self.root)
            return False
        if idproof == "AdharCard" and not re.fullmatch(r"\d{12}", idnum):
            messagebox.showerror("Invalid", "Aadhar must be 12 digits", parent=self.root)
            return False
        if idproof == "PanCard" and not re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", idnum):
            messagebox.showerror("Invalid", "PAN must be in format ABCDE1234F", parent=self.root)
            return False
        if idproof == "DrivingLicence" and not re.fullmatch(r"[A-Za-z0-9]{16}", idnum):
            messagebox.showerror("Invalid", "Driving Licence must be 16 characters", parent=self.root)
            return False
        if not salary.isdigit() or int(salary) <= 0:
            messagebox.showerror("Invalid", "Salary must be a positive number without characters", parent=self.root)
            return False

        return True
    
    def Save_data(self):
        if not self.validate_inputs():
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO staff VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_id.get(),
                self.var_name.get(),
                self.var_gender.get(),
                self.var_address.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_idProof.get(),
                self.var_idnumber.get(),
                self.var_dateofjoining.get(),
                self.var_salary.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            self.clear()
            messagebox.showinfo("Success", "Staff has been added", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                
            
                
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from staff")
                store=my_cursor.fetchall()
                if len(store)!=0:
                    self.Staff_Detail_table.delete(*self.Staff_Detail_table.get_children())
                    for i in store:
                        self.Staff_Detail_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
                        
    def get_cursor(self,event=""):
        cursor_row=self.Staff_Detail_table.focus()
        content=self.Staff_Detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_address.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_idProof.set(row[6]),
        self.var_idnumber.set(row[7]),
        self.var_dateofjoining.set(row[8]),
        self.var_salary.set(row[9])
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
         
            conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
            my_cursor=conn.cursor()
            my_cursor.execute("update staff set name=%s,gender=%s,address=%s,mobile=%s,email=%s,idProof=%s,idnumber=%s,dateofjoining=%s,salary=%s where id=%s",(
                                                                                                                        
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_mobile.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_idProof.get(),
                                                                                                                        self.var_idnumber.get(),
                                                                                                                        self.var_dateofjoining.get(),
                                                                                                                        self.var_salary.get(),
                                                                                                                        self.var_id.get()
                                                                                                                        ) )
            conn.commit()
            self.fetch_data()
            conn.close()
            self.clear()
            messagebox.showinfo("Update","Staff details has been updated succesfully",parent=self.root)
    
    def delete(self):
        delete=messagebox.askyesno("Cafe Management System","Do you want to delete this staff details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
            my_cursor=conn.cursor()  
            query="delete from staff where id=%s"
            value=(self.var_id.get(),)
            my_cursor.execute(query,value) 
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        self.clear()
        
        
    def clear(self):
        self.var_id.set(str(random.randint(0, 100)))  # Reset to a new random ID
        self.var_name.set("")
        self.var_gender.set("Male")  # Reset to default value
        self.var_address.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_idProof.set("AdharCard")  # Reset to default value
        self.var_idnumber.set("")
        self.var_dateofjoining.set("")
        self.var_salary.set("")
        
    def reset(self):
        self.var_id.set(""),
        self.var_name.set(""),
        #self.var_gender.set(""),
        self.var_address.set("")
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_idProof.set(""),
        self.var_idnumber.set(""),
        self.var_dateofjoining.set(""),
        self.var_salary.set("")
        x=random.randint(0,100)
        self.var_id.set(str(x))
        
    def search(self):
        search_fields = {
            "Staff Id": "id",
            "Mobile No": "mobile"
        }

        column_name = search_fields.get(self.search_var.get())
        if not column_name:
            messagebox.showerror("Error", "Invalid search field selected", parent=self.root)
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
        my_cursor = conn.cursor()

        query = f"SELECT * FROM staff WHERE {column_name} LIKE %s"
        my_cursor.execute(query, ('%' + self.txt_search.get() + '%',))

        rows = my_cursor.fetchall()
        if rows:
            self.Staff_Detail_table.delete(*self.Staff_Detail_table.get_children())
            for row in rows:
                self.Staff_Detail_table.insert("", END, values=row)
            conn.commit()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=staff_win(root)
    root.mainloop()