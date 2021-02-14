from tkinter import *
from tkinter import messagebox as mb

#--------------------------------------------------------table---------------------------------------------------------------------------------------------
import sqlite3 as sq
'''
con = None
try:
con =  sq.connect("student.db")
print("conneced")
cur = con.cursor()
cur.execute("CREATE TABLE student(Rno integer, Name text, Marks integer)")
con.commit()
except Exception as e:
print("creation issue-->", e)
finally:
if con is not None:
con.close()
#print("disconnected")

'''
#--------------------------------------------------------functions--------------------------------------------------------------------------------------
def add():
adst.deiconify()
win.withdraw()

def view():
vist.deiconify()
win.withdraw()
con = None
try:
con = sq.connect("student.db")
cur = con.cursor()
cur.execute("SELECT * FROM student")
res= cur.fetchall()
info = " "
for r in res:
info = info+ "rollno : " + r[0] + "name" + r[1] + "marks" + r[2]
listbox.insert(end, info)
except Exception as e:
print(e)
def update():
upst.deiconify()
win.withdraw()
def delete():
dest.deiconify()
win.withdraw()
def charts():
pass

def asave():
print("hi")
con = None
rno = 0
name = ""
marks = 0
try:
rno = rno_ae.get()
rnos = int(rno)
name= name_ae.get()
print(name)
mark = marks_ae.get()
marks = int(marks)
print(marks)
con = sq.connect("student.db")
cur = con.cursor()
sql = "INSERT INTO mystudent VALUES('%d','%s','%d')"
args = (rnos, name, marks)
cur.execute(sql %args)
print("saved")
con.commit()
except Exception as e:
print("save issue--->",e)
finally:
print(rno, name,marks)
def aback():
win.deiconify()
adst.withdraw()
def vback():
win.deiconify()
vist.withdraw()
def usave():
pass
def uback():
win.deiconify()
upst.withdraw()
def dsave():
pass
def dback():
win.deiconify()
dest.withdraw()

#---------------------------------------------------------home page----------------------------------------------------------------------------------
win = Tk()
win.title("Home Page")
win.geometry("300x400")
#win.config(bg = "light green")
#add fonts and bg to title and window????

lbl = Label(win, text = "Welcome to Student Management System ",font = ("arial", 10, "bold") )
lbl.pack(pady = "10")
addbtn = Button(win, width = "10", text = "ADD",font = ("arial", 10, "bold"), background = "light grey", command = add)
addbtn.pack(pady = "14")
viewbtn = Button(win, width = "10",text = "VIEW ",font = ("arial", 10, "bold"), background = "light grey", command = view)
viewbtn.pack(pady = "14")
updbtn = Button(win, width = "10", text = "UPDATE ",font = ("arial", 10, "bold"), background = "light grey", command = update)
updbtn.pack(pady = "14")
dltbtn = Button(win, width = "10", text = "DELETE ",font = ("arial", 10, "bold"), background = "light grey", command = delete)
dltbtn.pack(pady = "14")
chartbtn = Button(win, width = "10", text = "CHARTS",font = ("arial", 10, "bold"), background= "light grey", command = charts)
chartbtn.pack(pady = "14")
loc = Label(win, bd = '4' ,relief = "flat", text = "Location : " + "  " )
temp = Label(win, text = "Temperature : " + " " )
qotd = Label(win, text = "QOTD : " + "  ")
loc.place(x = 5, y = 350)
temp.place(x = 150, y = 350)
qotd.place(x = 5, y = 380)

#border?????????????


#--------------------------------------------------------------------add student-------------------------------------------------------------------------------------
#add student window
adst = Toplevel(win)
adst.title("Add student")
adst.geometry("250x350")
adst.withdraw() #so that sari windows ek sath na appear ho

rno_l = Label(adst, text = "Enter rno: ", font = ('arial',10, 'bold'))
rno_ae = Entry(adst, width = 15)
name_l = Label(adst, text = "Enter Name: ", font = ('arial',10, 'bold'))
name_ae = Entry(adst, width = 15)
marks_l = Label(adst, text = "Enter Marks: ", font = ('arial',10, 'bold'))
marks_ae = Entry(adst, width = 15)
save = Button(adst, text = "SAVE",font = ("arial", 10, "bold"), background = "light grey", command = asave)
back = Button(adst, text = "BACK",font = ("arial", 10, "bold"), background = "light grey", command = aback)
rno_l.pack(pady = 10)
rno_ae.pack(pady = 10)
name_l.pack(pady = 10)
name_ae.pack(pady = 10)
marks_l.pack(pady = 10)
marks_ae.pack(pady = 10)
save.pack(pady = 11)
back.pack(pady = 11)
#---------------------------------------------------------------update student------------------------------------------------------------------------------------
#update student window
upst = Toplevel(win)
upst.title("update Students")
upst.geometry("250x350")
upst.withdraw()

rno_l = Label(upst, text = "Enter rno: ", font = ('arial',10, 'bold'))
rno_e = Entry(upst, width = 15)
name_l = Label(upst, text = "Enter Name: ", font = ('arial',10, 'bold'))
name_e = Entry(upst, width = 15)
marks_l = Label(upst, text = "Enter Marks: ", font = ('arial',10, 'bold'))
marks_e = Entry(upst, width = 15)
save = Button(upst, text = "SAVE",font = ("arial", 10, "bold"), background = "light grey", command = usave)
back = Button(upst, text = "BACK",font = ("arial", 10, "bold"), background = "light grey", command = uback)
rno_l.pack(pady = 11)
rno_e.pack(pady = 11)
name_l.pack(pady = 11)
name_e.pack(pady = 11)
marks_l.pack(pady = 11)
marks_e.pack(pady = 11)
save.pack(pady = 11)
back.pack(pady = 11)

#---------------------------------------------------------view student-----------------------------------------------------------------------------------------
#view student window
vist = Toplevel(win)
vist.title("View Students")
vist.geometry("250x350")
vist.withdraw() #so that sari windows ek sath na appear ho

back = Button(vist, text = "BACK", width = 10, background = "light grey", command= vback)
sc = Scrollbar(vist, width = 20)
back.pack(side = "bottom")
sc.pack(side = 'right', fill = 'y')
list = Listbox(vist, width = 35, height = 25)
list.pack(side = 'left')


#-----------------------------------------------------------------delete student--------------------------------------------------------------------------------------
#delete student window
dest = Toplevel(win)
dest.title(" Remove Students")
dest.geometry("250x350")
dest.withdraw()

rno_l = Label(dest, text = "Enter rno: ", font = ('arial',10, 'bold'))
rno_e = Entry(dest, width = 15)
save = Button(dest, text = "DELETE",width = 10, font = ("arial", 10, "bold"), background = "light grey", command = dsave)
back = Button(dest, text = "BACK", width = 10, font = ("arial", 10, "bold"), background = "light grey", command = dback)
rno_l.pack(pady = 11)
rno_e.pack(pady = 11)
save.pack(pady = 11)
back.pack(pady = 11)





win.mainloop()