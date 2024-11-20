#ATTEMPT 2 TO CONVERT TERMINAL LOGIC TO GUI
import pandas as pd
import string
from tkinter import *
root=Tk()
ROLL_LIST=r'C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Roll list.csv'
ID_PASS=r'C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\id_password.csv'
#====================================================================================================
file=pd.read_csv(ROLL_LIST)
df = pd.DataFrame(file)
#====================================================================================================
admin_id_pass=pd.read_csv(ID_PASS)
df1 = pd.DataFrame(admin_id_pass)
id_pass=df1.loc[0].tolist()
#====================================================================================================
info1=['Roll No          :','Enrollment No    :','Name of Student  :','Student Mo       :','Parents Mo       :','E-mail           :']
info=['Roll No.','Enrollment No.','Name of Student','Student Mo.','Parents Mo.','E-mail']
#====================================================================================================
#====================================================================================================
def student_login():
  def sedit(i):
    if i!=-1:
      student_edit(i)
    else:
      for widget in root.winfo_children():
        widget.destroy()
      main()
  def check():
    global i
    i=-1
    id_search=df[info[5]]
    for index in range (len(id_search)):
      if id.get()==id_search[index]:
        break
      elif index>len(id_search):
        print("INVALLID ID PASSWORD")
        index=0
      else:
        continue
    password_search=df.loc[index].tolist()
    if password.get()==password_search[1]:
      print_info(index,0)
      i=index
      Button(text="EDIT",command=lambda:sedit(i),font="Georgia 12").grid(row=6,column=4)
      Button(text="EXIT",command=lambda:sedit(-1),font="Georgia 12").grid(row=6,column=5)
  Label(text="",font="Georgia 12").grid(row=4,column=1)
  Label(text="STUDENT ID::",font="Georgia 12").grid(row=5, column=0)
  Label(text="PASSWORD::",font="Georgia 12").grid(row=6,column=0)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 12")
  passentry=Entry(root,textvariable=password,show="*",font="Georgia 12")
  identry.grid(row=5,column=1)
  passentry.grid(row=6,column=1)
  Button(text="SUBMIT",command=check,font="Georgia 12").grid(row=7,column=1)
#====================================================================================================
def student_edit(j):
  def submit(j):
    change=[roll_no.get(),en_no.get(),name.get(),student_number.get(),parent_number.get(),email.get()]
    for h in range(6):
      if change[h]=='':
        change[h]=df.loc[j,info[h]]      
    df.loc[j]=change
    df.to_csv(ROLL_LIST,index=False)
    print_info(j,8)
  roll_no=StringVar()
  roll_entry=Entry(root,textvariable=roll_no,font="Georgia 12")
  roll_entry.grid(row=0,column=6)
  en_no=StringVar()
  en_entry=Entry(root,textvariable=en_no,font="Georgia 12")
  en_entry.grid(row=1,column=6)
  name=StringVar()
  name_entry=Entry(root,textvariable=name,font="Georgia 12")
  name_entry.grid(row=2,column=6)  
  student_number=StringVar()
  student_number_entry=Entry(root,textvariable=student_number,font="Georgia 12")
  student_number_entry.grid(row=3,column=6)  
  parent_number=StringVar()
  parent_number_entry=Entry(root,textvariable=parent_number,font="Georgia 12")
  parent_number_entry.grid(row=4,column=6)  
  email=StringVar()
  email_entry=Entry(root,textvariable=email,font="Georgia 12")
  email_entry.grid(row=5,column=6)
  Button(root,text="EDIT INFO",command=lambda:submit(j),font="Georgia 12").grid(row=6,column=6)
#====================================================================================================
def print_info(i,n):
  a=df.loc[i].tolist()
  for j in range (6):
    Label(text=info1[j],font="Georgia 12").grid(row=j+n,column=4)
    Label(text=a[j],font="Georgia 12").grid(row=j+n,column=5)
  return i
#====================================================================================================
def admin():
  def sedit(h):
    if h==1:
      edit()
    else:
      return
  def check():
    if id.get()==id_pass[0] and password.get()==id_pass[1]:
      #Button(text="FIND",command=lambda:sedit(1),font="Georgia 12").grid(row=8,column=0)
      #Button(text="EXIT",command=lambda:sedit(0),font="Georgia 12").grid(row=8,column=1)
      edit()
  Label(text="",font="Georgia 12").grid(row=4,column=1)
  Label(text="USER ID::",font="Georgia 12").grid(row=5, column=0)
  Label(text="PASSWORD::",font="Georgia 12").grid(row=6,column=0)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 12")
  passentry=Entry(root,textvariable=password,show="*",font="Georgia 12")
  identry.grid(row=5,column=1)
  passentry.grid(row=6,column=1)
  Button(text="SUBMIT",command=check,font="Georgia 12").grid(row=7,column=1)
