from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import pandas as pd
import requests
import numpy as np

try:
	wa = "https://ipinfo.io"
	res= requests.get(wa)
	data = res.json()
	city = data["city"]
except Exception as e:
	showerror("issue", e)

try:
	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + city
	
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	ta = a1 + a2 + a3 + a4
	res = requests.get(ta)
	data = res.json()
	tem = data["main"]["temp"]
except Exception as e:
	showerror("issue ", e)

def f1():
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0, END)
	con=None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + " rno : " + str(d[0]) + " name :" + str(d[1]) + " marks :" + str(d[2]) +"\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("issue", e)
	finally:
		if con is not None:
			con.close()

def f4():
	vw.withdraw()
	mw.deiconify()
	
def f5():
	mw.withdraw()
	uw.deiconify()

def f6():
	uw.withdraw()
	mw.deiconify()
def f7():
	mw.withdraw()
	dw.deiconify()

def f8():
	dw.withdraw()
	mw.deiconify()

def f9():
	con = None
	rno=0
	marks=None
	try:
		con = connect("sms.db")
		try:
			rno=int(aw_ent_rno.get())
			if rno <=0:
				showinfo("Error", "rno should br greater than zero")
				aw_ent_rno.delete(0, END)
				aw_ent_rno.focus()
				return
		
		except ValueError:
			showinfo("Error", "rno should be integer only")
			aw_ent_rno.delete(0, END)
			aw_ent_rno.focus()
			return


		name = aw_ent_name.get()
		if len(name)<2:
			showinfo("Error","name should contain atleast 2 character")
			aw_ent_name.delete(0,END)
			aw_ent_name.focus()
			return
		elif(name.isalpha()):
			pass
		else:
			showinfo("Error","Name should contain only alphabets")
			aw_ent_name.delete(0,END)
			aw_ent_name.focus()
			return
	
		try:
			
			marks=int(aw_ent_marks.get())
			if marks<0 or marks>100:
				showinfo("Error","marks should be between 0-100")
				aw_ent_marks.delete(0,END)
				aw_ent_marks.focus()
		except ValueError:
			showinfo("Error","marks should be integers only")
			aw_ent_marks.delete(0,END)
			aw_ent_marks.focus()
			con.rollback()
	
		if rno>0 and len(name)>=2 and name.isalpha() and marks is not None and (marks>=0 and marks<=100):
				cursor = con.cursor()
				sql = "insert into student values('%d', '%s', '%d')"
				cursor.execute(sql % (rno, name,marks))
				con.commit()
				showinfo("Success", "record added")
				aw_ent_rno.delete(0, END)
				aw_ent_name.delete(0, END)
				aw_ent_marks.delete(0, END)
				aw_ent_rno.focus()
	except DatabaseError as e:
		showerror("Error","rno no already exists")
		aw_ent_rno.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_marks.delete(0, END)
		aw_ent_rno.focus()
	finally:

		if con is not None:
			con.close()

def f10():
	con = None
	rno=0
	marks=None
	try:
		con = connect("sms.db")
		try:
			rno=int(uw_ent_rno.get())
			if rno <=0:
				showinfo("Error", "rno should br greater than zero")
				uw_ent_rno.delete(0, END)
				uw_ent_rno.focus()
				return
		
		except ValueError:
			showinfo("Error", "rno should be integer only")
			uw_ent_rno.delete(0, END)
			uw_ent_rno.focus()
			return


		name = uw_ent_name.get()
		if len(name)<2:
			showinfo("Error","name should contain atleast 2 character")
			uw_ent_name.delete(0,END)
			uw_ent_name.focus()
			return
		elif(name.isalpha()):
			pass
		else:
			showinfo("Error","Name should contain only alphabets")
			uw_ent_name.delete(0,END)
			uw_ent_name.focus()
			return
	
		try:
			
			marks=int(uw_ent_marks.get())
			if marks<=0 or marks>100:
				showinfo("Error","marks should be between 0-100")
				uw_ent_marks.delete(0,END)
				uw_ent_marks.focus()
		except ValueError:
			showinfo("Error","marks should be integers only")
			uw_ent_marks.delete(0,END)
			uw_ent_marks.focus()
			con.rollback()
	
		if rno>0 and len(name)>=2 and name.isalpha() and marks is not None and(marks>0 and marks<=100):
			con = connect("sms.db")
			sql = "update student set name ='%s', marks ='%d' where rno ='%d' "
			cursor = con.cursor()
			cursor.execute(sql % (name,marks, rno))
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success", "record updated")
				uw_ent_rno.delete(0, END)
				uw_ent_name.delete(0, END)
				uw_ent_marks.delete(0, END)
				uw_ent_rno.focus()
			else:
				showinfo("Failure", "rno not exists")
				uw_ent_rno.delete(0, END)
				uw_ent_name.delete(0, END)
				uw_ent_marks.delete(0, END)
				uw_ent_rno.focus()

	except DatabaseError as e:
		showerror("Error","rno not exists")
		uw_ent_rno.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_marks.delete(0, END)
		uw_ent_rno.focus()
	finally:
		if con is not None:
			con.close()

