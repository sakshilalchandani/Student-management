'''try:
		rno = arno_e.get()
		name= aname_e.get()
		marks = amarks_e.get()
		con = sq.connect("student.db")
		cur = con.cursor()
		cur.execute("SELECT * FROM student")
		res= cur.fetchall()
		print(res)
		flag = False
		for r in res:
			if r[0] == int(rno):
				showerror("error", "rno exists")
				flag = True
				arno_e.delete(0,END)
				aname_e.delete(0,END)
				amarks_e.delete(0,END)
				break		
		if flag == False:
			print(rno)
			print(marks)
			#if rno.isdigit() == False:
				#raise Exception("invalid roll no")
			#	showerror("error", "invalid rno, try again")
			#	arno_e.delete(0, END)
			if int(rno) < 1:
				showerror("Invalid roll number", "please check the rno! ")
			elif rno.isalpha() == True:
				showerror("errrrrrr", "only integer")
			elif len(name)<2 or len(name) == 0 or name.isalpha() == False:
				#raise Exception("invalid name")
				#-----------------------------raise exception karne k baad program breaks---------------------------------------------------			
				showerror("Invalid name", "please check the name! ")
				aname_e.delete(0, END)

			elif int(marks)<0 or int(marks) >100:
				#raise Exception("invalid marks, try again")
				showerror("error", "invalid marks")
				amarks_e.delete(0, END)

			elif marks.isalpha() == True:
				#raise Exception("enter value kar bhai")
				showerror("invalid", "marks is integer only")
	
			else:
				con = sq.connect("student.db")
				cur = con.cursor()
				with con:
					cur.execute("INSERT INTO student VALUES(?,?,?)", (rno, name, marks))
				print("saved")
				showinfo("success", "record added")
			aname_e.delete(0, END)
			arno_e.delete(0, END)
			amarks_e.delete(0, END)	
	except Exception as e:
		print("save issue--->",e)
		showerror("Invalid Input !", "Please Check Your Inputs again! ")


#	finally:
#		print(rno, name,marks)'''
