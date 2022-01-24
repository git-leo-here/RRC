import mysql.connector 
def runTeacher(classSec):
        usr = input("Enter mySQL Username: ") #Taking Username From User
        pwd =  input("Enter mySQL  Password: ")
        # classSec = input("Enter class and Section: ")
        def addStudent(Studentname , GuardianName ,  DOB  ):
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("INSERT INTO student_{classSec} (Studentname , GuardianName , DOB ) VALUES ({Studentname},{GuardianName},{DOB}) ;".format(classSec=classSec,Studentname=Studentname,GuardianName=GuardianName,DOB=DOB))   

        def viewStudents(): 
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM student_{classSec} LEFT JOIN exam_{classSec} ON exam_{classSec}.roll_no = student_{classSec}.roll_no;".format(classSec = classSec))
                
                myresult = cursor.fetchall()
                for row in myresult:
                        print(row)
        
        def addMarks():
                comp_marks = input("Enter Computer Marks: ")
                math_marks = input("Enter Math Marks: ")
                english_marks = input("Enter English Marks: ")
                science_marks = input("Enter Science Marks: ")
                ssc_marks = input("Enter Social Science Marks: ")
                obtained_marks = comp_marks+ math_marks + english_marks + science_marks + ssc_marks    #add subjects
                percentage = round((obtained_marks/500)*100)
                mydb = mysql.connector.connect(host="localhost",user= usr ,passwd= pwd, database="school")
                cursor = mydb.cursor()
                cursor.execute("INSERT INTO marks_{classSec} (Computer , Math , English , Science , SocialScience , Obtained , Percentage ) VALUES ({Computer},{Math},{English},{Science},{SocialScience},{Obtained},{Percentage}) ;".format(classSec=classSec,Computer=comp_marks,Math=math_marks,English=english_marks,Science=science_marks,SocialScience=ssc_marks,Obtained=obtained_marks,Percentage=percentage))

        #Printing Welcome Message And options For This Program
        print(""" 

        ------------------------------------------------------
        |======================================================| 
        |======== Welcome To Student Management System ==========|
        |======================================================|
        ------------------------------------------------------

        Enter 1 : To Add Student 
        Enter 2 : To View Students
        Enter 3 : To Add Marks  
                        """)


        try: #Using Exceptions For Validation
                userInput = int(input("Please Select from the Above Options: ")) #Will Take Input From User
        except ValueError:
                print("\nHey! That's Not A Valid Number") #Error Message
        else:
                print("\n") #Print New Lin
        if(userInput == 1): #This Option Will ADD Student
                StudentName =input("Enter student's name:")
                GuardianName=input("Enter guardian's name:")
                DOB=input("Enter DOB:")
                Class = input("Enter Class:")
                Sec = input("Enter Section:")
                # math_marks = input("Enter Math Marks:")
                addStudent ( StudentName , GuardianName , DOB)
                print("Record has been written to file")
        elif(userInput == 2): #This Option Will view Students
                # SELECT * FROM `adminStudent`
                viewStudents()

        elif(userInput == 3): #This Option Will Add Marks
                addMarks()
        else:
                print("\nHey! That's Not A Valid Option")

