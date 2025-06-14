from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class product_win:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Cafe Management System")
        self.root.geometry("1223x597+300+125")
        
        self.var_category=StringVar()
        self.var_item_name=StringVar()
        self.var_item_price=StringVar()
        
    
        back=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/bg.png")
        back=back.resize((1223,597),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(back)
        
        lbl=Label(self.root,image=self.photoimage,bd=2,relief=RIDGE)
        lbl.place(x=0,y=0)
    
        
        self.Clogo=Image.open("C:/Users/janhavi/OneDrive/Desktop/Cafe/images/Cup.png")
        self.Clogo=self.Clogo.resize((40,40),Image.Resampling.LANCZOS)
        self.Clogo=ImageTk.PhotoImage(self.Clogo)
        
        lbl_title=Label(self.root,text="Product Details",image=self.Clogo,compound=LEFT,font=('Snap ITC',30,'bold'),bg="#1f77b4",fg="white")
        lbl_title.place(x=0,y=0,width=1223,height=40)
    
        frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Product Details",font=('times new roman',12,'bold'),padx=2)
        frame.place(x=10,y=50,width=400,height=400)
        
        
        category=Label(frame,text="Category:",font=('Bahnschrift',14,'bold'))
        category.place(x=6,y=8)
        
        combo_category=ttk.Combobox(frame,font=('Bahnschrift',14,'bold'),textvariable=self.var_category,width=27,state='readonly')
        combo_category['value']=("select","Coffee", "Pizza", "Burger",'Tea','Sandwich','Roll','Nachos','Pasta','Fries','Momos','Meggi')
        combo_category.current(0)
        combo_category.place(x=90,y=10)
        
        name=Label(frame,text="Item Name :",font=('Bahnschrift',14,'bold'))
        name.place(x=5,y=67)
        
        e1_name=ttk.Entry(frame,width=27,textvariable=self.var_item_name,font=('Bahnschrift',13,'bold'))
        e1_name.place(x=110,y=70)
        
        price=Label(frame,text="Item Price :",font=('Bahnschrift',14,'bold'))
        price.place(x=5,y=135)
        
        e1_price=ttk.Entry(frame,width=27,textvariable=self.var_item_price,font=('Bahnschrift',13,'bold'))
        e1_price.place(x=110,y=135)
        
      

        #button
        btn_frame=Frame(frame,bd=2,relief=RIDGE)
        btn_frame.place(x=9,y=200,width=368,height=120)
        
        Save_button=Button(btn_frame,text="Save",cursor="hand2",font=('Bahnschrift', 13, "bold"),command=self.add_data,bg="#1f77b4",fg="white",width=10)
        Save_button.place(x=40,y=10)
     

        Update_button=Button(btn_frame,text="Update",cursor="hand2",font=('Bahnschrift', 13, "bold"),command=self.update,bg="#1f77b4",fg="white",width=10)
        Update_button.place(x=200,y=10)
   
    
        Delete_button=Button(btn_frame,text="Delete",cursor="hand2",font=('Bahnschrift', 13, "bold"),command=self.delete,bg="#1f77b4",fg="white",width=10)
        Delete_button.place(x=40,y=69)
        
        reset_button=Button(btn_frame,text="Clear",cursor="hand2",font=('Bahnschrift', 13, "bold"),bg="#1f77b4",command=self.reset,fg="white",width=10)
        reset_button.place(x=200,y=69)
       
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details ",font=('times new roman',12,'bold'),padx=2)
        table_frame.place(x=418,y=50,width=790,height=400)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)  

        self.product_details_table=ttk.Treeview(table_frame,columns=("category","item_name","item_price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.product_details_table.xview)
        scroll_y.config(command=self.product_details_table.yview)
        
        self.product_details_table.heading("category",text="Category",)
        self.product_details_table.heading("item_name",text="Item Name")
        self.product_details_table.heading("item_price",text="Item Price")
        
        self.product_details_table["show"]="headings"
        
        self.product_details_table.column("category",width=130)
        self.product_details_table.column("item_name",width=130)
        self.product_details_table.column("item_price",width=130)
                        
        self.product_details_table.pack(fill=BOTH,expand=1)
        self.product_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_category.get() == "select" or self.var_category.get() == "":
            messagebox.showerror("Error", "Please select a category", parent=self.root)
            return
        elif self.var_item_name.get() == "":
            messagebox.showerror("Error", "Please enter item name", parent=self.root)
            return
        elif self.var_item_price.get() == "":
            messagebox.showerror("Error", "Please enter item price", parent=self.root)
            return
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO product VALUES (%s, %s, %s)", (
                    self.var_category.get(),
                    self.var_item_name.get(),
                    self.var_item_price.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Product has been added", parent=self.root)
                self.reset()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

                
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Janhvi04",database="cms")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from product")
                store=my_cursor.fetchall()
                if len(store)!=0:
                    self.product_details_table.delete(*self.product_details_table.get_children())
                    for i in store:
                        self.product_details_table.insert("",END,values=i)
                    conn.commit()
                conn.close() 
                
    def get_cursor(self,event=""):
        cursor_row=self.product_details_table.focus()
        content=self.product_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_category.set(row[0]),
        self.var_item_name.set(row[1]),
        self.var_item_price.set(row[2]),
        
        
    def update(self):
        if self.var_category.get() == "select" or self.var_category.get() == "":
            messagebox.showerror("Error", "Please select a product to update", parent=self.root)
            return
        elif self.var_item_name.get() == "":
            messagebox.showerror("Error", "Please enter item name", parent=self.root)
            return
        elif self.var_item_price.get() == "":
            messagebox.showerror("Error", "Please enter item price", parent=self.root)
            return
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM product WHERE category=%s", (self.var_category.get(),))
                result = my_cursor.fetchone()
                if result is None:
                    messagebox.showerror("Error", "Product not found for update", parent=self.root)
                else:
                    my_cursor.execute("UPDATE product SET item_name=%s, item_price=%s WHERE category=%s", (
                        self.var_item_name.get(),
                        self.var_item_price.get(),
                        self.var_category.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Update", "Product details updated successfully", parent=self.root)
                    self.reset()
            except Exception as es:
                messagebox.showerror("Error", f"Failed to update product: {str(es)}", parent=self.root)

            
            

    
    def delete(self):
        # Check if a product is selected
        if self.var_category.get() == "" or self.var_category.get() == "select":
            messagebox.showerror("Error", "Please select a product to delete", parent=self.root)
            return

        # Confirm delete action
        delete = messagebox.askyesno("Cafe Management System", "Do you want to delete this product details?", parent=self.root)
        if delete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Janhvi04", database="cms")
                my_cursor = conn.cursor()
                query = "DELETE FROM product WHERE category=%s"
                value = (self.var_category.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Product deleted successfully", parent=self.root)
                self.reset()
            except Exception as es:
                messagebox.showerror("Error", f"Failed to delete product: {str(es)}", parent=self.root)
        else:
            return

        
        
            
    def reset(self):
        self.var_category.set(""),
        self.var_item_name.set(""),
        self.var_item_price.set(""),
        
        
    
    
    

if __name__=="__main__":
    root=Tk()
    obj=product_win(root)
    root.mainloop()