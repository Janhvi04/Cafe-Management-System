from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import os
import pandas as pd

class CafeReports:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.state('zoomed')
        self.root.geometry("1400x850+10+10")
        
        
        window_width = 1600
        label_width = 1600 
        x_position = (window_width - label_width)

        t1 = Label(self.root, text="REPORT", font=("times new roman", 40, "bold"), bg="#1f77b4", fg="white", bd=4, relief=RIDGE)
        t1.place(x=x_position, y=0, width=label_width, height=70)
        
        f2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        f2.place(x=0, y=70, width=1570, height=900)
        back=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/bg.png")
        back=back.resize((1523,660),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(back)
        
        lbl=Label(f2,image=self.photoimage,bd=2,relief=RIDGE)
        lbl.place(x=0,y=0)

        b1 = Button(self.root, text="Staff", font=("arial", 20, "bold"), bg="#1f77b4", fg="white", width=10, height=3, command=self.show_staff_report)
        b1.place(x=70, y=130)

        b2 = Button(self.root, text="Supplier", font=("arial", 20, "bold"), bg="#1f77b4", fg="white", width=10, height=3,command=self.show_supplier_report)
        b2.place(x=70, y=290)
        
        b3 = Button(self.root, text="Stock", font=("arial", 20, "bold"), bg="#1f77b4", fg="white", width=10, height=3,command=self.show_stock_report)
        b3.place(x=70, y=440)
        

        
        lbl_Footer = Label(self.root, text="CMS-Cafe Management System | Developed by Siddhi and Janhvi\n", font=('times new roman', 15), bg="#4d636d", fg="white").pack(side='bottom', fill=X)

        
        
        
        
    def show_staff_report(self):
        self.clear_frame()
        self.create_staff_report()
        
    def show_supplier_report(self):
        self.clear_frame()
        self.create_supplier_report()
        
    def show_stock_report(self):
        self.clear_frame()
        self.create_stock_report()
        
    
        
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.__init__(self.root)  # Reinitialize the main frame
        
    def create_staff_report(self):
        f2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        f2.place(x=330, y=130, width=1200, height=550)

        # Add a heading for the staff report
        heading_label = Label(f2, text="Staff Report", font=("arial", 24, "bold"), bg="white", fg="black")
        heading_label.pack(pady=10)  # Add some padding for better spacing

        # Generate PDF Button
        pdf_button = Button(f2, text="Generate PDF", font=("arial", 14, "bold"), bg="green", fg="white", command=self.generate_staff_excel)
        pdf_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Treeview", background="lightblue", foreground="black", rowheight=25, fieldbackground="lightblue")
        style.map("Treeview", background=[("selected", "blue")])  # Change selected row color

        # Scrollbars
        scroll_x = ttk.Scrollbar(f2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(f2, orient=VERTICAL)

        # Treeview
        self.staff_table = ttk.Treeview(f2, columns=("id","name","gender","address",
                                                                 "mobile","email","idProof","idnumber","dateofjoining","salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure Scrollbars
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)

        # Treeview Headings
        self.staff_table.heading("id",text="Staff Id")
        self.staff_table.heading("name",text="Staff Name")
        self.staff_table.heading("gender",text="Gender")
        self.staff_table.heading("address",text="Address")
        self.staff_table.heading("mobile",text="Mobile No")
        self.staff_table.heading("email",text="Email")
        self.staff_table.heading("idProof",text="Id ProofType")
        self.staff_table.heading("idnumber",text="Id number")
        self.staff_table.heading("dateofjoining",text="Date of joining")
        self.staff_table.heading("salary",text="Salary")
        
        self.staff_table["show"]="headings"
        
        self.staff_table.column("id",width=100)
        self.staff_table.column("name",width=150)
        self.staff_table.column("gender",width=100)
        self.staff_table.column("address",width=150)
        self.staff_table.column("mobile",width=120)
        self.staff_table.column("email",width=130)
        self.staff_table.column("idProof",width=110)
        self.staff_table.column("idnumber",width=110)
        self.staff_table.column("dateofjoining",width=110)
        self.staff_table.column("salary",width=100)

        self.record_staff()

        # Pack Treeview
        self.staff_table.pack(fill=BOTH, expand=TRUE)
        

    def create_supplier_report(self):
        f2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        f2.place(x=330, y=130, width=1200, height=550)


        # Add a heading for the staff report
        heading_label = Label(f2, text="Supplier Report", font=("arial", 24, "bold"), bg="white", fg="black")
        heading_label.pack(pady=10)  # Add some padding for better spacing

        # Generate PDF Button
        pdf_button = Button(f2, text="Generate PDF", font=("arial", 14, "bold"), bg="green", fg="white", command=self.generate_supplier_excel)
        pdf_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Treeview", background="lightblue", foreground="black", rowheight=25, fieldbackground="lightblue")
        style.map("Treeview", background=[("selected", "blue")])  # Change selected row color

        # Scrollbars
        scroll_x = ttk.Scrollbar(f2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(f2, orient=VERTICAL)

        # Treeview
        self.supplier_table = ttk.Treeview(f2, columns=("company","id","name","contact","email",
                                                                 "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure Scrollbars
        scroll_x.config(command=self.supplier_table.xview)
        scroll_y.config(command=self.supplier_table.yview)

        # Treeview Headings
        self.supplier_table.heading("company",text="Company Name")
        self.supplier_table.heading("id",text="Supplier Id")
        self.supplier_table.heading("name",text="Supplier Name")
        self.supplier_table.heading("contact",text="Contact No")
        self.supplier_table.heading("email",text="Email")
        self.supplier_table.heading("address",text="Address")
 
        self.supplier_table["show"]="headings"
        
        self.supplier_table.column("company",width=150)
        self.supplier_table.column("id",width=100)
        self.supplier_table.column("name",width=150)
        self.supplier_table.column("contact",width=100)
        self.supplier_table.column("email",width=150)
        self.supplier_table.column("address",width=150)

        self.record_supplier()

        # Pack Treeview
        self.supplier_table.pack(fill=BOTH, expand=TRUE)
        
        
        
    def create_stock_report(self):
        f2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        f2.place(x=330, y=130, width=1200, height=550)


        # Add a heading for the staff report
        heading_label = Label(f2, text="Stock Report", font=("arial", 24, "bold"), bg="white", fg="black")
        heading_label.pack(pady=10)  # Add some padding for better spacing

        # Generate PDF Button
        pdf_button = Button(f2, text="Generate PDF", font=("arial", 14, "bold"), bg="green", fg="white", command=self.generate_stock_excel)
        pdf_button.pack(pady=10)

        style = ttk.Style()
        style.configure("Treeview", background="lightblue", foreground="black", rowheight=25, fieldbackground="lightblue")
        style.map("Treeview", background=[("selected", "blue")])  # Change selected row color

        # Scrollbars
        scroll_x = ttk.Scrollbar(f2, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(f2, orient=VERTICAL)

        # Treeview
        self.stock_table = ttk.Treeview(f2, columns=("contact","com_name","product_id","product_name","product_type",
                                                                 "quantity", "wholesale_price", "expiry_date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure Scrollbars
        scroll_x.config(command=self.stock_table.xview)
        scroll_y.config(command=self.stock_table.yview)

        # Treeview Headings
        self.stock_table.heading("contact",text="Contact No")
        self.stock_table.heading("com_name",text="Company Name")
        self.stock_table.heading("product_id",text="Product Id")
        self.stock_table.heading("product_name",text="Product Name")
        self.stock_table.heading("product_type",text="Product Type")
        self.stock_table.heading("quantity",text="Quantity")
        self.stock_table.heading("wholesale_price",text="Wholesale Price")
        self.stock_table.heading("expiry_date",text="Expiry Date")

        
        self.stock_table["show"]="headings"
        
        self.stock_table.column("contact",width=100)
        self.stock_table.column("com_name",width=150)
        self.stock_table.column("product_id",width=150)
        self.stock_table.column("product_name",width=150)
        self.stock_table.column("product_type",width=150)
        self.stock_table.column("quantity",width=150)
        self.stock_table.column("wholesale_price",width=150)
        self.stock_table.column("expiry_date",width=150)
        self.record_stock()

        # Pack Treeview
        self.stock_table.pack(fill=BOTH, expand=TRUE)
        
        
    
        
        
    def fetch_staff_data(self):
        conn = mysql.connector.connect(host="localhost", user="root",password="Janhvi04",database="cms", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT  id,name,gender,address,mobile,email,idProof,idnumber,dateofjoining,salary FROM staff")
        records = my_cursor.fetchall()
        conn.close()
        return records
    
    
    def fetch_supplier_data(self):
        conn = mysql.connector.connect(host="localhost", user="root",password="Janhvi04",database="cms", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT  company,id,name,contact,email,address FROM supplier")
        records = my_cursor.fetchall()
        conn.close()
        return records
    
    def fetch_stock_data(self):
        conn = mysql.connector.connect(host="localhost", user="root",password="Janhvi04",database="cms", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT  contact,com_name,product_id,product_name,product_type,quantity,wholesale_price,expiry_date FROM stock")
        records = my_cursor.fetchall()
        conn.close()
        return records
    
    
    def record_staff(self):
        for i in self.staff_table.get_children():
            self.staff_table.delete(i)

        records = self.fetch_staff_data()

        for record in records:
            self.staff_table.insert("", "end", values=record)
            
    def record_supplier(self):
        for i in self.supplier_table.get_children():
            self.supplier_table.delete(i)

        records = self.fetch_supplier_data()

        for record in records:
            self.supplier_table.insert("", "end", values=record)
            
    def record_stock(self):
        for i in self.stock_table.get_children():
            self.stock_table.delete(i)

        records = self.fetch_stock_data()

        for record in records:
            self.stock_table.insert("", "end", values=record)
            

        

    def generate_staff_excel(self):
        records = self.fetch_staff_data()
        df = pd.DataFrame(records, columns=["Id", "Name", "Gender", "Address", "Mobile", "Email", "IdProof", "Id Number", "Date of Joining", "Salary"])
        excel_file = "staff_report.xlsx"
        df.to_excel(excel_file, index=False)

        try:
            os.startfile(excel_file)
        except AttributeError:
            print(f"✅ Excel file saved as '{excel_file}'. Please open it manually.")
        
        
    def generate_supplier_excel(self):
        records = self.fetch_supplier_data()
        df = pd.DataFrame(records, columns=["Company Name", "Supplier Id", "Supplier Name", "Contact No", "Email", "Address"])
        excel_file = "supplier_report.xlsx"
        df.to_excel(excel_file, index=False)

        try:
            os.startfile(excel_file)
        except AttributeError:
            print(f"✅ Excel file saved as '{excel_file}'. Please open it manually.")

    def generate_stock_excel(self):
        records = self.fetch_stock_data()
        df = pd.DataFrame(records, columns=["Contact No", "Company Name", "Product Id", "Product Name", "Product Type", "Quantity", "Wholesale Price", "Expiry Date"])
        excel_file = "stock_report.xlsx"
        df.to_excel(excel_file, index=False)

        try:
            os.startfile(excel_file)
        except AttributeError:
            print(f"✅ Excel file saved as '{excel_file}'. Please open it manually.")


        

        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = CafeReports(root)
    root.mainloop()
