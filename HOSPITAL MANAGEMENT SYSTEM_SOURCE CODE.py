##hospital management system
##PRINTING WELCOME NOTE
from tabulate import tabulate
def menu_fmt(x):
    x="#"+x[0:]
    for i in range(len(x)):
        if x[i]=='\n':
            x=x[:i+1]+"#"+x[1+i:]
    x=x.replace('#','\t\t\t\t')
    print(x)
while(True):
    print("""
                                            =================================================================================
             
                                                                   WELCOME TO MEDANTA THE MEDICITY 

                                            =================================================================================
    """)
    ##creating database connectivity
    import mysql.connector
    passwd=str(input("ENTER THE DATABASE PASSWORD;"))
    
    mysql=mysql.connector.connect(host="localhost",user="root",passwd=passwd)
    mycursor=mysql.cursor()
    #creating database
    mycursor.execute("create database if not exists project")
    mycursor.execute("use project")
    #creating the tables we need
    mycursor.execute("create table if not exists patient_details(name varchar(30) primary key,sex varchar(10),age int(3),problem varchar(50),address varchar(30),contact bigint)")
    mycursor.execute("create table if not exists doctor_details(name varchar(30) primary key,specialisation varchar(40),age int(3),contact bigint,fees int(10),monthly_salary int(10))")
    mycursor.execute("create table if not exists nurse_details(name varchar(30) primary key,age int(3),contact bigint,monthly_salary int(10))")
    
    #login or signup option
    #creating table for storing the username and password of the user
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
    #printing option
    while(True):
        print("""
                                                                     1. SIGN IN (LOGIN)
                                                                     2. SIGN UP (REGISTER)
                                                                                """)
    
        r=int(input("enter your choice:"))
    
    
    
        #IF USER WANTS TO REGISTER
        if r==2:
            print("""

                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLEASE REGISTER YOURSELF!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                    """)
            u=input("ENTER YOUR PREFERRED USERNAME!!:")
            p=input("ENTER YOUR PREFERRED PASSWORD (PASSWORD SHOULD BE STRONG!!!:")
            #ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
            mycursor.execute("insert into user_data values('"+u+"','"+p+"')")
            mysql.commit()
    
    
            print("""
                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                    """)
            x=input("enter any key to continue:")
        #IF USER WANTS TO LOGIN
        elif r==1:
        
        #PRINTING THE SIGNIN OPTION AGAIN TO THE USER AFTER REGISTRATION

                print("""
                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{SIGN IN }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                        """)
                un=input("ENTER THE USERNAME!!:")
                ps=input("ENTER THE PASSWORD!!:")
                
                mycursor.execute("select password from user_data where username='"+un+"'")
                row=mycursor.fetchall()
                for i in row:
                    a=list(i)
                    if a[0]==str(ps):
                        while(True):
                            ##displaying the task you can perform
                            print("""
                                                                      1.ADMINISTRATION
                                                                      2.PATIENT (ADMISSION AND DISCHARGE PROCESS)
                                                                      3.SIGN OUT
                                                                      
                                                                      """)
    

                            ##asking for the task from user
                            a=int(input("ENTER YOUR CHOICE:"))
                            #if user wants to enter administration option
                            if a==1:
                                print("""
                                                                      1. SHOW DETAILS
                                                                      2. ADD NEW MEMBER
                                                                      3. DELETE EXISTING ONE
                                                                      4. EXIT
                                                                          """)
                                b=int(input("ENTER YOUR CHOICE:"))
                                #showing the existing details
                                if b==1:
                                    print("""
                                                                      1. DOCTOR DETAILS
                                                                      2. NURSE DETAILS
                                                                                
                                                                                """)
                                    
                                    
                                    #ASKING USER'S CHOICE
                                    c=int(input("ENTER YOUR CHOICE:"))
                                    #if user wants to see the details of doctors 
                                    if c==1:
                                        mycursor.execute("select * from doctor_details")
                                        row=mycursor.fetchall()
                                        menu_fmt(tabulate(row,headers=["NAME","SPECIALISATION","AGE","CONTACT","FEES","MONTHLY_SALARY"],tablefmt='fancy_grid'))
                                        
                                    #if user wants to see the details of nurses    
                                    elif c==2:
                                        mycursor.execute("select * from nurse_details")
                                        row=mycursor.fetchall()
                                        menu_fmt(tabulate(row,headers=["NAME","AGE","CONTACT","MONTHLY_SALARY"],tablefmt='fancy_grid'))
                                        
                                    
                                #IF USER WANTS TO ENTER DETAILS
                                elif b==2:
                                    print("""

                                                                      1. DOCTOR DETAILS
                                                                      2. NURSE DETAILS
                                                                                    
                                                                                    """)
                                    c=int(input("ENTER YOUR CHOICE:"))
                                    #FOR ENTERING DETAILS OF DOCTORS
                                    if c==1:
                                      #ASKING THE DETAILS
                                      name=input("ENTER DR. NAME:")
                                      spe=input("ENTER SPECIALISATION:")
                                      age=input("ENTER AGE:")
                                      cont=input("ENTER CONTACT NO.:")
                                      fees=input("ENTER FEES:")
                                      ms=input("ENTER MONTHLY_SALARY:")
                                      #INSERTING VALUES ENTERED INTO THE DOCTORS_TABLE
                                      mycursor.execute("insert into doctor_details values('"+name+"','"+spe+"','"+age+"','"+cont+"','"+fees+"','"+ms+"')")
                                      mysql.commit()
                                      print("SUCCESSFULLY ADDED")
                                    #for entering nurse details
                                    elif c==2:
                                      #ASKING THE DETAILS
                                      name=input("ENTER NURSE NAME:")
                                      age=input("ENTER AGE:")
                                      cont=input("ENTER CONTACT NO.:")
                                      ms=int(input("ENTER MONTHLY_SALARY:"))
                                      #INSERTING VALUES ENTERED TO THE TABLE
                                      mycursor.execute("insert into nurse_details values('"+name+"','"+age+"','"+cont+"','"+str(ms)+"')")
                                      mysql.commit()
                                      print("SUCCESSFULLY ADDED")
                                    
                                   
                                #if user wants to delete data
                                elif b==3:
                                   print("""
                                                                      1. DOCTOR DETAILS
                                                                      2. NURSE DETAILS
                                                                                    
                                                                                    """)
                                   c=int(input("ENTER YOUR CHOICE:"))
                                   #deleting doctor's details
                                   if c==1:
                                       name=input("ENTER DOCTOR'S NAME:")
                                       p=input("you really want to delete this data? (y/n):")
                                       if p=='y':
                                           data="DELETE FROM doctor_details WHERE name='"+name+"'"
                                           query=data.format(name)
                                           mycursor.execute(query)
                                           mysql.commit()
                                           print("SUCCESSFULLY DELETED!!")
                                           print("""
                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{AFTER DELETION }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                        """)
                                           mycursor.execute("select * from doctor_details")
                                           row=mycursor.fetchall()
                                           menu_fmt(tabulate(row,headers=["NAME","SPECIALISATION","AGE","CONTACT","FEES","MONTHLY_SALARY"],tablefmt='fancy_grid'))
                                       else:
                                           print("NOT DELETED")


                                   #deleting nurse details
                                   elif c==2:
                                       name=input("ENTER NURSE'S NAME:")
                                       p=input("you really want to delete this data? (y/n):")
                                       if p=='y':
                                           data="DELETE FROM nurse_details WHERE name='"+name+"'"
                                           query=data.format(name)
                                           mycursor.execute(query)
                                           mysql.commit()
                                           print("SUCCESSFULLY DELETED!!")
                                           print("""
                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{AFTER DELETION }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                        """)
                                           mycursor.execute("select * from nurse_details")
                                           row=mycursor.fetchall()
                                           menu_fmt(tabulate(row,headers=["NAME","AGE","CONTACT","MONTHLY_SALARY"],tablefmt='fancy_grid'))
                                       else:
                                           print("NOT DELETED")
                                       
                                elif b==4:
                                    print("THANK YOU")
                                    break
                               
                            #entering the patient details table
                            elif a==2:
                                
                                print("""
                                                                      1. SHOW  PATIENT DETAILS
                                                                      2. ADD  NEW PATIENT
                                                                      3. DISCHARGE PATIENT
                                                                      4. EXIT
                                                                          """)
                                b=int(input("ENTER YOUR CHOICE:"))
                                #showing the existing details
                                #if user wants to see the details of patient
                                if b==1:
                                    mycursor.execute("select * from patient_details")
                                    row=mycursor.fetchall()
                                    menu_fmt(tabulate(row,headers=["NAME","SEX","AGE","PROBLEM","ADDRESS","CONTACT"],tablefmt='fancy_grid'))
                                    
                                    
                                #adding new patient
                                elif b==2:
                                    name=str(input("ENTER NAME: "))
                                    sex=str(input("ENTER SEX: "))
                                    age=str(input("ENTER AGE: "))
                                    problem=str(input("ENTER PROBLEM:"))
                                    address=str(input("ADDRESS: "))
                                    contact=str(input("CONTACT NUMBER: "))
                                    mycursor.execute ("insert into patient_details values('"+str(name)+"','"+str(sex)+"','"+str(age)+"','"+str(problem)+"','"+str(address)+"','"+str(contact)+"')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                                    
                                #discharge process
                                elif b==3:
                                    name=input("ENTER PATIENT'S NAME:")
                                    bill=input("HAS THE PATIENT PAID ALL THE BILLS ? (y/n):")
                                    if bill=='y':
                                        data="DELETE FROM patient_details WHERE name='"+name+"'"
                                        query=data.format(name)
                                        mycursor.execute(query)
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                        print("""
                                            =================================================================================
                                            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{AFTER DELETION }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                            =================================================================================
                                                        """)
                                        mycursor.execute("select * from patient_details")
                                        row=mycursor.fetchall()
                                        menu_fmt(tabulate(row,headers=["NAME","SEX","AGE","PROBLEM","ADDRESS","CONTACT"],tablefmt='fancy_grid'))
                                    else:
                                        print("BILL NOT PAID")
                                        print("NOT DELETED")
                                    
                                #if user wants to exit
                                elif b==4:
                                    print("THANK YOU")
                                    break
                            ###SIGN OUT
                            elif a==3:
                                print("SIGNED OUT")
                                break
                                    
                                
                   #IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
                    else:
                        print("USERNAME OR PASSWORD NOT IN DATABSE")
                        

