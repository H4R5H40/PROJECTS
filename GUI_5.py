#ATTEMPT 5 TO CONVERT TERMINAL LOGIC TO GUI
import pandas as pd
import string
from tkinter import *
root=Tk()
STUDENT_ACCOUNT=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\STUDENT.png"
STUDENR_PROFILE=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\STUDENT PHOTO.png"
ADMIN_ACCOUNT=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\ADMIN.png"
ID_PASS=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\id_password.csv"
ROLL_LIST=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Roll list.csv"
BACKGROUND=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Screenshot 2024-10-29 142601.png"
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
def student_login():
  def sedit(i):
    if i!=-1:
      student_edit(i)
    else:
      for widget in root.winfo_children():
        widget.destroy()
      student_login()
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
      for widget in root.winfo_children():
        widget.destroy()
      print_info(index)
      i=index
      Button(text="EDIT",command=lambda:sedit(i),font="Georgia 12",background="white").grid(row=7,column=0)
      Button(text="BACK",command=lambda:sedit(-1),font="Georgia 12",background="white").grid(row=7,column=1)
  Label(root,image=photo).place(x=0,y=0)
  global p1
  p1=PhotoImage(file=STUDENT_ACCOUNT)
  Label(root,image=p1,background="white").place(x=270,y=75)
  Label(text="STUDENT ID::",font="Georgia 12",background="white").place(x=200, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=200,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",background="white").place(x=200, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",background="white").place(x=200, y=290)
  #҈֍•
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",background="white").place(x=260,y=330)
#====================================================================================================
def student_edit(j):
  def submit(j):
    change=[roll_no.get(),en_no.get(),name.get(),student_number.get(),parent_number.get(),email.get()]
    for h in range(6):
      if change[h]=='':
        change[h]=df.loc[j,info[h]]      
    df.loc[j]=change
    df.to_csv(ROLL_LIST,index=False)
    for widget in root.winfo_children():
      widget.destroy()
    print_info(j)
    Button(text="CLOSE",command=root.destroy,font="Georgia 12",background="white").grid(row=7,column=1)
  roll_no=StringVar()
  roll_entry=Entry(root,textvariable=roll_no,font="Georgia 12",background="white").grid(row=1,column=2)
  en_no=StringVar()
  en_entry=Entry(root,textvariable=en_no,font="Georgia 12",background="white").grid(row=2,column=2)
  name=StringVar()
  name_entry=Entry(root,textvariable=name,font="Georgia 12",background="white").grid(row=3,column=2)  
  student_number=StringVar()
  student_number_entry=Entry(root,textvariable=student_number,font="Georgia 12",background="white").grid(row=4,column=2)  
  parent_number=StringVar()
  parent_number_entry=Entry(root,textvariable=parent_number,font="Georgia 12",background="white").grid(row=5,column=2)  
  email=StringVar()
  email_entry=Entry(root,textvariable=email,font="Georgia 12",background="white").grid(row=6,column=2)
  Button(root,text="EDIT INFO",command=lambda:submit(j),font="Georgia 12",background="white").grid(row=7,column=2)
#====================================================================================================
def print_info(i):
  a=df.loc[i].tolist()
  Label(root,image=photo).place(x=0,y=0)
  global p3
  root.configure(background="white")
  p3=PhotoImage(file=STUDENR_PROFILE)
  Label(root,image=p3,background="white").grid(row=0,column=1)
  for j in range (6):
    Label(text=info1[j],font="Georgia 12",background="white").grid(row=j+1,column=0)
    Label(text=a[j],font="Georgia 12",background="white").grid(row=j+1,column=1)
  return i
