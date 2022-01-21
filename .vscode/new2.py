# Importing
from getpass import getpass
from mysql.connector import connect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import texttable

#################################
#Defining/Assigning

create_db_query = """CREATE DATABASE IF NOT EXISTS ip_project;"""

use_db_query = "USE ip_project;"

crt_examtbl_query = """CREATE TABLE IF NOT EXISTS `exam` (
  `sub_code` varchar(3) NOT NULL,
  `roll_no` int NOT NULL,
  `marks` int DEFAULT NULL,
  `test` varchar(3) NOT NULL
);"""

crt_stutbl_query = """CREATE TABLE IF NOT EXISTS `student` (
  `roll_no` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `stream` varchar(5) NOT NULL,
  PRIMARY KEY (`roll_no`)
);"""

crt_subtbl_query = """CREATE TABLE IF NOT EXISTS `subject` (
  `sub_code` varchar(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`sub_code`)
);
"""

tbl_structure = '''You can now see the table structures to get a better idea:
 
'exam' table:
============
+----------+------------+------+-----+---------+-------+
| Field    | Type       | Null | Key | Default | Extra |
+----------+------------+------+-----+---------+-------+
| sub_code | varchar(3) | NO   |     | NULL    |       |
| roll_no  | int        | NO   |     | NULL    |       |
| marks    | int        | YES  |     | NULL    |       |
| test     | varchar(3) | NO   |     | NULL    |       |
+----------+------------+------+-----+---------+-------+

'student' table:
===============
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| roll_no | int         | NO   | PRI | NULL    |       |
| name    | varchar(20) | NO   |     | NULL    |       |
| stream  | varchar(5)  | NO   |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

'subject' table:
===============
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| sub_code | varchar(3)  | NO   | PRI | NULL    |       |
| name     | varchar(30) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
'''

insert_stu_query = '''INSERT INTO student(roll_no, name, stream) VALUES(%s, %s, %s);'''

stream_human_lst = '''
1. MPC
2. BiPC
3. MEC
4. CEIP
'''
stream_list = ["MPC","BiPC","MEC","CEIP"]

stream_inp_stat = "Choose one of the these streams (by typing the number): "

select_stu_query = "SELECT * FROM student;"

insert_sub_query = '''INSERT INTO subject
VALUES
("301","English"),
("041","Maths"),
("042","Physics"),
("043","Chemistry"),
("065","Informatics Practices"),
("055","Accountancy"),
("030","Economics"),
("054","Business Studies"),
("044","Biology");
'''

select_sub_query = "SELECT * FROM subject;"

exam_tbl = "We request you to insert data in 'exam' table using MySQL."

#######################################################################

menu = '''Choose one of the options by typing the number:
1. See the marks of the student
2. See the total marks and percentage of each test of the student
3. See graphs/charts made using the marks of the student
'''

Q1 = "SELECT * FROM student;"

marks_query = """
              SELECT
                exam.test Test,
                exam.sub_code 'Code',
                subject.name Subject,
                exam.marks Marks
              FROM exam
              LEFT JOIN subject ON exam.sub_code = subject.sub_code
              WHERE roll_no=%s
              ORDER BY exam.test,exam.sub_code ASC;
              """

total_query = '''
SELECT test Test, SUM(marks) Total, SUM(marks)/250*100 "Percentage (%)"
FROM exam
WHERE roll_no=%s
GROUP BY test
ORDER BY test ASC;
'''

plot_menu = '''Choose one of the options by typing the number:
1. Bar graph
2. Line graph
'''

mpc_query = '''SELECT * FROM student WHERE stream="MPC";'''

bipc_query = '''SELECT * FROM student WHERE stream="BiPC";'''

mec_query = '''SELECT * FROM student WHERE stream="MEC";'''

ceip_query = '''SELECT * FROM student WHERE stream="CEIP";'''

bar_query = """
            SELECT exam.test, exam.sub_code, subject.name, exam.marks
            FROM exam
            LEFT JOIN subject ON exam.sub_code = subject.sub_code
            WHERE exam.roll_no=%s
            ORDER BY exam.test,exam.sub_code ASC;
            """
line_query = """
            SELECT exam.test, exam.sub_code, subject.name, exam.marks
            FROM exam
            LEFT JOIN subject ON exam.sub_code = subject.sub_code
            WHERE exam.roll_no=%s
            ORDER BY exam.sub_code,exam.test ASC;
            """
            
uni_subnames = """
              SELECT DISTINCT subject.name
              FROM exam
              LEFT JOIN subject ON exam.sub_code = subject.sub_code
              WHERE exam.roll_no=%s
              ORDER BY exam.sub_code,exam.test ASC;
              """

########################################################################

