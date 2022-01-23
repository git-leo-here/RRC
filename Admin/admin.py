def runAdmin():
        import os
        import platform
        import mysql.connector

        usr = input("Enter mySQL Username: ") #Taking Username From User
        pwd =  input("Enter mySQL  Password: ")       

        def addTeacher(Teachername,ClassSec,Password):
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("INSERT INTO adminTeacher (Name,password,ClassSec) VALUES ({Teachername},{Password},{ClassSec}) ;")
                create_exam_table(ClassSec)
                mydb.commit()

        def create_exam_table(ClassSec):
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS `exam_{ClassSec}` (`sub_code` varchar(3) NOT NULL,`roll_no` int NOT NULL,`marks` int DEFAULT NULL,`test` varchar(3) NOT NULL);")
                mydb.commit()

        def manageStudent(): 
                #Printing Welcome Message And options For This Program
                print(""" 

        ------------------------------------------------------
        |======================================================| 
        |======== Welcome To ADMIN Management System ==========|
        |======================================================|
        ------------------------------------------------------

        Enter 1 : To Add Teacher 
        Enter 2 : To Add Student 
        Enter 3 : To View Students  
                        """)

                try: #Using Exceptions For Validation
                        userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
                except ValueError:
                        exit("\nHey! That's Not A Valid Number") #Error Message
                else:
                        print("\n") #Print New Line

                #Checking Using Option  
                if(userInput == 1): #This Option Will Add Teacher
                        
                        Teachername=input("Enter firstname:")
                        Class=input("Enter teacher's class :")
                        Sec=input("Enter teacher's section :")
                        Password=input("Enter password:")
                        addTeacher(Teachername,Class+Sec,Password)
                        print("Teacher has been added to database")



                elif(userInput == 2): #This Option Will ADD Student
                        StudentName=input("Enter student's name:")
                        GuardianName=input("Enter guardian's name:")
                        DOB=input("Enter DOB:")
                        addStudent(StudentName , GuardianName , DOB )
                        print("Record has been written to file")
                
                elif(userInput == 3): #This Option Will view Students
                        # SELECT * FROM `adminStudent`
                else:
                        exit("\nHey! That's Not A Valid Option")
                                

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
                        quit("bye") #Print GoodBye Message And Exit The Program

        runAgain()              
