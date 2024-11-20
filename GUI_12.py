#ATTEMPT 12 TO CONVERT TERMINAL LOGIC TO GUI
#TRAYING TO UPGRED ATTENDANCE VIWE
import pandas as pd
import string
from tkinter import *
import random
import math
import telerivet
root=Tk()
STUDENT_ACCOUNT=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Screenshot 2024-10-30 113925.png"
STUDENR_PROFILE=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\STUDENT PHOTO.png"
ADMIN_ACCOUNT=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Screenshot 2024-10-30 113343.png"
ID_PASS=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\id_password.csv"
ROLL_LIST=r"C:\Users\harsh\OneDrive\Desktop\coding\ROLL_LIST_2.csv"
BACKGROUND=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\WhatsApp Image 2024-10-30 at 09.13.18_0b004897.png"
BACKGROUND1=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\WhatsApp Image 2024-10-30 at 09.13.16_b1c0104f.png"
CHANGE=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\luxury-black-and-gold-background-with-space-in-the-middle-photo.png"
ATTENDANCE_NAME=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\ATTENDANCE NAME.csv"
#====================================================================================================
file=pd.read_csv(ATTENDANCE_NAME)
df = pd.DataFrame(file)
#====================================================================================================
admin_id_pass=pd.read_csv(ID_PASS)
df1 = pd.DataFrame(admin_id_pass)
id_pass=df1.loc[0].tolist()
#====================================================================================================
info1=['Roll No          :','Enrollment No    :','Name of Student  :','Student Mo       :','Parents Mo       :','E-mail           :']
info=['Roll No.','Enrollment No.','Name of Student','Student Mo.','Parents Mo.','E-mail','ID','PASSWORD','SHORT NAME']
#====================================================================================================
def send_message(info11,info12,mobile_no):
  mobile_no1='9822301670'
  api = telerivet.API('sO8Wr_17yEd1S86Bx2AZ9VCGbeKZSrcqNMsQ')
  project = api.initProjectById('PJ82fb59bb562c1a26')
  if info11!='':
    project.sendMessage(to_number=mobile_no1,content=f"YOUR OTP TO CHANGE PASSSWORD IS {info11[:3]}-{info11[3:]}")
  else:
    project.sendMessage(to_number=mobile_no1,content=f"YOUR CHILD IS NOT PRESENT IN THE LECTURE OF {info12}")
  print("Message sent successfully!")