#====================================================================================================
def edit():
  def searching(option,h): 
    Label(text=f"{h}",font="Georgia 12").grid(row=7,column=0)
    search1=StringVar()
    searchentry=Entry(root,textvariable=search1,font="Georgia 12")
    searchentry.grid(row=7,column=1)
    Button(root,text="SEARCH",command=lambda:modify(option),font="Georgia 12").grid(row=7,column=2)
    def modify(option):           
      search=df[info[option]]
      global i
      i=-1
      for index in range (len(search)):
        if search1.get() in search[index]:
          i=index
          print_info(i,8)
          break
      if i!=-1:
        Button(root,text="EDIT",command=lambda:admin_change(i),font="Georgia 12").grid(row=8,column=2)
      else:
        print("not found")
  def check_a():
    if box1.get()==1:
      option=0
      h="ROLL NO"
    elif box2.get()==1:
      option=1
      h="ENROLMENT NO"
    elif box3.get()==1:
      option=2
      h="NAME"
    elif box4.get()==1:
      option=3
      h="STUDENT NUMBER"
    elif box5.get()==1:
      option=4
      h="PARENTS NUMBER"
    elif box6.get()==1:
      option=5
      h="EMAIL-ID"
    searching(option,h)
  #Label(text="CHANGE OPTION APPEAR HERE").grid(row=8,column=0)
  for i in range (6):
    Label(text=f"SEARCH BY {info1[i]}",font="Georgia 12").grid(row=i,column=4)
  box1=IntVar()
  Checkbutton(root,variable=box1,font="Georgia 12").grid(row=0,column=5)
  box2=IntVar()
  Checkbutton(root,variable=box2,font="Georgia 12").grid(row=1,column=5)
  box3=IntVar()
  Checkbutton(root,variable=box3,font="Georgia 12").grid(row=2,column=5)
  box4=IntVar()
  Checkbutton(root,variable=box4,font="Georgia 12").grid(row=3,column=5)
  box5=IntVar()
  Checkbutton(root,variable=box5,font="Georgia 12").grid(row=4,column=5)
  box6=IntVar()
  Checkbutton(root,variable=box6,font="Georgia 12").grid(row=5,column=5)
  Button(text="FIND",command=check_a,font="Georgia 12").grid(row=6,column=5)
  def admin_change(i):
    box12=IntVar()
    Checkbutton(root,variable=box12,font="Georgia 12").grid(row=8,column=7)
    box22=IntVar()
    Checkbutton(root,variable=box22,font="Georgia 12").grid(row=9,column=7)
    box32=IntVar()
    Checkbutton(root,variable=box32,font="Georgia 12").grid(row=10,column=7)
    box42=IntVar()
    Checkbutton(root,variable=box42,font="Georgia 12").grid(row=11,column=7)
    box52=IntVar()
    Checkbutton(root,variable=box52,font="Georgia 12").grid(row=12,column=7)
    box62=IntVar()
    Checkbutton(root,variable=box62,font="Georgia 12").grid(row=13,column=7)
    Button(root,text="EDIT INFO",command=lambda:change(i),font="Georgia 12").grid(row=14,column=7)
    def change(i):
      if box12.get()==1:
        option=1
        h="ROLL NO"
      elif box22.get()==1:
        option=2
        h="ENROLMENT NO"
      elif box32.get()==1:
        option=3
        h="NAME"
      elif box42.get()==1:
        option=4
        h="STUDENT NUMBER"
      elif box52.get()==1:
        option=5
        h="PARENTS NUMBER"
      elif box62.get()==1:
        option=6
        h="EMAIL-ID"
      change1(option,i,h)
    def change1(option,i,h):
      Label(text=h,font="Georgia 12").grid(row=9,column=0)
      studentchange=StringVar()
      studentchangeentry=Entry(root,textvariable=studentchange,font="Georgia 12")
      studentchangeentry.grid(row=9,column=1)
      Button(root,text="SUBMIT CHANGE",command=lambda:change2(option,i),font="Georgia 12").grid(row=9,column=2)
      def change2(option,i):
        df.loc[i,info[option-1]]=studentchange.get()
        df.to_csv(ROLL_LIST,index=False)
#====================================================================================================
def main():
  root.geometry("1325x505")
  root.title("WELCOME")
  def option():
    if box1.get()==1:
      admin()
    if box2.get()==1:
      student_login()
    if box1.get()==1:
      return
  Label(text="ADMIN  LOGIN / EDIT THE INFORMATION(ADMIN)",font="Georgia 12").grid(row=0,column=0)
  Label(text="STUDENT LOGIN / EDIT THE INFORMATIOM(STUDENT)",font="Georgia 12").grid(row=1,column=0)
  Label(text="EXIT",font="Georgia 12").grid(row=2,column=0)
  box1=IntVar()
  Checkbutton(variable=box1,font="Georgia 12").grid(row=0,column=1)
  box2=IntVar()
  Checkbutton(variable=box2,font="Georgia 12").grid(row=1,column=1)
  box3=IntVar()
  Checkbutton(variable=box3,font="Georgia 12").grid(row=2,column=1)
  Button(text="SUBMIT",command=option,font="Georgia 12").grid(row=3,column=1)
if __name__ == "__main__":
    main()
root.mainloop()
#3,1