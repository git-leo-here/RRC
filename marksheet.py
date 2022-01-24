rollno = int(input("enter roll number: "))
name = input("enter name: ")
standard = int(input("enter class: "))
english = int(input("enter english marks: "))
physics = int(input("enter physics marks: "))
chemistry = int(input("enter chemistry marks: "))
PED = int(input("enter ped marks: "))
computer = int(input("enter computer marks: "))
obtained_marks = english+ physics+ chemistry + PED +computer    #add subjects
percentage = (obtained_marks/500)*100

print("-------------STUDENT'S MARKSHEET----------------")
print("YOUR ROLL NUMBER IS: " + str(rollno))
print("YOUR NAME IS: " + name)  
print("YOUR CLASS IS: " + str(standard))
print("TOTAL MARKS ARE: 500 " )
print("obtained marks:"obtained_marks)
print("YOUR PERCENTAGE IS: " + str(percentage))

if percentage >= 80:
    print("GRADE: A-1")
elif percentage >= 70:
    print("GRADE: A")
elif percentage >= 60:
     print("GRADE: B")
elif percentage >= 50:
     print("GRADE: C")
elif percentage >= 30:
    print("GRADE: E")
else:
    print("Grade: FAIL")

i = 0
subjects_name = ""

if english < 30:
    i = i+1
    subjects_name += "English"
if physics < 30:
    i = i+1
    subjects_name += "Physics"
if chemistry < 30:
    i = i+1
    subjects_name += "Chemistry"
if computer < 30:
    i = i+1
    subjects_name += "Computer"
if PED < 30:
    i = i+1
    subjects_name += "PED"

print("Failed subjects count: " + str(i))    
    
    
     
    
