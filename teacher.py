def runAgain():
    import mysql.connector
    usr = input("Enter mySQL Username: ") #Taking Username From User
    pwd =  input("Enter mySQL  Password: ")

    def addStudent(Studentname , GuardianName ,  DOB  ):
            mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
            cursor = mydb.cursor()
            cursor.execute("INSERT INTO adminStudent (Studentname , GuardianName , DOB ) VALUES ({Studentname},{GuardianName},{DOB}) ;")
            mydb.commit()


    #Printing Welcome Message And options For This Program
    print(""" 

    ------------------------------------------------------
    |======================================================| 
    |======== Welcome To Student Management System ==========|
    |======================================================|
    ------------------------------------------------------

    Enter 1 : To Add Student 
    Enter 2 : To View Students  
                    """)


    try: #Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
            exit("\nHey! That's Not A Valid Number") #Error Message
    else:
            print("\n") #Print New Lin
            if(userInput == 1): #This Option Will ADD Student
                StudentName =input("Enter student's name:")
                GuardianName=input("Enter guardian's name:")
                DOB=input("Enter DOB:")
                addStudent ( StudentName , GuardianName , DOB )
                print("Record has been written to file")
            elif(userInput == 2): #This Option Will view Students
            # SELECT * FROM `adminStudent`
                pass
            else:
                print("\nHey! That's Not A Valid Option")