#====================================================================================================
def admin():
  def check():
    if id.get()==id_pass[0] and password.get()==id_pass[1]:
      for widget in root.winfo_children():
        widget.destroy()
      edit()
  Label(root,image=photo).place(x=0,y=0)
  global p2
  p2=PhotoImage(file=ADMIN_ACCOUNT)
  Label(root,image=p2,background="white").place(x=270,y=75)
  Label(text="USER ID::",font="Georgia 12",background="white").place(x=205, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=205,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",background="white").place(x=205, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",background="white").place(x=205, y=290)
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",background="white").place(x=260,y=330)
#====================================================================================================
def edit():
  def searching(option,h):           
    def back():
      for widget in root.winfo_children():
        widget.destroy()
      edit() 
    search=df[info[option]]
    global i
    i=-1
    for index in range (len(search)):
      if ((h.lower()) in (search[index].lower()) or h==search[index]) :
        i=index
        print_info(i)
        break
    if i!=-1:
      Button(root,text="EDIT",command=lambda:admin_change(i),font="Georgia 12",background="white").grid(row=7,column=0)
      Button(root,text="EXIT",command=back,font="Georgia 12",background="white").grid(row=7,column=1)
    else:
      print("not found")
  def find():
    if roll_no.get()!='':
      h=roll_no.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(0,h)
    elif en_no.get()!='':
      h=en_no.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(1,h)
    elif name.get()!='':
      h=name.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(2,h)
    elif student_number.get()!='':
      h=student_number.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(3,h)
    elif parent_number.get()!='':
      h=parent_number.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(4,h)
    elif email.get()!='':
      h=email.get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(5,h)
  for i in range (6):
    Label(text=f"SEARCH BY {info1[i]}",font="Georgia 12",background="white").grid(row=i+1,column=0)
  Label(text='SEARCH STUDENT BY FOLLOWING OPTION',background="white").grid(row=0,column=1)
  roll_no=StringVar()
  roll_entry=Entry(root,textvariable=roll_no,font="Georgia 12",background="white").grid(row=1,column=1)
  en_no=StringVar()
  en_entry=Entry(root,textvariable=en_no,font="Georgia 12",background="white").grid(row=2,column=1)
  name=StringVar()
  name_entry=Entry(root,textvariable=name,font="Georgia 12",background="white").grid(row=3,column=1)  
  student_number=StringVar()
  student_number_entry=Entry(root,textvariable=student_number,font="Georgia 12",background="white").grid(row=4,column=1)  
  parent_number=StringVar()
  parent_number_entry=Entry(root,textvariable=parent_number,font="Georgia 12",background="white").grid(row=5,column=1)  
  email=StringVar()
  email_entry=Entry(root,textvariable=email,font="Georgia 12",background="white").grid(row=6,column=1)
  Button(root,text="SEARCH",command=find,font="Georgia 12",background="white").grid(row=7,column=1)
  def admin_change(i):
    roll_no1=StringVar()
    roll_entry=Entry(root,textvariable=roll_no1,font="Georgia 12",background="white").grid(row=1,column=2)
    en_no1=StringVar()
    en_entry=Entry(root,textvariable=en_no1,font="Georgia 12",background="white").grid(row=2,column=2)
    name1=StringVar()
    name_entry=Entry(root,textvariable=name1,font="Georgia 12",background="white").grid(row=3,column=2)  
    student_number1=StringVar()
    student_number_entry=Entry(root,textvariable=student_number1,font="Georgia 12",background="white").grid(row=4,column=2)  
    parent_number1=StringVar()
    parent_number_entry=Entry(root,textvariable=parent_number1,font="Georgia 12",background="white").grid(row=5,column=2)  
    email1=StringVar()
    email_entry=Entry(root,textvariable=email1,font="Georgia 12",background="white").grid(row=6,column=2)
    Button(root,text="APPLY",command=lambda:change1(i),font="Georgia 12",background="white").grid(row=7,column=2)
    def change1(i):
      change=[roll_no1.get(),en_no1.get(),name1.get(),student_number1.get(),parent_number1.get(),email1.get()]
      for h in range(6):
        if change[h]=='':
          change[h]=df.loc[i,info[h]]   
      df.loc[i]=change
      df.to_csv("Roll list.csv",index=False)
      for widget in root.winfo_children():
        widget.destroy()
      print_info(i)
      Button(root,text="BACK",command=lambda:back(),font="Georgia 12",background="white").grid(row=7,column=0)
      Button(root,text="COLSE",command=root.destroy,font="Georgia 12",background="white").grid(row=7,column=1)
    def back():
      for widget in root.winfo_children():
        widget.destroy()
      edit()
#====================================================================================================
def main():
  root.geometry("650x400")
  global photo
  photo=PhotoImage(file=BACKGROUND)
  Label(root,image=photo).place(x=0,y=0)
  root.title("WELCOME")
  def admin_login():
    for widget in root.winfo_children():
      widget.destroy()
    admin()
  def student():
    for widget in root.winfo_children():
      widget.destroy()
    student_login()
  Button(text="  ADMIN  LOGIN  \nEDIT THE INFORMATION(ADMIN)",font="Georgia 12",command=admin_login,background="white").place(x=180,y=100)
  Button(text="STUDENT LOGIN \n EDIT THE INFORMATIOM(STUDENT)",font="Georgia 12",command=student,background="white").place(x=165,y=160)
  Button(text="       EXIT        ",font="Georgia 12",command=root.destroy,background="white").place(x=260,y=220)
if __name__ == "__main__":
    main()
root.mainloop()