# Welcoming user
print("Hello! Welcome to the report card management software.")
print()
print("""Do you have a MySQL database which has the marks data of students?
       
Press y or n.""")

print()
database_inp = input()
print()

if database_inp == "n":
    print()
    print("OK. Let's create a database for you.")
    print()
    print("Firstly, let's connect to MySQL.")
    db_cnnt = connect(
                  host="localhost",
                  user=input("Enter username: "),
                  password=getpass("Enter password: "))

    #Cursor
    db_cursor = db_cnnt.cursor()
    
    db_cursor.execute(create_db_query)
    
    print()
    print("We have created a database named 'ip_project' for you.")
    print()
    
    db_cursor.execute(use_db_query)
    
    db_cursor.execute(crt_examtbl_query)
    db_cursor.execute(crt_stutbl_query)
    db_cursor.execute(crt_subtbl_query)
    
    print("We have also created three tables for you. The tables are 'exam', 'student' and 'subject'.")
    print()
    print(tbl_structure)
    print()
    print("Now let's insert data in 'student' table.")
    stu_no = int(input("How many rows do you want to add in student table (type number)? "))
    main_l = []

    for i in range(stu_no):
        c1 = int(input("Enter roll number of the student: "))
        c2 = input("Enter name of the student: ")
        print(stream_inp_stat, stream_human_lst)
        print("For example: Type 1 for MPC.")
        print()
        stream_choice = int(input())

        if stream_choice == 1:
            c3 = stream_list[0]
        elif stream_choice == 2:
            c3 = stream_list[1]
        elif stream_choice == 3:
            c3 = stream_list[2]
        elif stream_choice == 4:
            c3 = stream_list[3]
        
        l1 = [c1,c2,c3]
        t1 = tuple(l1)

        main_l.append(t1)
    
    db_cursor.executemany(insert_stu_query,main_l)
    db_cnnt.commit()
    
    print()
    db_cursor.execute(select_stu_query)
    stu_sql_tbl = pd.DataFrame(db_cursor.fetchall(),
                        columns=[item[0] for item in db_cursor.description])
    print("This is the 'student' table:")
    print()
    print(stu_sql_tbl.to_markdown(index = False, tablefmt="grid"))
    
    db_cursor.execute(insert_sub_query)
    db_cnnt.commit()
    
    db_cursor.execute(select_sub_query)
    sub_sql_tbl = pd.DataFrame(db_cursor.fetchall(),
                        columns=[item[0] for item in db_cursor.description])
    print()
    print("We have inserted the data in 'subject' table. This is the subject table:")
    print()
    print(sub_sql_tbl.to_markdown(index = False, tablefmt="grid"))
    
    print()
    print(exam_tbl)
    print("After inserting data in 'exam' table through MySQL, you can see other things like total and graphs in this program.")
    
    db_cursor.close()
    db_cnnt.close()

