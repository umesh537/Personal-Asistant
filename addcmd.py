from tkinter import *
import mysql.connector
def cmd():
	global root3
	root3 = Tk()
	root3.title("Account register for VOIX")
	root3.geometry("450x300")
	root3.config(bg="white")
	global command_reg
	global ans_reg
	Label(root3, text='Please Add your custom commands', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
	bg="purple",width=300).pack()
	command_reg = StringVar()
	ans_reg = StringVar()
	Label(root3, text="").pack()
	Label(root3, text="Command :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=command_reg).pack()
	Label(root3, text="").pack()
	Label(root3, text="Action :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=ans_reg).pack()
	Label(root3, text="").pack()
	Button(root3, text="ADD", bg="purple", fg='white', relief="groove", font=('arial', 12, 'bold'),command=cmd_verification).pack()
	Label(root3, text="") 
  
def cmd_verification():
	cmd_verification = command_reg.get()
	ans_verification = ans_reg.get()
	import mysql.connector

	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="umesh123",
	database="logindb"
	)

	mycursor = mydb.cursor()

	sql = "INSERT INTO commands(command, ans) VALUES (%s, %s)"
	val = (cmd_verification, ans_verification)

	mycursor.execute(sql, val)

	mydb.commit()

	print(mycursor.rowcount, "record inserted.") 
cmd()
root3.mainloop()    