#====================================================================================================
#👇👇
def presenty():
    root.destroy()
    subject = ''
    def send_alert():
        alert_no = df[info[4]]
        i = 0
        otp = ''
        for j in range(len(alert_no)):
            if i < len(d) and j == int(d[i]):
                number = alert_no[j]
                send_message(otp, subject, number)
                i=i+ 1
                j = 0
        root1.destroy()
    def submit():
        global d
        d = []
        for i in range(len(b)):
            print(b[i].get())
            if b[i].get():
                continue
            else:
                e = str(i + 1)
                d.append(e)
        print(d)
        send_alert()
    def on_mouse_wheel(event):
        if event.delta > 0:
            canvas.yview_scroll(-1, "units")
        else:
            canvas.yview_scroll(1, "units")
    root1 = Tk()
    root1.geometry("400x400")
    file_name = pd.read_csv(ATTENDANCE_NAME)
    df = pd.DataFrame(file_name)
    a = 'box'
    global b
    b = []
    for i in range(len(df)):
        c = a + str(i)
        b.append(c)
    name = df['SHORT NAME']
    canvas = Canvas(root1)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar = Scrollbar(root1, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    for l, present in enumerate(range(len(df))):
        b[present] = IntVar()
        Label(frame, text=name[present]).grid(row=l, column=0, sticky="w", padx=10, pady=5)
        Checkbutton(frame, variable=b[present], font="Georgia 12").grid(row=l, column=1, padx=10, pady=5)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    root1.bind_all("<MouseWheel>", on_mouse_wheel)
    Button(root1, text="SUBMIT \nATTENDANCE", command=submit, font="Georgia 12", relief='solid').place(x=250,y=320)
    root1.mainloop()
#☝️☝️
#====================================================================================================
def register():
  #👇👇
  for widget in root.winfo_children():
    widget.destroy()
  #☝️☝️
  def login():
    def complete():
      a=df[info[6]]
      h=0
      hs=0
      print(id.get()[-10:])
      for i in range (len(a)):
        if id.get()==a[i] or( id.get()[:-10]!='@sgbau.com') or id.get()=='':
          Label(root,text='USER NAME IS NOT AVAILABLE',font="Georgia 10",background="white",foreground="red").place(x=200,y=100)
          return
        else:
          Label(root,text='                                                                                  ',font="Georgia 10",background="white").place(x=200,y=100)
          h=1
      if password.get()!=conform_password.get() or password.get()=='':
        Label(root,text='PASSWORD NOT MATCH',font="Georgia 12",background="white",foreground="red").place(x=200,y=175)
        return
      else:
        Label(root,text='                                                                                  ',font="Georgia 12",background="white").place(x=200,y=175)
        hs=1
      if h==1 and hs==1:
        new_a=df[info[1]]
        length=len(new_a)
        new_list=[(length+1)]
        for i in range(5):
          if new[i].get()!='':
            s=new[i].get()
          else:
            s='N.A.'
          new_list.append(s)
        new_list.append(id.get())
        new_list.append(password.get())
        df.loc[length]=new_list
        df.to_csv(ROLL_LIST,index=False)
        print(new_list)
    Label(root,image=p4).place(x=0,y=0)
    Label(root,text='CREATE USER NAME',font="Georgia 12",background="white").place(x=200, y=50)
    id=StringVar()
    Entry(root,textvariable=id,font="Georgia 12").place(x=200,y=75)
    Label(root,text="PASSWORD",font="Georgia 12",background="white").place(x=200, y=125)
    password=StringVar()
    Entry(root,textvariable=password,font="Georgia 12").place(x=200,y=150)
    Label(root,text="CONFORM PASSWORD",font="Georgia 12",background="white").place(x=200, y=200)
    conform_password=StringVar()
    Entry(root,textvariable=conform_password,font="Georgia 12").place(x=200,y=225)   
    Button(root,text='FINISH',command=complete).place(x=200,y=250) 
  global p4,new
  p4=PhotoImage(file=BACKGROUND1)
  Label(root,image=p4).place(x=0,y=0)
  new=['ENROLLMENT NO','NAME','SUTDENT MOBILE NO','PARENTS MOBIME NO','EMAIL ID','ID','PASSWORD']
  for i in range (5):
    Label(root,text=new[i],font="Georgia 12",background="white").place(x=50,y=50+(25*i))
  for i in range (5):
    new[i]=StringVar()
    Entry(root,textvariable=new[i],font="Georgia 12").place(x=250,y=50+(i*25))
  Label(root,text="CAPITAL LETTER ONLY",font="Georgia 8",background="white",foreground="red").place(x=450,y=75)
  Button(root,text="REGISTER",command=login,font="Georgia 12").place(x=200,y=200)
#====================================================================================================
def delete_info(i):
  print(i)
  global df
  for s in range(i,len(df[info[0]])-1):
    df.loc[s]=df.loc[s+1]
    df.loc[s,'Roll No.']=s+1
  #👇👇
  df=df.drop(len(df)-1)
  #☝️☝️
  df.to_csv(ROLL_LIST,index=False)  
#====================================================================================================
def forgot_password_admin():
  def change_admin_password(otp):
    for widget in root.winfo_children():
      widget.destroy()
    global p5
    p5=PhotoImage(file=CHANGE)
    Label(root,image=p5).place(x=0,y=0)
    Label(text="ENTER OTP",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
    def verify():
      if otp==otp_entry.get():
        def changepassword():
          id_pass[1]=new_password.get()
          df1.loc[0]=id_pass
          df1.to_csv(ID_PASS,index=False)
          for widget in root.winfo_children():
            widget.destroy()
          admin()
        Label(text="ENTER PASSWORD HERE",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=220)
        new_password=StringVar()
        Entry(root,textvariable=new_password,font="Georgia 12 bold").place(x=200,y=250)
        Button(root,text='CHANGE',command=changepassword).place(x=200,y=280)
      else:
        Label(root,text="RE-ENTER OTP",background="#333333",foreground="red",font="Georgia 12 bold").place(x=300,y=190)
    otp_entry=StringVar()
    Entry(root,textvariable=otp_entry,font="Georgia 12 bold").place(x=200,y=160)
    Button(root,text="SUBMIT",command=verify).place(x=200,y=190)
  #👇👇
  data='0123456789'
  length=len(data)
  otp=''
  mess=''
  for x in range(6):
    otp+=data[math.floor(random.random()*length)]
  send_message(otp,mess)
  #☝️☝️
  change_admin_password(otp)
#====================================================================================================
def forgot_password_student():
  def change_student_password():
    b=df[info[3]]
    for h in range (len(b)):
      if b[h]==number_entry.get():
        global z
        z=h
        a=''
        data='0123456789'
        length=len(data)
        otp=''
        for x in range(6):
          otp+=data[math.floor(random.random()*length)]
        number=number_entry.get()
        send_message(otp,a,number)
        break
    for widget in root.winfo_children():
      widget.destroy()
    def verify():
      if otp==otp_entry.get():
        def changepassword():
          df.loc[z,info[7]]=new_password.get()
          df.to_csv(ROLL_LIST,index=False)
          for widget in root.winfo_children():
            widget.destroy()
          student_login()
        Label(text="ENTER PASSWORD HERE",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=220)
        new_password=StringVar()
        Entry(root,textvariable=new_password,font="Georgia 12 bold").place(x=200,y=250)
        Button(root,text='CHANGE',command=changepassword).place(x=200,y=280)
      else:
        Label(root,text="RE-ENTER OTP",background="#333333",foreground="red",font="Georgia 12 bold").place(x=300,y=190)
    Label(root,image=p5).place(x=0,y=0)
    Label(text="ENTER OTP",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
    otp_entry=StringVar()
    Entry(root,textvariable=otp_entry,font="Georgia 12 bold").place(x=200,y=160)
    Button(root,text="SUBMIT",command=verify).place(x=200,y=190)        
  for widget in root.winfo_children():
    widget.destroy()
  global p5
  p5=PhotoImage(file=CHANGE)
  Label(root,image=p5).place(x=0,y=0)
  Label(text="ENTER MOBILE NO",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
  number_entry=StringVar()
  Entry(root,textvariable=number_entry,font="Georgia 12 bold").place(x=200,y=160)
  Button(root,text="SEND OTP",font="Georgia 12 bold",command=change_student_password).place(x=200,y=200)
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
    id_search=df[info[6]]
    for index in range (len(id_search)):
      if id.get()==id_search[index]:
        break
    password_search=df.loc[index].tolist()
    if password.get()==password_search[7]:
      for widget in root.winfo_children():
        widget.destroy()
      print_info(index)
      i=index
      Button(text="EDIT",command=lambda:sedit(i),font="Georgia 12",background="white").place(x=105,y=190)
      Button(text="BACK",command=lambda:sedit(-1),font="Georgia 12",background="white").place(x=230,y=190)
    else:
      #👇👇
      custom_box = Toplevel(root)
      custom_box.title("Custom Message Box")
      custom_box.geometry("300x90")
      custom_box.resizable(False, False)
      Label(custom_box, text="INCORRECT ID PASSWORD",font="Georgia 12",foreground="red").place(x=40,y=10)
      def custom_action():
        forgot_password_student()  
        custom_box.destroy()
      def cancel_action():
        custom_box.destroy()
      Button(custom_box, text="CHANGE PASSWORD", command=custom_action).place(x=10,y=40)
      Button(custom_box, text="RETRY", command=cancel_action).place(x=220,y=40)
      #☝️☝️
  Label(root,image=photo).place(x=0,y=0)
  global p1
  p1=PhotoImage(file=STUDENT_ACCOUNT)
  Label(root,image=p1,borderwidth=0).place(x=270,y=75)
  Label(text="STUDENT ID::",font="Georgia 12",background="white").place(x=200, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=200,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",background="white").place(x=200, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",background="white")
  passentry.place(x=200, y=290)
  #👇👇
  def toggle_password():
      if show_password_var.get():
          passentry.config(show="")
          return
      else:
          passentry.config(show="•")
          return
  show_password_var = IntVar()
  Checkbutton(root,variable=show_password_var,background="white",command=toggle_password).place(x=450,y=310)
  #☝️☝️
  #҈֍•
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",background="white").place(x=260,y=330)
#====================================================================================================
def student_edit(j):
  def submit(j):
    change=[]
    for h in range (6):
      b=entry[h].get()
      change.append(b)
    for h in range(6):
      if change[h]=='':
        change[h]=df.loc[j,info[h]]      
    df.loc[j]=change
    df.to_csv(ROLL_LIST,index=False)
    for widget in root.winfo_children():
      widget.destroy()
    print_info(j)
    Button(text="CLOSE",command=root.destroy,font="Georgia 12",background="white").grid(row=7,column=1)
  global entry
  entry=['rool_no','en_no','name','student_number','parent_number','email']
  b=df.loc[i].tolist()
  for h in range (6):
    if ((b[h]=='' or b[h]=='N.A.') or (h>1 and h!=4)):
      entry[h]=StringVar()
      Entry(root,textvariable=entry[h],font="Georgia 10",background="white").place(x=470,y=40+(25*h))
    else:
      continue
  Button(root,text="EDIT INFO",command=lambda:submit(j),font="Georgia 12",background="white").place(x=470,y=190)
#====================================================================================================
def print_info(i):
  a=df.loc[i].tolist()
  global p3,p4
  p4=PhotoImage(file=BACKGROUND1)
  Label(root,image=p4).place(x=0,y=0)
  p3=PhotoImage(file=STUDENR_PROFILE)
  Label(root,image=p3).place(x=0,y=45)
  for j in range (6):
    Label(text=info1[j],font="Georgia 12",background="white").place(x=105,y=40+(25*j))
    Label(text=a[j],font="Georgia 12",background="white").place(x=230,y=40+(25*j))
  return i
#====================================================================================================
def admin():
  def check():
    if id.get()==id_pass[0] and password.get()==id_pass[1]:
      for widget in root.winfo_children():
        widget.destroy()
      edit()
    else:
      custom_box = Toplevel(root)
      custom_box.title("Custom Message Box")
      custom_box.geometry("300x90")
      custom_box.resizable(False, False)
      Label(custom_box, text="INCORRECT ID PASSWORD",font="Georgia 12",foreground="red").place(x=40,y=10)
      def custom_action():
        forgot_password_admin()  
        custom_box.destroy()
      def cancel_action():
        custom_box.destroy()
      Button(custom_box, text="CHANGE PASSWORD", command=custom_action).place(x=10,y=40)
      Button(custom_box, text="RETRY", command=cancel_action).place(x=220,y=40)
  Label(root,image=photo).place(x=0,y=0)
  global p2
  p2=PhotoImage(file=ADMIN_ACCOUNT)
  Label(root,image=p2,borderwidth=0).place(x=270,y=75)
  Label(text="USER ID::",font="Georgia 12",background="white").place(x=205, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=205,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",relief='solid',borderwidth=2).place(x=205, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",relief='solid',borderwidth=2)
  passentry.place(x=205, y=290)
  def toggle_password():
      if show_password_var.get():
          passentry.config(show="")
          return
      else:
          passentry.config(show="•")
          return
  show_password_var = IntVar()
  Checkbutton(root,variable=show_password_var,background="white",command=toggle_password).place(x=455,y=310)
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",relief='solid').place(x=260,y=330)
#====================================================================================================
def edit():
  '''def delete_info1(i):
    delete_info(i)'''
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
      Button(root,text="EDIT",command=lambda:admin_change(i),font="Georgia 12",background="white").place(x=105,y=190)
      Button(root,text="EXIT",command=back,font="Georgia 12",background="white").place(x=230,y=190)
      Button(root,text="DELETE",command=lambda:delete_info(i),font="Georgia 12",background="white").place(x=355,y=190)
    else:
      print("not found")
  def find():
    if entry[0].get()!='':
      h=entry[0].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(0,h)
    elif entry[1].get()!='':
      h=entry[1].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(1,h)
    elif entry[2].get()!='':
      h=entry[2].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(2,h)
    elif entry[3].get()!='':
      h=entry[3].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(3,h)
    elif entry[4].get()!='':
      h=entry[4].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(4,h)
    elif entry[5].get()!='':
      h=entry[5].get()
      for widget in root.winfo_children():
        widget.destroy()
      searching(5,h)
  global p4
  p4=PhotoImage(file=BACKGROUND1)
  Label(root,image=p4).place(x=0,y=0)
  for i in range (6):
    Label(text=f"SEARCH BY {info1[i]}",font="Georgia 12",background="white").place(x=105,y=40+(25*i))
  Label(text='SEARCH STUDENT BY FOLLOWING OPTION',font="Georgia 12 bold",background="white").grid(row=0,column=1)
  global entry
  entry=['rool_no','en_no','name','student_number','parent_number','email']
  for h in range (6):
    entry[h]=StringVar()
    Entry(root,textvariable=entry[h],font="Georgia 10",background="white").place(x=370,y=40+(25*h))
  Button(root,text="SEARCH",command=find,font="Georgia 12",background="white").place(x=370,y=190)
  def admin_change(i):
    global entry1
    entry1=['rool_no1','en_no1','name1','student_number1','parent_number1','email1']
    for h in range (6):
        entry1[h]=StringVar()
        Entry(root,textvariable=entry1[h],font="Georgia 10",background="white").place(x=470,y=40+(25*h))
    Button(root,text="APPLY",command=lambda:change1(i),font="Georgia 12",background="white").place(x=470,y=190)
    def change1(i):
      change=[]
      for h in range (6):
        b=entry1[h].get()
        change.append(b)
      for h in range(6):
        if change[h]=='':
          change[h]=df.loc[i,info[h]]   
      df.loc[i]=change
      df.to_csv(ROLL_LIST,index=False)
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
  Button(text="  ADMIN  LOGIN  \nEDIT THE INFORMATION(ADMIN)",font="Georgia 12",command=admin_login,background="skyblue",relief='solid').place(x=180,y=100)
  Button(text="STUDENT LOGIN \n EDIT THE INFORMATIOM(STUDENT)",font="Georgia 12",command=student,background="skyblue",relief='solid').place(x=165,y=160)
  Button(text="           REGESTER           ",font="Georgia 12",command=register,background="skyblue",relief='solid').place(x=220,y=220)
  Button(text="           ATTENDACE           ",font="Georgia 12",command=presenty,background="skyblue",relief='solid').place(x=215,y=265)
  root.maxsize(650,400)
  root.minsize(650,400)
if __name__ == "__main__":
    main()
root.mainloop()