from tkinter import *
from tkinter import messagebox
import pandas as pd
import os.path
from os import path

root = Tk()
root.title("PII Form")
root.geometry("500x350")


def restartFunc():
	resetFunc()

def copyURL():
	urlEntry.delete(0, 'end')
	urlEntry.insert(0, menuOptions[r.get()-1])

def clipit(parent,textwidget):
    parent.clipboard_clear()
    parent.event_generate("<<TextModified>>")
    parent.clipboard_append(textwidget.get())
    parent.update()

def frame3():
	frame2 = Frame(root)
	frames.append(frame2)
	frame2.pack()
	global menuOptions
	menuOptions = url.split(',')

	mb = Menubutton(frame2, text="Select URL Type", relief=RAISED)
	mb.grid(row=0, column=0)
	mb.menu = Menu(mb, tearoff=0)
	mb["menu"] = mb.menu

	global r
	r = IntVar()
	for i in range(0, len(menuOptions)):	
		mb.menu.add_radiobutton( label="url"+str(i+1), variable=r, value=(i+1))
	mb.grid(row=0, column=0, pady=15)

	global urlEntry
	urlEntry = Entry(frame2, width=30)
	urlEntry.grid(row=3,column=0)

	copyText = Button(frame2, text="Copy URL", command=lambda: clipit(frame2, urlEntry))
	copyText.grid(row=3, column=1)

	copyBtn = Button(frame2, text="Copy URL to TextBox", command=copyURL)
	copyBtn.grid(row=4, column=0)

	restartBtn = Button(frame2, text="Restart", command=restartFunc)
	restartBtn.grid(row=3, column=2, padx=5)


def emptyNamePopupError():
	messagebox.showerror("Notification", "Name cannot be empty")

def submitFunction():

	if(len(nameEntry.get())==0):
		emptyNamePopupError()

	else:
		name[len(name)-1]=nameEntry.get()
		if(cityVar.get()==1):
			city[len(city)-1]=cityEntry.get()
		if(workplaceVar.get()==1):
			workplace[len(workplace)-1]=workplaceEntry.get()
		if(instituteVar.get()==1):
			institute[len(institute)-1]=instituteEntry.get()
		resetFunc(True)

def frame2():
	frame1 = Frame(root)
	frames.append(frame1)
	frame1.pack(pady=10)
	row=0;
	col=0;

	global nameEntry
	global cityEntry
	global workplaceEntry
	global instituteEntry

	if nameVar.get()==1:
		nameLabel = Label(frame1, text="Name", pady=5).grid(row=row, column=col)
		col+=1
		nameEntry = Entry(frame1)
		nameEntry.grid(row=row, column=col)
		col=0
		row+=1
	if cityVar.get()==1:
		cityLabel = Label(frame1, text="City", pady=5).grid(row=row, column=col)
		col+=1
		cityEntry = Entry(frame1)
		cityEntry.grid(row=row, column=col)
		col=0
		row+=1
	if workplaceVar.get()==1:
		workplaceLabel = Label(frame1, text="Workplace", pady=5).grid(row=row, column=col)
		col+=1
		workplaceEntry = Entry(frame1)
		workplaceEntry.grid(row=row, column=col)
		col=0
		row+=1
	if instituteVar.get()==1:
		instituteLabel = Label(frame1, text="Institute", pady=5).grid(row=row, column=col)
		col+=1
		instituteEntry = Entry(frame1)
		instituteEntry.grid(row=row, column=col)
		col=0
		row+=1
	
	col+=1
	submitButton = Button(frame1, text="Submit And Generate Url", command=submitFunction)
	submitButton.grid(row=row, column=col)


def resetFunc(checkPress=False):
	if len(frames)==2:
		if(checkPress):
			generateURL()
			saveData()
			frame3()
			checkPress=False
		else:
			frames[1].destroy()
			frames.pop(1)
			submitBtn["state"]=NORMAL

	elif len(frames)==1:
		nameCheckBox.select()
		cityCheckBox.deselect()
		instituteCheckBox.deselect()
		workplaceCheckBox.deselect()

	elif len(frames)==3:
		frames[2].destroy()
		frames.pop(2)
		frames[1].destroy()
		frames.pop(1)
		nameCheckBox.select()
		cityCheckBox.deselect()
		instituteCheckBox.deselect()
		workplaceCheckBox.deselect()
		submitBtn["state"]=NORMAL

