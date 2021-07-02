from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
root = Tk()
frame = Frame(root)
frame.pack()
root.geometry('800x600')

#---------------------------------------databse----------------------------------------------------
connect= mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd=#write your password,
  database=#write your db name
)

cur = connect.cursor()
s = "SELECT * FROM Ntodo"
cur.execute(s)
cur.fetchall()
t_value=cur.rowcount
#print(t_value)
#---------------------------------------database functions---------------------------------------

def add():
  sql = "INSERT INTO Ntodo(title,dc) VALUES(%s,%s)"
  data = (t_entry.get(), d_entry.get())
  cur.execute(sql,data)
  messagebox.showinfo("inserted", "* * * Your Data Inserted * * *")
  display()


def delete():
  x_value=dlt_entry.get()
  display()
  if len(x_value) == 0:
    messagebox.showinfo("zero-record","no task available")
  else:
    sql = "DELETE FROM Ntodo WHERE t_id="+x_value
    cur.execute(sql)
    messagebox.showinfo("Delete-task","task deleted")
  display()
  
  
#---------------------------------------database functions End---------------------------------------

#---------------------------------------DISPLAY-------------------------------

def display():
  tv = ttk.Treeview(root,columns=(1,2,3), show="headings", height='5')
  tv.column('#1',anchor=CENTER)
  tv.column('#2',anchor=CENTER)
  tv.column('#3', anchor=CENTER)
  tv.place(x=0, y=320,width=800)

  tv.heading(1,text="Sr.No")
  tv.heading(2,text="Title")
  tv.heading(3,text="desc")

  sql = "SELECT * FROM Ntodo"
  cur.execute(sql)

  rows = cur.fetchall()
  for i in rows:
    tv.insert('','end',values=i)
  
#----------------------------------------DISPLAY END---------------------------

#------------------------------------fucntions---------------------------------------------------

def insert():
    if len(t_entry.get()) == 0 and len(d_entry.get()) == 0:
      messagebox.showinfo('None-Value', 'Enter Creditionals')
    else:
      add()
  
def clear():
    t_entry.delete(0,END)
    d_entry.delete(0,END)

#-------------------------------------End Function---------------------------------------------
main_label = Label(root, text="* * * TODO LIST * * *", bg='black',fg='white')
main_label.config(font=("Courier",40))
main_label.place(x=0,y=0,width=800)
lab = Label(root,bg='grey')
lab.place(x=0,y=50,width=800,height=400)


lab_txt = Label(root,text='Task Title:', bg='black', fg='white')
lab_txt.place(x=20, y=55, width=200, height=50)
lab_txt.config(font=("Courier",20))

t_entry = Entry(root, justify=LEFT,relief=FLAT)
t_entry.place(x=250, y=55, width=530, height=50)


lab_txt1 = Label(root,text='Description:', bg='black', fg='white')
lab_txt1.place(x=20, y=120, width=200, height=50)
lab_txt1.config(font=("Courier",20))

d_entry = Entry(root, justify=LEFT,relief=FLAT)
d_entry.place(x=250, y=120, width=530, height=50)

btn5 = Button(root, text='DELETE', bg='blue', fg='white', command=delete)
btn5.place(x=500, y=180) 

dlt_entry = Entry(root,justify=LEFT,relief=FLAT)
dlt_entry.place(x=600, y=180)

def show():
  w_lab = Label(root, bg="black")
  w_lab.place(x=0, y=220, width=800, height=400)
  w_lab = Label(root, bg="white", text="Your Todo's")
  w_lab.place(x=0, y=220, width=800, height=50)
  w_lab.config(font=("Courier",25))
    
  w2_lab = Label(root, bg="white")
  w2_lab.place(x=0, y=320, width=800, height=400)
      
  display()

btn1 = Button(root, text='ADD', bg='black', fg='grey', command=insert )
btn2 = Button(root, text='CLEAR', bg='black', fg='grey', command=clear)
btn3 = Button(root, text='SHOW', bg='black', fg='grey',command=show)
btn4 = Button(root, text='EXIT', bg='black', fg='grey',command=exit)

btn1.place(x=100, y=180)
btn2.place(x=200, y=180)
btn3.place(x=300, y=180)
btn4.place(x=400, y=180)

root.mainloop()