def f11():
	rno=0
	con = None
	try:
		con = connect("sms.db")
		try:
			rno=int(dw_ent_rno.get())
			if rno <=0:
				showinfo("Error", "rno should br greater than zero")
				dw_ent_rno.delete(0, END)
				dw_ent_rno.focus()
		
		except ValueError:
			showinfo("Error", "rno should be integer only")
			dw_ent_rno.delete(0, END)
			dw_ent_rno.focus()
			con.rollback()

		if rno>0:
			cursor = con.cursor()
			sql = "delete from student where rno ='%d' "
			cursor.execute(sql % (rno))
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success", "record deleted")
			else:
				showinfo("Failure", "rno not exists")
	except DatabaseError as e:
		showerror("Error","rno not exists")
	finally:
		dw_ent_rno.delete(0, END)
		dw_ent_rno.focus()
		if con is not None:
			con.close()

def f12():
	mw.withdraw()
	gw.deiconify()

	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql="select rno, name,marks from student order by marks desc"
		cursor.execute(sql)
		data=cursor.fetchall()
		name,marks=[],[]
		for d in data:
			name.append(str(d[1]))
			marks.append(int(d[2]))
		n=name[:5]
		p=marks[:5]
		p.sort(reverse=True)
		x=np.arange(len(marks))
		plt.bar(n,p,color="red", width=0.3, linewidth=5)
		plt.xlabel("names")
		plt.ylabel("marks")
		plt.title("Top 5 Students")
		plt.show()
	except Exception as e:
		showinfo("issue",e)
	finally:
		if con is not None:
			con.close()

def f13():
	gw.withdraw()
	mw.deiconify()
		
		





mw = Tk()
mw.title("S.M.S.")
mw.geometry("800x1000+50+50")

f=("Arial", 30, "bold")
y=20
x=10
mw_btn_add = Button(mw, text="Add student", font=f, width=15, command=f1)
mw_btn_view = Button(mw, text="View student", font=f, width=15, command =f3)
mw_btn_update = Button(mw, text="Update student", font=f, width=15, command=f5)
mw_btn_delete = Button(mw, text="Delete student", font=f, width=15, command=f7)
mw_btn_charts = Button(mw, text="Charts", font=f, width=15, command=f12)

mw_lab_location=Label(mw, text="Location : "+ city, font=f)
mw_lab_temp=Label(mw, text="Temp : "+ str(tem) + "°C", font=f)

mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_update.pack(pady=y)
mw_btn_delete.pack(pady=y)
mw_btn_charts.pack(pady=y)
mw_lab_location.place(x=15, y=610)
mw_lab_temp.place(x=500, y=610)

aw = Toplevel(mw)
aw.title("Add student")
aw.geometry("700x1000+50+50")

aw_lab_rno = Label(aw, text="enter rno", font=f)
aw_ent_rno = Entry(aw, font=f)
aw_lab_name = Label(aw, text="enter name", font=f)
aw_ent_name = Entry(aw, font=f)
aw_lab_marks = Label(aw, text="enter marks", font=f)
aw_ent_marks = Entry(aw, font=f)
aw_btn_save= Button(aw, text="Save", font=f, command=f9)
aw_btn_back= Button(aw, text="Back", font=f, command=f2)

aw_lab_rno.pack(pady=y)
aw_ent_rno.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_lab_marks.pack(pady=y)
aw_ent_marks.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)
aw.withdraw()

vw = Toplevel(mw)
vw.title("View student")
vw.geometry("800x600+50+50")

vw_st_data = ScrolledText(vw, width=35, height=8, font=f)
vw_btn_back= Button(vw, text="Back", font=f, command = f4)
vw_st_data.pack(pady=y)
vw_btn_back.pack(pady=y)
vw.withdraw()

uw = Toplevel(mw)
uw.title("Update student")
uw.geometry("700x1000+50+50")

uw_lab_rno = Label(uw, text="enter rno", font=f)
uw_ent_rno = Entry(uw, font=f)
uw_lab_name = Label(uw, text="enter name", font=f)
uw_ent_name = Entry(uw, font=f)
uw_lab_marks = Label(uw, text="enter marks", font=f)
uw_ent_marks = Entry(uw, font=f)
uw_btn_save= Button(uw, text="Save", font=f, command=f10)
uw_btn_back= Button(uw, text="Back", font=f, command=f6)

uw_lab_rno.pack(pady=y)
uw_ent_rno.pack(pady=y)
uw_lab_name.pack(pady=y)
uw_ent_name.pack(pady=y)
uw_lab_marks.pack(pady=y)
uw_ent_marks.pack(pady=y)
uw_btn_save.pack(pady=y)
uw_btn_back.pack(pady=y)
uw.withdraw()

dw = Toplevel(mw)
dw.title("Delete student")
dw.geometry("700x1000+50+50")

dw_lab_rno = Label(dw, text="enter rno", font=f)
dw_ent_rno = Entry(dw, font=f)
dw_btn_save= Button(dw, text="Delete", font=f, command= f11)
dw_btn_back= Button(dw, text="Back", font=f, command=f8)
dw_lab_rno.pack(pady=y)
dw_ent_rno.pack(pady=y)
dw_btn_save.pack(pady=y)
dw_btn_back.pack(pady=y)
dw.withdraw()

gw = Toplevel(mw)
gw.title("Graph")
gw.geometry("700x1000+50+50")

gw_btn_back= Button(gw, text="Back", font=f, command=f13)
gw_btn_back.place(x=250, y=620)
gw.withdraw()

mw.mainloop()