elif database_inp == "y":
    print("Let's connect to the MySQL database!")
    db_cnnt = connect(
                  host="localhost",
                  user=input("Enter username: "),
                  password=getpass("Enter password: "),
                  database="ip_project")

    #print(db_cnnt)

    #Cursor
    db_cursor = db_cnnt.cursor()

    #Getting basic details of all students
    db_cursor.execute(Q1)
    
    stu_table = pd.DataFrame(db_cursor.fetchall(),
                             columns=[item[0] for item in db_cursor.description],
                             index = range(1,21))
    #Taking input
    while True:
        try:
            inp = int(input("Please type the roll number of the student whose details you would like to see: "))
        except ValueError:
            print("Please type a valid input.")
            continue
        else:
            break

    print()
    print(menu)
    menu_inp = int(input())
    
    if menu_inp == 1:
    
        print()   
        db_cursor.execute(marks_query, (inp,))
    
        marks_df = pd.DataFrame(db_cursor.fetchall(),
                                columns=[item[0] for item in db_cursor.description])
        marks_df1 = marks_df
        marks_df1.loc[marks_df1['Test'].duplicated(), 'Test'] = ''

        if marks_df1["Marks"].isnull().values.any() == True:
            marks_df1["Marks"] = marks_df1["Marks"].fillna("Absent")

        marks_col = marks_df1.columns
        marks_val = marks_df1.values.tolist()

        tableObj = texttable.Texttable()
        tableObj.set_cols_align(["l", "l", "l", "r"])
        tableObj.set_cols_dtype(["t", "t", "t", "a"])
        tableObj.set_cols_valign(["m", "m", "m", "m"])

        tableObj.header(marks_col)
        tableObj.add_rows(marks_val,header=False)

        print("Name of student:", stu_table.loc[inp,"name"])
        print("Grade: XII")
        print("Stream:", stu_table.loc[inp,"stream"])
        print()
        print(tableObj.draw())
        print()


    ##############################################################################
    
    elif menu_inp==2:
        db_cursor.execute(total_query, (inp,))
    
        total_df = pd.DataFrame(db_cursor.fetchall(),
                                columns=[item[0] for item in db_cursor.description])
        total_col = total_df.columns
        total_val = total_df.values.tolist()
    
        tableObj = texttable.Texttable()
        tableObj.set_cols_align(["l", "l", "l"])
        tableObj.set_cols_dtype(["t", "i", "f"])
        tableObj.set_cols_valign(["l", "m", "m"])
    
        tableObj.header(total_col)
        tableObj.add_rows(total_val,header=False)
        print(tableObj.draw())

    ####################################################### 
    
    elif menu_inp==3:
        print(plot_menu)
        plot_menu_inp = int(input())
        
        if plot_menu_inp == 1:
            db_cursor.execute(bar_query, (inp,))
        
            bar_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
        
            #print(bar_df)
        
            ########################################################
        
            m1_values = bar_df.loc[0:4, 'marks'].to_list()
            m2_values = bar_df.loc[5:9, 'marks'].to_list()
            m3_values = bar_df.loc[10:14, 'marks'].to_list()
            sub_list = bar_df.loc[0:4, 'name'].to_list()
        
            #########################################################
            
            db_cursor.execute(mpc_query)
            mpc_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
            mpc_list = mpc_df.roll_no.to_list()
        
            db_cursor.execute(bipc_query)
            bipc_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
            bipc_list = bipc_df.roll_no.to_list()
        
            db_cursor.execute(mec_query)
            mec_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
            mec_list = mec_df.roll_no.to_list()
        
            db_cursor.execute(ceip_query)
            ceip_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
            ceip_list = ceip_df.roll_no.to_list()
        
        
            if inp in mpc_list or inp in bipc_list:
                sub_list[3]="IP"
            elif inp in mec_list:
                sub_list[2]="B.St."
                sub_list[3]="Acct."
            elif inp in ceip_list:
                sub_list[1]="B.St."  
                sub_list[2]="Acct."
                sub_list[3]="IP"
        
            #print(sub_list)
            #########################################################

            N = len(sub_list)
            ind = np.arange(N) 
            width = 0.25
        
            plt.grid(axis='y', zorder=0)
        
            plt.bar(ind, m1_values, width, label="MT1", color='xkcd:pink', zorder=3)
            plt.bar(ind+width, m2_values, width, label="MT2", color='xkcd:light blue', zorder=3)
            plt.bar(ind+width*2, m3_values, width, label="MT3", color='xkcd:mint', zorder=3)
        
            plt.xticks(ind+width,sub_list)
            plt.yticks(np.arange(0, 51, 5))
        
            plt.legend(loc=(1.05, 0.5))
            plt.tight_layout()
            plt.show() 
    
        #####################################################################
        elif plot_menu_inp == 2:
            db_cursor.execute(line_query, (inp,))
        
            line_df = pd.DataFrame(db_cursor.fetchall(),
                                  columns=[item[0] for item in db_cursor.description])
        
            #print(line_df)
        
            db_cursor.execute(uni_subnames, (inp,))
        
            uni_subnames_df = pd.DataFrame(db_cursor.fetchall(),
                                           columns=[item[0] for item in db_cursor.description])
        
            #print(uni_subnames_df)
        
            uni_sub_list = uni_subnames_df.name.to_list()
        
            mt_list = ["MT1","MT2","MT3"]
        
            ########################################################
        
            sub1_marks = line_df.loc[0:2, 'marks'].to_list()
            sub2_marks = line_df.loc[3:5, 'marks'].to_list()
            sub3_marks = line_df.loc[6:8, 'marks'].to_list()
            sub4_marks = line_df.loc[9:11, 'marks'].to_list()
            sub5_marks = line_df.loc[12:14, 'marks'].to_list()
        
            plt.grid()
            plt.plot(sub1_marks, label=uni_sub_list[0], marker="s")
            plt.plot(sub2_marks, label=uni_sub_list[1], marker="s")
            plt.plot(sub3_marks, label=uni_sub_list[2], marker="s")
            plt.plot(sub4_marks, label=uni_sub_list[3], marker="s")
            plt.plot(sub5_marks, label=uni_sub_list[4], marker="s")
        
            plt.xticks(np.arange(0,3),mt_list)
            plt.legend(loc=(1.05, 0.5))
            plt.xlabel(r"Monthly Test $\rightarrow$")
            plt.ylabel(r"Marks $\rightarrow$")
            plt.tight_layout()
            plt.show()

    #######################################################

    db_cursor.close()
    db_cnnt.close()

input("Program complete. Press any key to exit.")