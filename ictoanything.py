import mysql.connector
import tkinter.messagebox as mbox

line="---"*10

try:
	mydb=mysql.connector.connect(host="localhost",
		user="root", 
		password="")
except:
	print("Not connect to localhost")
	print(line+"\n")

def CreateDatabase():
	try:
		q3db=mydb.cursor()
		create="CREATE DATABASE IF NOT EXISTS ictoanything"
		q3db.execute(create)
		try:
			mydb.database="ictoanything"
			try:
				tbl="CREATE TABLE IF NOT EXISTS user"\
				"(Name VARCHAR(2000), "\
				"Ic VARCHAR(12) PRIMARY KEY, "\
				"MatricNum VARCHAR(12), DOB VARCHAR(10), "\
				"Umur VARCHAR(10), jantina VARCHAR(6),"\
				"Negeri VARCHAR(100))"
				q3db.execute(tbl)
			except mysql.connector.Error as ctb:
				print("Fail Creating Table : {}".format(ctb))
		except mysql.connector.Error as dnf:
			print("Database Not Found : {}".format(dnf))
	except mysql.connector.Error as x:
		print("Fail Creating database : {}".format(ror))

def InsertDatabase():
	try:
		mydb.database="ictoanything"

		mydbse = mydb.cursor()
		mydbse.execute("SELECT * FROM user WHERE Ic=%s",
			(ic,))
		sameinpt=mydbse.fetchone()

		if sameinpt:
			mbox.showinfo("Same Ic","Your Ic already In Classmate List")
		else:
			mydbse.execute("INSERT INTO user"
				"(Name,Ic,MatricNum,DOB,Umur,jantina,Negeri)"
				"VALUES(%s,%s,%s,%s,%s,%s,%s)",
				(name,ic,nomatric,DOB,umur,jantina,negeri))
			mydb.commit()
		
	except mysql.connector.Error as err:
		print("Failed Insert data : {}".format(err)+"\n")

def bfday(ic):
	tahun=int(ic[0:2])
	if tahun>=0 and tahun<=24:
		tahun+=2000
	else:		
		tahun+=1900
	bulan=int(ic[2:4])
	hari=int(ic[4:6])
	DOB=str(hari)+"/"+str(bulan)+"/"+str(tahun)
	return tahun,DOB

def Jantina(ic):
	jntina=int(ic)
	jntina%=2	
	if jntina == 0:	
		jantina="Female"	
	else:	
		jantina="Male"

	return jantina

def NegeriAsal(ic):
	negeriasal=int(ic[6:8])
	if negeriasal==1 or negeriasal==21 or negeriasal==22 or negeriasal==23 or negeriasal==24:
		negeri="Johor"
	elif negeriasal==2 or negeriasal==25 or negeriasal==26 or negeriasal==27:
		negeri="Kedah"
	elif negeriasal==3 or negeriasal==28 or negeriasal==29:
		negeri="Kelantan"
	elif negeriasal==4 or negeriasal==30 :
		negeri="Melaka"
	elif negeriasal==5 or negeriasal==31 or negeriasal==59:
		negeri="Negeri Sembilan"
	elif negeriasal==6 or negeriasal==32 or negeriasal==33:
		negeri="Pahang"
	elif negeriasal==7 or negeriasal==34 or negeriasal==35:
		negeri="Pulau Pinang"
	elif negeriasal==8 or negeriasal==36 or negeriasal==37 or negeriasal==38 or negeriasal==39:
		negeri="Perak"
	elif negeriasal==9 or negeriasal==40 :
		negeri="Perlis"
	elif negeriasal==10 or negeriasal==41 or negeriasal==42 or negeriasal==43 or negeriasal==44:
		negeri="Selangor"
	elif negeriasal==11 or negeriasal==45 or negeriasal==46:
		negeri="Terengganu"
	elif negeriasal==12 or negeriasal==47 or negeriasal==48 or negeriasal==49:
		negeri="Sabah"
	elif negeriasal==13 or negeriasal==50 or negeriasal==51 or negeriasal==52 or negeriasal==53:
		negeri="Sarawak"
	elif negeriasal==14 or negeriasal==54 or negeriasal==55 or negeriasal==56 or negeriasal==57:
		negeri="Kuala Lumpur"
	elif negeriasal==15 or negeriasal==58 :
		negeri="Labuan"
	elif negeriasal==16 :
		negeri="Putrajaya"
	else:
		negeri="Negeri Tidak Diketahui"

	return negeri

while True:
	name=input("Name : ")
	ic=input("Ic : ")
	tahun,DOB=bfday(ic)
	umur=2023-tahun
	jantina=Jantina(ic)
	negeri=NegeriAsal(ic)
	nomatric=input("No.Matric : ")

	try:
		CreateDatabase()
		InsertDatabase()
	except:
		print("\n"+line)
		print("Not Database connected to localhost")
		print(line+"\n")

	print(line)
	print(name)
	print(ic)
	print(nomatric)
	print(DOB)
	print(umur)
	print(jantina)
	print(negeri)
	print(line+"\n")