#ALL LOGIC WHICH WORKS IN TERMINAL
import pandas as pd
import string
#====================================================================================================
ROLL_LIST=r'C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\Roll list.csv'
file=pd.read_csv(ROLL_LIST)
df = pd.DataFrame(file)
#====================================================================================================
ID_PASS=r"C:\Users\harsh\OneDrive\Desktop\coding\IMAGE OR DATA\id_password.csv"
admin_id_pass=pd.read_csv(ID_PASS)
df1 = pd.DataFrame(admin_id_pass)
id_pass=df1.loc[0].tolist()
#====================================================================================================
info1=['Roll No          :','Enrollment No    :','Name of Student  :','Student Mo       :','Parents Mo       :','E-mail           :']
info=['Roll No.','Enrollment No.','Name of Student','Student Mo.','Parents Mo.','E-mail']
#====================================================================================================
def searching(option):
  a=info[option]
  search=df[info[option]]
  #BETTER LOOK
  if option==0:
    information=int(input(f"ENTER THE {a.upper()} ::"))
    print_info(information-1)
    return
  else:
    information=str(input(f"ENTER THE {a.upper()} ::"))
    for i in range (len(search)):
        if information.lower() in search[i].lower():
          print_info(i)
          return i
  return
#====================================================================================================
def student_login():
  id=input("ENTER THE STUDENT ID::")
  password=input("ENTER THE PASSWORD::")
  id_search=df[info[5]]
  for i in range (len(id_search)):
    if id==id_search[i]:
      break
    elif i>len(id_search):
      print("INVALLID ID PASSWORD")
      i=0
    else:
      continue  
  password_search=df.loc[i].tolist()
  if password==password_search[1]:
    i=print_info(i)
    #STUDENT CHOISE TO EDIT THE INFORMATION
    student=int(input("ENTER 1 TO EDIT INFORMATION ::"))
    if student==1:
      student_edit(i)
    else:
      return
  return
#====================================================================================================
def student_edit(j):
  print("CHOSSE WHAT DO YOU WANT TO EDIT")
  for i, item in enumerate(info, start=1):
    print(f"{i}. {item.upper()}")
    #BETTER LOOK
  option=int(input("ENTER THE OPTION::"))
  #SOME RESTRICTION TO EDIT FOR STUDENT
  if (df.loc[j,info[option-1]]!='N.A.' or option==3 or option==4 or option==6):
    df.loc[j,info[option-1]]=input("ENTER CHANGE::")
    df.to_csv(ROLL_LIST,index=False)
    print("*"*150)
    print_info(j)
#====================================================================================================
def print_info(i):
  a=df.loc[i].tolist()
  print("*"*150)
  for j in range (6):
    print(f"{info1[j]} {a[j]}")
  print("*"*150)
  return i
#====================================================================================================
def admin():
  print("*"*150)
  for i in range(3):
    id=input("ENTER THE ID ::")
    password=input("ENTER THE PASSWORD ::")
    if id==id_pass[0] and password==id_pass[1]:
      print("*"*150)
      print("WELCOME")
      edit()
      return
    else:
      print("INVALID ID OR PASSWORD")
#====================================================================================================
def edit():
    print("*"*150)
    for i, item in enumerate(info, start=1):
        print(f"{i}.SEARCH BY {item.upper()}")
    print("7.SEARCH BY EXIT")
    option=int(input("ENTER THE OPTION::"))
    print("*"*150)
    i=searching(option-1)
    print("*"*150)
    #ADMIN COISE TO EDIT OR NOT
    admin_change=int(input("ENTER 8 TO EDIT THE INFORMATION::"))
    if admin_change==8:
      option=int(input("ENTER WHICH INFORMATION YOU WANT TO EDIT IN THE SEQUENCE OF ABOVE::"))
      if option==1:
        df.loc[i,info[0]]=input('ENTER THE NEW ROLL NUMBER::')
        df.to_csv(ROLL_LIST, index=False)
      elif option==2:
        check=input('ENTER THE NEW ENROLLMENT NUMBER::')
        if check[:2]=='EN':
          df.loc[i,info[1]]=input('ENTER THE NEW ENROLLMENT NUMBER::')
          df.to_csv(ROLL_LIST, index=False)
        else:
          print("INVALID SYNTAK")
          return
      elif option==3:
        df.loc[i,info[2]]=input('ENTER THE NEW NAME IN FORMAT OF [STUDENT NAME]_[FATHER NAME]_[SURNAME]::')
        df.to_csv(ROLL_LIST, index=False)
      elif option==4:
        check=input('ENTER THE NEW STUDENT MOBILE NUMBER::')
        if len(check)==10:
          df.loc[i,info[3]]=input('ENTER THE NEW STUDENT MOBILE NUMBER::')
          df.to_csv(ROLL_LIST, index=False)
        else:
          print("INVALID SYNTAK")
          return
      elif option==5:
        check=input('ENTER THE NEW PARENTS MOBILE NUMBER::')
        if len(check)==10:
          df.loc[i,info[4]]=check
          df.to_csv(ROLL_LIST, index=False)
        else:
          print("INVALID SYNTAK")
          return
      elif option==6:
        check=input('ENTER THE NEW EMAIL ID::')
        if check[-10:]=="@gmail.com":
          df.loc[i,info[6]]=input('ENTER THE NEW EMAIL ID::')
          df.to_csv(ROLL_LIST, index=False)
        else:
          print("INVALID SYNTAK")
          return
      else:
        return
#====================================================================================================
def main():
  print("*"*150)
  print("1.ADMIN  LOGIN / EDIT THE INFORMATION(ADMIN)")
  print("2.STUDENT LOGIN / EDIT THE INFORMATIOM(STUDENT)")
  print("3.EXIT")
  option=int(input("ENTER THE OPTION::"))
  print("*"*150)
  if option==1:
    admin()
  elif option==2:
    student_login()
  elif option>3:
    return
#====================================================================================================
if __name__ == "__main__":
    main()

