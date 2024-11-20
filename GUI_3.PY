#ATTEMPT 3 TO CONVERT TERMINAL LOGIC TO GUI
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
      print_info(index,0,3)
      i=index
      Button(text="EDIT",command=lambda:sedit(i),font="Georgia 12").grid(row=6,column=4)
      Button(text="EXIT",command=lambda:sedit(-1),font="Georgia 12").grid(row=6,column=3)
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
    print_info(j,8,3)
  roll_no=StringVar()
  roll_entry=Entry(root,textvariable=roll_no,font="Georgia 12")
  roll_entry.grid(row=0,column=5)
  en_no=StringVar()
  en_entry=Entry(root,textvariable=en_no,font="Georgia 12")
  en_entry.grid(row=1,column=5)
  name=StringVar()
  name_entry=Entry(root,textvariable=name,font="Georgia 12")
  name_entry.grid(row=2,column=5)  
  student_number=StringVar()
  student_number_entry=Entry(root,textvariable=student_number,font="Georgia 12")
  student_number_entry.grid(row=3,column=5)  
  parent_number=StringVar()
  parent_number_entry=Entry(root,textvariable=parent_number,font="Georgia 12")
  parent_number_entry.grid(row=4,column=5)  
  email=StringVar()
  email_entry=Entry(root,textvariable=email,font="Georgia 12")
  email_entry.grid(row=5,column=5)
  Button(root,text="EDIT INFO",command=lambda:submit(j),font="Georgia 12").grid(row=6,column=5)
#====================================================================================================
def print_info(i,n,m):
  a=df.loc[i].tolist()
  for j in range (6):
    Label(text=info1[j],font="Georgia 12").grid(row=j+n,column=m)
    Label(text=a[j],font="Georgia 12").grid(row=j+n,column=m+1)
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
  def end():
    for widget in root.winfo_children():
        widget.destroy()
    main()
  def searching(option,h):            
      search=df[info[option]]
      global i
      i=-1
      for index in range (len(search)):
        if ((h.lower()) in (search[index].lower()) or h==search[index]) :
          i=index
          print_info(i,8,3)
          break
      if i!=-1:
        Button(root,text="EDIT",command=lambda:admin_change(i),font="Georgia 12").grid(row=15,column=4)
        Button(root,text="EXIT",command=end,font="Georgia 12").grid(row=15,column=3)
      else:
        print("not found")
  def check_a():
    if roll_no.get()!='':
      h=roll_no.get()
      searching(0,h)
    elif en_no.get()!='':
      h=en_no.get()
      searching(1,h)
    elif name.get()!='':
      h=name.get()
      searching(2,h)
    elif student_number.get()!='':
      h=student_number.get()
      searching(3,h)
    elif parent_number.get()!='':
      h=parent_number.get()
      searching(4,h)
    elif email.get()!='':
      h=email.get()
      searching(5,h)
  for i in range (6):
    Label(text=f"SEARCH BY {info1[i]}",font="Georgia 12").grid(row=i,column=4)
  roll_no=StringVar()
  roll_entry=Entry(root,textvariable=roll_no,font="Georgia 12")
  roll_entry.grid(row=0,column=5)
  en_no=StringVar()
  en_entry=Entry(root,textvariable=en_no,font="Georgia 12")
  en_entry.grid(row=1,column=5)
  name=StringVar()
  name_entry=Entry(root,textvariable=name,font="Georgia 12")
  name_entry.grid(row=2,column=5)  
  student_number=StringVar()
  student_number_entry=Entry(root,textvariable=student_number,font="Georgia 12")
  student_number_entry.grid(row=3,column=5)  
  parent_number=StringVar()
  parent_number_entry=Entry(root,textvariable=parent_number,font="Georgia 12")
  parent_number_entry.grid(row=4,column=5)  
  email=StringVar()
  email_entry=Entry(root,textvariable=email,font="Georgia 12")
  email_entry.grid(row=5,column=5)
  Button(root,text="SEARCH",command=check_a,font="Georgia 12").grid(row=7,column=5)
  def admin_change(i):
    roll_no1=StringVar()
    roll_entry=Entry(root,textvariable=roll_no1,font="Georgia 12")
    roll_entry.grid(row=8,column=5)
    en_no1=StringVar()
    en_entry=Entry(root,textvariable=en_no1,font="Georgia 12")
    en_entry.grid(row=9,column=5)
    name1=StringVar()
    name_entry=Entry(root,textvariable=name1,font="Georgia 12")
    name_entry.grid(row=10,column=5)  
    student_number1=StringVar()
    student_number_entry=Entry(root,textvariable=student_number1,font="Georgia 12")
    student_number_entry.grid(row=11,column=5)  
    parent_number1=StringVar()
    parent_number_entry=Entry(root,textvariable=parent_number1,font="Georgia 12")
    parent_number_entry.grid(row=12,column=5)  
    email1=StringVar()
    email_entry=Entry(root,textvariable=email1,font="Georgia 12")
    email_entry.grid(row=13,column=5)
    Button(root,text="APPLY",command=lambda:change1(i),font="Georgia 12").grid(row=15,column=5)
    def change1(i):
        change=[roll_no1.get(),en_no1.get(),name1.get(),student_number1.get(),parent_number1.get(),email1.get()]
        for h in range(6):
            if change[h]=='':
                change[h]=df.loc[i,info[h]]   
        df.loc[i]=change
        df.to_csv(ROLL_LIST,index=False)
        print_info(i,8,0)
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