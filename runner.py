import mysql.connector 
import admin , teacher , pdf_generator 
import os , platform

usr = input("Enter mySQL Username: ") #Taking Username From User
pwd =  input("Enter mySQL  Password: ")

mydb = mysql.connector.connect(host="localhost", user=usr , password = pwd)
cursor = mydb.cursor()
with open("new.txt") as file:
    for line in file.readlines():
        cursor.execute(line)

def startProgram():
    print(""" 

    ------------------------------------------------------
    |======================================================| 
    |======== Welcome To Student Management System ==========|
    |======================================================|
    ------------------------------------------------------

    Enter 1 : Run as admin
    Enter 2 : Run as teacher
    Enter 3 : Print results  
                    """)

    try: #Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
            print("\nHey! That's Not A Valid Number") #Error Message
    else:
            print("\n") #Print New Line

    if userInput == 1:
        admin.runAdmin()

    elif userInput == 2:
        Class = input("Enter Class: ")
        Sec = input("Enter Section: ")
        ClassSec = Class + Sec
        teacher.runTeacher(ClassSec)


    elif userInput == 3:
        classSec = input("Enter Class and Section: ")
        os.mkdir(classSec)
        # change cwd to the new directory made in previous line
        cwd = os.getcwd()
        os.chdir(cwd + "/" + classSec)
        class_strength = int(input("Enter total number of students in class: "))
        cursor.execute("SELECT * FROM student_{classSec} LEFT JOIN exam_{classSec} ON exam_{classSec}.roll_no = student_{classSec}.roll_no;".format(classSec = classSec))
        rows = cursor.fetchall()
        
        os.chdir(cwd)
        print("\nPDF Generated Successfully")
        print("\n")
        startProgram()
        for result in rows:
            pdf_generator.delete_file(result)
            pdf_generator.runPDF(result)

    def runAgain(): 
        runAgn = input("\nwant To Run Again Y/n: ")
        if(runAgn.lower() == 'y'):
                if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
                        print(os.system('cls')) 
                else:
                        print(os.system('clear'))
                startProgram()
                runAgain()
        else:
                print("Program is shutting down") 

    runAgain()      

startProgram()