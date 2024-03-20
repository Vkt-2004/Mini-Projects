'''Login into the database'''
'''Password changes every day'''
#A password is said to be valid if it starts with a
#digit and it has length 6 or more. If your program determines
#that the user-entered password is not valid, it should print a
#message saying so. Otherwise, it should print a message saying
#that it has accepted the user-entered password.
print('\t','\t','WELCOME TO MEDANTA THE MEDICITY','\t','\t')
a=input("Enter your password:")
for i in a:
    if len(a)>=6:
        if i.isdigit():
            print("THE PASSWORD ENTERED IS ACCEPTED")
            break
        else:
            print("THE PASSWORD IS INVALID")
            print("THE PASSWORD SHOULD START WITH A DIGIT")
            break
    else:
        print("THE PASSWORD IS INVALID")
        print("THE PASSWORD SHOULD CONTAIN ATLEAST 6 CHARACTERS")
        break


import csv
import datetime
def createrecord():
    with open('Hospital.csv',mode='a',newline='') as f:
        mywriter=csv.writer(f,delimiter=',')
        while True:
            PNo=int(input("Enter patient number:"))
            name=input("Enter patient's name:")
            age=int(input("Enter patient's age:"))
            date=str(input("Enter date of admission:"))
            prob=input("Enter patient's problem:")
            Line=[PNo,name,age,date,prob]
            mywriter.writerow(Line)
            ch=input("Do you want to enter more records:")
            if ch.upper()=='N':
                break
        f.close()


def searchrecord():
    with open('Hospital.csv',mode='a',newline='') as f:
        myreader=csv.reader(f)
        PNO=int(input("Enter the patient number you want to search:"))
        for row in myreader:
            if(row[0]==PNO):
                print(row)
    f.close()


def deleterecord():
        lines = list()
        pno=int(input("Enter patient's number who has been discharged from the hospital and is to be deleted:"))
        with open('Hospital.csv',mode='r',newline='') as f:
            myreader1=csv.reader(f)
            for row in myreader1:
                lines.append(row)
            for field in row:
                if field==pno:
                    lines.remove(row)
        print("The record is deleted")
        f.close()
print('\t','\t','MEDANTA THE MEDICITY','\t','\t')
print('\t','\t','HOSPITAL MANAGEMENT SYSTEM','\t')
print('\t','\t','\t','MENU','\t','\t','\t')
print('1.ADMIT PATIENT/ADD RECORD')
print('2.SEARCH A RECORD')
print('3.PATIENT DISCHARGED/DELETE RECORD')
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        createrecord()
    elif choice==2:
        searchrecord()
    elif choice==3:
        deleterecord()
    else:
        print("Choice Invalid")
        print("Please enter number from 1/2/3")























    
