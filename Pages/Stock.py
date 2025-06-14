from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
from tkcalendar import DateEntry
import random

class stock_win:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x850+10+10")
        self.root.state('zoomed')
        self.root.title("Cafe Management System")
        self.root.config(bg="white")
        
        self.var_productid=StringVar()
        x=random.randint(0,100)
        self.var_productid.set(str(x))
        
        self.var_contact=StringVar()
        self.var_companyname=StringVar()     
        self.var_productname=StringVar()
        self.var_producttype=StringVar()
        self.var_quantity=StringVar()
        self.var_wholesaleprice=StringVar() 
        self.var_expirydate=StringVar()

        
    
        title=Label(self.root,text="Stock System",font=('Snap ITC',40,'bold'),bg="#1f77b4",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)

#############################################################frame1##########################################################################

        stock_frame =LabelFrame(self.root,text="Stock Information",font=('times new roman',17,'bold'),bg="white")
        stock_frame.place(x=30,y=100,width=680,height=500)
        
        lbl1_sup=Label(stock_frame,text="Contact No :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl1_sup.place(x=70,y=5)
        
        e1_sup=ttk.Entry(stock_frame,textvariable=self.var_contact,font=('Bahnschrift',13,'bold'))
        e1_sup.place(x=250,y=10,width=280)
        
        search_button1=Button(stock_frame,text="Search",cursor="hand2",command=self.fetch_contact,font=('Bahnschrift', 15, "bold"),bg="#1f77b4",fg="white",width=7)
        search_button1.place(x=560,y=5)
        
        lbl1_com=Label(stock_frame,text="Company Name :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl1_com.place(x=70,y=50)
        
        e1_com=ttk.Entry(stock_frame,textvariable=self.var_companyname,font=('Bahnschrift',13,'bold'))
        e1_com.place(x=250,y=55,width=280)

        lbl1_cat=Label(stock_frame,text="Product ID :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl1_cat.place(x=70,y=90)
        
        e1_id=ttk.Entry(stock_frame,textvariable=self.var_productid,font=('Bahnschrift',13,'bold'))
        e1_id.place(x=250,y=95,width=280)
        

        lbl1_item=Label(stock_frame,text="Product Type :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl1_item.place(x=70,y=130)
        
        combo1_lbl_item=ttk.Combobox(stock_frame,textvariable=self.var_productname,font=('Bahnschrift',13,'bold'),width=27,state='readonly')
        combo1_lbl_item['value']=('Coffee & Tea','Sugar,Hunny & Sweeteners','Flour & baking supplies','Dairy Products','Packaged Drinks','Backed Goods','Grains & Cereals','Spices & Herbs','Cooking oils & Vinegars','Frozen Deserts','Frozen seafood & Meat','Other')
        combo1_lbl_item.current(0)
        combo1_lbl_item.place(x=250,y=135,width=280)


        lbl1_qn=Label(stock_frame,text="Product Name :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl1_qn.place(x=70,y=170)
        
        e1_qn1=ttk.Entry(stock_frame,width=29,textvariable=self.var_producttype,font=('Bahnschrift',15,'bold'))
        e1_qn1.place(x=250,y=175,width=280)

        lbl_dis1=Label(stock_frame,text="Quantity :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl_dis1.place(x=70,y=210)
        
        e1_dis1=ttk.Entry(stock_frame,width=29,textvariable=self.var_quantity,font=('Bahnschrift',15,'bold'))
        e1_dis1.place(x=250,y=215,width=280)

        lbl_price1=Label(stock_frame,text="Wholesale Price :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl_price1.place(x=70,y=250)
        
        e1_price1=ttk.Entry(stock_frame,width=29,textvariable=self.var_wholesaleprice,font=('Bahnschrift',15,'bold'))
        e1_price1.place(x=250,y=255,width=280)

        lbl_ttl1=Label(stock_frame,text="Expiry Date :",bg='white',font=('Bahnschrift',14,'bold'),padx=2,pady=6)
        lbl_ttl1.place(x=70,y=295)
        
        e1_ttl1=DateEntry(stock_frame,textvariable=self.var_expirydate,font=("Bahnschrift",13),state="readonly",date_pattern="dd/mm/yyyy")
        e1_ttl1.place(x=250,y=300,width=280)
        
        #buttons
        Add_button1=Button(stock_frame,text="Add ",cursor="hand2",command=self.add_data,font=('Bahnschrift', 15, "bold"),bg="#1f77b4",fg="white",width=10)
        Add_button1.place(x=70,y=380)
        
        Update_button1=Button(stock_frame,text="Update",cursor="hand2",command=self.update,font=('Bahnschrift', 15, "bold"),bg="#1f77b4",fg="white",width=10)
        Update_button1.place(x=270,y=380)
        
        Delete_button1=Button(stock_frame,text="Delete",command=self.delete,cursor="hand2",font=('Bahnschrift', 15, "bold"),bg="#1f77b4",fg="white",width=10)
        Delete_button1.place(x=470,y=380)
        
#########################################  frame2 #########################################    
    
        
        bottom_frame =LabelFrame(self.root,text="Total Calculation",font=('times new roman',12,'bold'),bd=2,bg="white")
        bottom_frame.place(x=30, y=620, width=680, height=130)
        
        self.total_stock_label =Label(bottom_frame, text="Total Qauntity: 0",bg="white" ,font=("Arial", 14, "bold"))
        self.total_stock_label.place(x=20,y=20)

        self.total_cp_label = Label(bottom_frame, text="Total Wholesale Price:0 Rs", font=("Arial", 14, "bold"),bg="white")
        self.total_cp_label.place(x=20,y=70)
        
        # === Right Panel (Table) ===
        right_frame = LabelFrame(self.root,text="View Detalis", bd=2, relief=RIDGE,font=('times new roman',12,'bold'), padx=10, pady=10,bg="white" )
        right_frame.place(x=730, y=105, width=780, height=645)
        
        show_frame=Frame(right_frame,bd=2,relief=RIDGE)
        show_frame.place(x=0,y=0,width=755,height=605)
        
        scroll_x=ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(show_frame,orient=VERTICAL) 
        
        self.Stock_Detail_table=ttk.Treeview(show_frame,column=("contact","com_name","product_id","product_name","product_type",
                                                                 "quantity", "wholesale_price", "expiry_date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   
        scroll_x.pack(side='bottom',fill=X)
        scroll_y.pack (side='right',fill=Y) 
        
        scroll_x.config(command=self.Stock_Detail_table.xview)
        scroll_y.config(command=self.Stock_Detail_table.yview)
        
        self.Stock_Detail_table.heading("contact",text="Contact No")
        self.Stock_Detail_table.heading("com_name",text="Company Name")
        self.Stock_Detail_table.heading("product_id",text="Product Id")
        self.Stock_Detail_table.heading("product_name",text="Product Name")
        self.Stock_Detail_table.heading("product_type",text="Product Type")
        self.Stock_Detail_table.heading("quantity",text="Quantity")
        self.Stock_Detail_table.heading("wholesale_price",text="Wholesale Price")
        self.Stock_Detail_table.heading("expiry_date",text="Expiry Date")

        
        self.Stock_Detail_table["show"]="headings"
        
        self.Stock_Detail_table.column("contact",width=100)
        self.Stock_Detail_table.column("com_name",width=150)
        self.Stock_Detail_table.column("product_id",width=150)
        self.Stock_Detail_table.column("product_name",width=150)
        self.Stock_Detail_table.column("product_type",width=150)
        self.Stock_Detail_table.column("quantity",width=150)
        self.Stock_Detail_table.column("wholesale_price",width=150)
        self.Stock_Detail_table.column("expiry_date",width=150)


    
        
        self.Stock_Detail_table.pack(fill=BOTH,expand=1)
        self.Stock_Detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def add_data(self):
        if self.var_productname.get()=="" or self.var_quantity.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into stock values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_companyname.get(),
                                                                                self.var_productid.get(),
                                                                                self.var_productname.get(),
                                                                                self.var_producttype.get(),
                                                                                self.var_quantity.get(),
                                                                                self.var_wholesaleprice.get(),
                                                                                self.var_expirydate.get(),
                                                                                    ))
            
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_fields()
                messagebox.showinfo("Success","Stock has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
                
    
    
    def update(self):
        if self.var_productid.get() == "":
            messagebox.showerror("Error", "Please select a product to update", parent=self.root)
            return

        if (self.var_productname.get() == "" or self.var_producttype.get() == "" or
            self.var_quantity.get() == "" or self.var_wholesaleprice.get() == "" or
            self.var_expirydate.get() == ""):
            messagebox.showerror("Error", "All fields must be filled before updating", parent=self.root)
            return

        try:
            int(self.var_quantity.get())
            float(self.var_wholesaleprice.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and Price must be a number", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE stock SET product_name=%s, product_type=%s, quantity=%s, wholesale_price=%s, expiry_date=%s WHERE product_id=%s", (
                self.var_productname.get(),
                self.var_producttype.get(),
                self.var_quantity.get(),
                self.var_wholesaleprice.get(),
                self.var_expirydate.get(),
                self.var_productid.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            self.clear_fields()
            messagebox.showinfo("Update", "Stock details have been updated successfully", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

            
            
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact no",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
            my_cursor=conn.cursor()
            query="SELECT company FROM supplier WHERE contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error","This contact number is not found",parent=self.root)
            else:
                self.var_companyname.set(row[0])
            conn.commit()
            conn.close()
           
           
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM stock")
        store = my_cursor.fetchall()
        
        total_stock = 0  # Initialize total stock variable
        total_wholesale_price = 0.0  # Initialize total wholesale price variable
        
        if len(store) != 0:
            self.Stock_Detail_table.delete(*self.Stock_Detail_table.get_children())
            for i in store:
                self.Stock_Detail_table.insert("", END, values=i)
                total_stock += int(i[5])  # Assuming quantity is at index 5
                
                # Check if the wholesale price is valid before converting
                try:
                    wholesale_price = float(i[6])  # Assuming wholesale price is at index 6
                    total_wholesale_price += wholesale_price
                except (ValueError, TypeError):
                    # Handle the case where conversion fails
                    print(f"Invalid wholesale price for product ID {i[2]}: {i[6]}")  # Log the error
                    continue  # Skip this entry

        # Update the total stock and total wholesale price labels
        self.total_stock_label.config(text=f"Total Quantity: {total_stock}")
        self.total_cp_label.config(text=f"Total Wholesale Price: {total_wholesale_price} Rs")
        
        conn.commit()
        conn.close()
        

    def delete(self):
        product_id = self.var_productid.get()
        
        if product_id == "":
            messagebox.showerror("Error", "Please select a product to delete", parent=self.root)
            return

        # Check if the product ID actually exists in the database
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM stock WHERE product_id=%s", (product_id,))
            result = my_cursor.fetchone()

            if result is None:
                messagebox.showerror("Error", "No stock found with this Product ID", parent=self.root)
                conn.close()
                return

            # Confirm deletion
            delete = messagebox.askyesno("Cafe Management System", "Do you want to delete this stock detail?", parent=self.root)
            if delete:
                my_cursor.execute("DELETE FROM stock WHERE product_id=%s", (product_id,))
                conn.commit()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo("Success", "Stock entry deleted successfully", parent=self.root)

            conn.close()

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def clear_fields(self):
        self.var_contact.set("")
        self.var_companyname.set("")
        self.var_productid.set(str(random.randint(0, 100)))  # Reset to a new random ID
        self.var_productname.set("")
        self.var_producttype.set("")
        self.var_quantity.set("")
        self.var_wholesaleprice.set("")
        self.var_expirydate.set("")
            


                        
    def get_cursor(self,event=""):
        cursor_row=self.Stock_Detail_table.focus()
        content=self.Stock_Detail_table.item(cursor_row)
        row=content["values"]
        

        
        
        self.var_contact.set(row[0]),
        self.var_companyname.set(row[1]),
        self.var_productid.set(row[2]),
        self.var_productname.set(row[3]),
        self.var_producttype.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_wholesaleprice.set(row[6]),
        self.var_expirydate.set(row[7])
        

        
        
        
        
        
        

        
        


if __name__ == "__main__":
    root = Tk()
    app= stock_win(root)
    root.mainloop()

