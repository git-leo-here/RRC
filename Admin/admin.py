import os
import platform


def manageStudent(): #Function For The Student Management System

        x = "#" * 30
        y = "=" * 28
        global bye #Making Bye As Super Global Variable
        bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===> code-projects.org <===  #\n# {} #\n {}".format(x, y, y, x) # Will Print GoodBye Message

        #Printing Welcome Message And options For This Program
        print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To ADMIN Management System ==========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To Add Teacher 
Enter 2 : To Remove Teacher 
Enter 3 : To Add Student 
Enter 4 : To Add Class 
                """)

        try: #Using Exceptions For Validation
                userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
        except ValueError:
                exit("\nHy! That's Not A Number") #Error Message
        else:
                print("\n") #Print New Line

        #Checking Using Option  
        if(userInput == 1): #This Option Will Add Teacher
                import csv
                with open('registration.txt','a',newline="") as fo: #open the file in append mode (add to file, we don't wish to overwrite!)
                        Writer=csv.writer(fo) #fo = file out (this can be called anything you like)
                        Teacherid=input("Enter Teacher ID:")
                        Teachername=input("Enter firstname:")
                        Class=input("class")
                        Writer.writerow([Teacherid,Teachername,Class])
                        print("Record has been written to file")

        elif(userInput == 2): #This Option Will Reamove Student
                newStd = input("Enter New Student: ")
                if(newStd in listtchr): #This Condition Checking The New Student Is Already In List Ur Not
                        print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
                else:   
                        listtchr.append(newStd)
                        print("\n=> New Student {} Successfully Add \n".format(newStd))
                        for students in listtchr:
                                print("=> {}".format(students)) 

        elif(userInput == 3): #This Option Will ADD Student
                import csv
                with open('student.txt','a',newline="") as fo: #open the file in append mode (add to file, we don't wish to overwrite!)
                        Writer=csv.writer(fo) #fo = file out (this can be called anything you like)
                        Studentid=input("Enter Student ID:")
                        Studentname=input("Enter firstname:")
                        DOB=input("Enter DOB:")
                        Class=int(input("class"))
                        Sec=str(input("Section"))
                        Writer.writerow([Studentid,Studentname,DOB,Class,Sec])
                        print("Record has been written to file")
        
        elif(userInput == 4): #This Option Will ADD Class
                import csv
                with open('CLASS.txt','a',newline="") as fo: #open the file in append mode (add to file, we don't wish to overwrite!)
                        Writer=csv.writer(fo) #fo = file out (this can be called anything you like)
                        Studentid=input("Enter Student ID:")
                        Teacherid=input("Enter Teacherid:")
                        Classname=input("Enter firstname:")
                        Writer.writerow([Studentid,Teacherid,Classname])
                        print("Record has been written to file")
                        
#brought to you by code-projects.org
manageStudent()

def runAgain(): #Making Runable Problem1353
        runAgn = input("\nwant To Run Again Y/n: ")
        if(runAgn.lower() == 'y'):
                if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
                        print(os.system('cls')) 
                else:
                        print(os.system('clear'))
                manageStudent()
                runAgain()
        else:
                quit(bye) #Print GoodBye Message And Exit The Program

runAgain()