def popup():
	messagebox.showerror("Notification", "Mandatory to select Name Field")

def submitFunc():
	if(nameVar.get()==0):
		popup()
	else:
		submitBtn["state"]=DISABLED
		frame2()

def exitFunc():
	root.destroy()

def frame1():
	frame = Frame(root)
	frames.append(frame)
	frame.pack()

	global nameCheckBox
	global cityCheckBox
	global instituteCheckBox
	global workplaceCheckBox

	global nameVar
	global cityVar
	global instituteVar
	global workplaceVar
	

	nameVar=IntVar()
	cityVar=IntVar()
	instituteVar=IntVar()
	workplaceVar=IntVar()
	
	nameCheckBox=Checkbutton(frame, text="Name", variable=nameVar, pady=10)
	nameCheckBox.grid(row=0, column=0)
	nameCheckBox.select()

	cityCheckBox=Checkbutton(frame, text="City", variable=cityVar)
	cityCheckBox.grid(row=0, column=1)

	workplaceCheckBox=Checkbutton(frame, text="Workplace", variable=workplaceVar, pady=10)
	workplaceCheckBox.grid(row=0, column=3)

	instituteCheckBox=Checkbutton(frame, text="Institute", variable=instituteVar)
	instituteCheckBox.grid(row=0, column=2)

	global submitBtn
	submitBtn = Button(frame, text="Submit", command=submitFunc)
	submitBtn.grid(row=1, column=1)

	resetBtn = Button(frame, text="Reset", command=resetFunc)
	resetBtn.grid(row=1, column=0)

	exitBtn = Button(frame, text="   Exit   ", command=exitFunc)
	exitBtn.grid(row=1, column=2)


def createCSV():
	df=pd.DataFrame()
	df["Name"]=[]
	# df["Age"]=[]
	df["City"]=[]
	df["Workplace"]=[]
	df["Institute"]=[]
	df["URL"]=[]

	df.to_csv("PII.csv")


def readCSV():
	global df
	global name
	# global lastName
	# global age
	global city
	global workplace
	global institute
	global URL

	df=pd.read_csv("PII.csv")
	name=df["Name"].tolist()
	city=df["City"].tolist()
	workplace=df["Workplace"].tolist()
	institute=df["Institute"].tolist()
	URL=df["URL"].tolist()
	name.append("")
	city.append("")
	workplace.append("")
	institute.append("")


def saveData():
	df=pd.DataFrame()
	df["Name"]=name
	df["City"]=city
	df["Workplace"]=workplace
	df["Institute"]=institute
	df["URL"]=URL
	df.to_csv("PII.csv")
	readCSV()


def addFilters(url, urlList, csvName, col1, col2, field):
	dfFilters = pd.DataFrame()
	dfFilters = pd.read_csv(csvName)
	list1 = dfFilters[col1].tolist()
	list2 = dfFilters[col2].tolist()
	for i,j in zip(list1, list2):
		if i.lower()==field[len(field)-1].lower():
			urlList.append(url+j)

def generateURL():
	global url
	url="https://www.facebook.com/search/people?q="
	space="%20"
	filters="&filters="
	nameList=nameEntry.get().lower().split(" ")
	for i in nameList:
		url += i + space
	url = url[0:len(url)-len(space)]
	
	urlList=[]
	if instituteVar.get()==1:
		addFilters(url+filters, urlList, "Education.csv", "Education", "Key", institute)
	if workplaceVar.get()==1:
		addFilters(url+filters, urlList, "Work.csv", "Work", "Key", workplace)
	if cityVar.get()==1:
		addFilters(url+filters, urlList, "city.csv", "City", "Code", city)
		
	urlList.append(url)
	url = ""

	for i in urlList:
		url = url+i+","
	url = url[0:len(url)-1]
	URL.append(url)


if path.exists('PII.csv')==False:
	createCSV()
readCSV()
frames=[]

frame1()
root.mainloop()
