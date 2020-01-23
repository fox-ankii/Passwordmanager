import tkinter as tk
import random
import sqlite3
#from datetime import date
from tkinter import messagebox
from simplegmail import Gmail

gmail = Gmail()


root = tk.Tk()
root.geometry('500x230')
root.title("Password Manager - by Ankit Agarwal")
root.configure(bg="white")
root.resizable(0,0)

root.option_add("Font","Courier 20")


e1 = tk.Entry(root,width=20,borderwidth=5)
e1.grid(row=1,column=2)

e2 = tk.Entry(root,width=20,borderwidth=5)
e2.grid(row=2,column=2)

e3 = tk.Entry(root,width=20,borderwidth=5)
e3.grid(row=3,column=2)


#today = date.today()
#datetime2 = date.strftime(today,'%d')



def generate():
    b = ["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    c = [1,2,3,4,5,6,7,8,9,0]
    d = ["!","@","#","$","%","^","&","*"]
    e = ["A","B","C","D","E","F","G","H","L","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]     
   #bbb8=random.choice(e)+random.choice(b)+random.choice(b)+random.choice(b)+str(random.choice(d))+str(random.choice(c))+str(random.choice(c))
    bbb=random.choice(e)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+str(random.choice(d))+str(random.choice(c))+str(random.choice(c))
    #bbb9=random.choice(e)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+str(random.choice(d))+str(random.choice(c))+str(random.choice(c))
    e2.insert(0,bbb)
    #mylabel = tk.Label(root,text="your password is" + bbb)
    #mylabel.grid(row=3,column=1)
    #connection = sqlite3.connect("Ankit.db")
    #cursor = connection.cursor()
    #cursor.execute("INSERT INTO customer VALUES ( ?,? )", ( bbb,e1.get()));
    #connection.commit()
    
def search():
    

    connection = sqlite3.connect("Ankit.db")
    cursor = connection.cursor()
  #print("below are the saved application's password")
  #cursor.execute("SELECT app_pswd FROM customer");
  #ans = cursor.fetchall()
  #print(ans)
  #c = input("Tell us for which application you're looking password :")
    e2.delete(0,50)
    cursor.execute("SELECT app_name FROM customer WHERE app_pswd = (?) ",(e1.get(),));
    ans1 = cursor.fetchall()

  #print(ans1)
 
  
  
    e2.insert(0,ans1)
  #mylabel4.config(text="Your password is "+ e3)
  #mylabel4.grid(row=5,column=4)
  
def save():
    
     connection = sqlite3.connect("Ankit.db")
     cursor = connection.cursor()
     #cursor.execute("CREATE TABLE customer( app_name text , app_pswd text)");
    #cursor.execute('INSERT INTO application20 VALUES(?,?)'(input2,bucket))
     cursor.execute("INSERT INTO customer VALUES ( ?,? )", ( e2.get(),e1.get()));
     connection.commit()
     e1.delete(0,50)
     e2.delete(0,50)
     messagebox.showinfo("Saved","Successfully saved")
     


def clear1():
    
     e1.delete(0,50)
     e2.delete(0,50)
   
     
def update():
  connection = sqlite3.connect("Ankit.db")
  cursor = connection.cursor()
  cursor.execute("UPDATE customer SET app_name = (?) WHERE app_pswd = (?) ",(e2.get(),e1.get()));
  connection.commit()
  e1.delete(0,50)
  e2.delete(0,50)
  messagebox.showinfo("Updated","Successfully updated")
  #ans1 = cursor.fetchall()
  #ans2=str(ans1)
  #print(ans1)
  #e2.insert(0,ans1)
  #mylabel4.config(text="Your password is "+ e3)
  #mylabel4.grid(row=5,column=4)
 

def delete():
    connection = sqlite3.connect("Ankit.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customer WHERE app_pswd = (?) ", (e1.get(),));
    connection.commit()
    e1.delete(0,50)
    e2.delete(0,50)
    messagebox.showinfo("Deleted","Successfully deleted")


    
    
    
mylabel2 = tk.Label(root,text="Application Name",width=17,padx=5,pady=5)
mylabel2.grid(row=1,column=1)

mylabel3 = tk.Label(root,text="Application userid",width=17,padx=5,pady=5)
mylabel3.grid(row=2,column=1)

mylabel3 = tk.Label(root,text="Application Password",width=17,padx=5,pady=5)
mylabel3.grid(row=3,column=1)

mylabel4 = tk.Label(root)

var = int()


mybutton = tk.Button(root,text="Generate password",fg="blue",padx=7,pady=12,width=16,command = generate)
mybutton.grid(row=10,column=1)

mybutton1 = tk.Button(root,text="Save a password",fg="blue",padx=7,pady=12,width=16,command = save)
mybutton1.grid(row=8,column=1)

mybutton2 = tk.Button(root,text="Retrieve  Password",fg="blue",padx=7,pady=12,width=16,command = search)
mybutton2.grid(row=9,column=1)

mybutton2 = tk.Button(root,text="Clear",fg="blue",padx=7,pady=12,width=16,command = clear1)
mybutton2.grid(row=10,column=2)

mybotton4 =tk.Button(root,text="Delete",fg="blue",padx=7,pady=12,width=16,command = delete)
mybotton4.grid(row=8,column=2)

mybotton5 =tk.Button(root,text="Update",fg="blue",padx=7,pady=12,width=16,command = update)
mybotton5.grid(row=9,column=2)




root.mainloop()
