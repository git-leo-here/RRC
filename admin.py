def runAdmin():

        import mysql.connector

        usr = input("Enter mySQL Username: ") #Taking Username From User
        pwd =  input("Enter mySQL  Password: ")       

        def addTeacher(Teachername,ClassSec):
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("INSERT INTO adminTeacher (Name,ClassSec) VALUES ('{Teachername}','{ClassSec}') ;".format(Teachername=Teachername,ClassSec=ClassSec))
                create_exam_tables(ClassSec)
                mydb.commit()

        def create_exam_tables(ClassSec):
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS `marks_{ClassSec}` ( roll_no INT(3) AUTO_INCREMENT , Computer INT , Math INT , English INT , Science INT , SocialScience INT , Obtained INT , Percentage INT , PRIMARY KEY (roll_no) ) ;".format(ClassSec=ClassSec))
                cursor.execute("CREATE TABLE IF NOT EXISTS `student_{ClassSec}` ( roll_no INT(3) AUTO_INCREMENT , StudentName VARCHAR(32) NOT NULL , GuardianName VARCHAR(32) NOT NULL , DOB DATE , PRIMARY KEY (roll_no) );".format(ClassSec=ClassSec))

        def manageStudent():
                #Printing Welcome Message And options For This Program
                print(""" 

        ---------------------------------------------
        |===========================================| 
        |======== Welcome To ADMIN section =========|
        |===========================================|
        ---------------------------------------------

        Enter 1 : To Add Teacher  
        Enter 2 : To View Teachers  
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
                        addTeacher(Teachername,Class+Sec)
                        print("Teacher has been added to database")
                
                elif(userInput == 2): #This Option Will view Students
                        # SELECT * FROM `adminStudent`
                        pass
                else:
                        print("\nHey! That's Not A Valid Option")
                                

        manageStudent()
