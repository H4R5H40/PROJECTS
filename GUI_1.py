#ATTEMPT 1 TO CONVERT TERMINAL LOGIC TO GUI
import pandas as pd
import string
from tkinter import *
root=Tk()
#====================================================================================================
ROLL_LIST=r'C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Roll list.csv'
file=pd.read_csv(ROLL_LIST)
df = pd.DataFrame(file)
#====================================================================================================
ID_PASS=r'C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\id_password.csv'
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
    if i==-1:
      return
    student_edit(i)
  def check():
    id_search=df[info[5]]
    for i in range (len(id_search)):
      if id.get()==id_search[i]:
        break
      elif i>len(id_search):
        print("INVALLID ID PASSWORD")
        i=0
      else:
        continue
    password_search=df.loc[i].tolist()
    if password.get()==password_search[1]:
      i=print_info(i,0)
      Button(text="EDIT",command=lambda:sedit(i)).grid(row=7,column=0)
      Button(text="EXIT",command=lambda:sedit(-1)).grid(row=7,column=1)
  Label(text="STUDENT ID::").grid(row=4, column=0)
  Label(text="PASSWORD::").grid(row=5,column=0)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id)
  passentry=Entry(root,textvariable=password,show="*")
  identry.grid(row=4,column=1)
  passentry.grid(row=5,column=1)
  Button(text="SUBMIT",command=check).grid(row=6,column=1)
#====================================================================================================
def student_edit(j):
  def submit(option,change):
    df.loc[j,info[option-1]]=change
    df.to_csv(ROLL_LIST,index=False)
    #Label(text="                  ").grid(row=7,column=2)
    Label(text="EDITED INFORMATION").grid(row=7,column=3)
    print_info(j,8)
  def check_a():
    option=0
    if box1.get()==1:
      option=1
    elif box2.get()==1:
      option=2
    elif box3.get()==1:
      option=3
    elif box4.get()==1:
      option=4
    elif box5.get()==1:
      option=5
    elif box6.get()==1:
      option=6
    if (df.loc[j,info[option-1]]!='N.A.' or option==3 or option==4 or option==6):
      Label(text=df.loc[j,info[option-1]]).grid(row=9,column=0)
      change=StringVar()
      newentry=Entry(root,textvariable=change)
      newentry.grid(row=9,column=1)
      Button(root,text="submit",command=lambda:submit(option,change.get())).grid(row=9,column=2)
  Label(text="CHANGE OPTION APPEAR HERE").grid(row=8,column=0)
  box1=IntVar()
  Checkbutton(root,variable=box1).grid(row=0,column=6)
  box2=IntVar()
  Checkbutton(root,variable=box2).grid(row=1,column=6)
  box3=IntVar()
  Checkbutton(root,variable=box3).grid(row=2,column=6)
  box4=IntVar()
  Checkbutton(root,variable=box4).grid(row=3,column=6)
  box5=IntVar()
  Checkbutton(root,variable=box5).grid(row=4,column=6)
  box6=IntVar()
  Checkbutton(root,variable=box6).grid(row=5,column=6)
  Button(text="check",command=check_a).grid(row=6,column=6)
#====================================================================================================
def print_info(i,n):
  a=df.loc[i].tolist()
  for j in range (6):
    Label(text=info1[j]).grid(row=j+n,column=4)
    Label(text=a[j]).grid(row=j+n,column=5)
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
      #Button(text="FIND",command=lambda:sedit(1)).grid(row=7,column=0)
      #Button(text="EXIT",command=lambda:sedit(0)).grid(row=7,column=1)
      edit()
  Label(text="").grid(row=4,column=0)
  Label(text="USER ID::",font="Georgia 12").grid(row=5, column=0)
  Label(text="PASSWORD::",font="Georgia 12").grid(row=6,column=0)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 12")
  passentry=Entry(root,textvariable=password,show="*",font="Georgia 12 bold")
  identry.grid(row=5,column=1)
  passentry.grid(row=6,column=1)
  Button(text="SUBMIT",command=check,font="Georgia 12").grid(row=7,column=1)
#====================================================================================================
def edit():
  def searching(option,h):    
    search=df[info[option]]
    Label(text=f"{h}").grid(row=7,column=0)
    search1=StringVar()
    searchentry=Entry(root,textvariable=search1)
    searchentry.grid(row=7,column=1)
    Button(root,text="SEARCH",command=lambda:modify(search)).grid(row=7,column=2)
    def modify(search):
        global i
        i=-1
        for index in range (len(search)):
          if search1.get().lower() in search[index].lower():
            i=index
            print_info(i,8)
            break
        if i!=-1:
          Button(root,text="EDIT",command=lambda:admin_change(i)).grid(row=8,column=2)
        else:
          print("not found")
  def check_a():
    option=0
    if box1.get()==1:
      option=1
      h="ROLL NO"
    elif box2.get()==1:
      option=0
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
    Label(text=f"SEARCH BY {info1[i]}").grid(row=i,column=4)
  box1=IntVar()
  Checkbutton(root,variable=box1).grid(row=0,column=5)
  box2=IntVar()
  Checkbutton(root,variable=box2).grid(row=1,column=5)
  box3=IntVar()
  Checkbutton(root,variable=box3).grid(row=2,column=5)
  box4=IntVar()
  Checkbutton(root,variable=box4).grid(row=3,column=5)
  box5=IntVar()
  Checkbutton(root,variable=box5).grid(row=4,column=5)
  box6=IntVar()
  Checkbutton(root,variable=box6).grid(row=5,column=5)
  Button(text="check",command=check_a).grid(row=6,column=5)
  def admin_change(i):
    box12=IntVar()
    Checkbutton(root,variable=box12).grid(row=8,column=7)
    box22=IntVar()
    Checkbutton(root,variable=box22).grid(row=9,column=7)
    box32=IntVar()
    Checkbutton(root,variable=box32).grid(row=10,column=7)
    box42=IntVar()
    Checkbutton(root,variable=box42).grid(row=11,column=7)
    box52=IntVar()
    Checkbutton(root,variable=box52).grid(row=12,column=7)
    box62=IntVar()
    Checkbutton(root,variable=box62).grid(row=13,column=7)
    Button(root,text="EDIT INFO",command=lambda:change(i)).grid(row=14,column=7)
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
      Label(text=h).grid(row=9,column=0)
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

