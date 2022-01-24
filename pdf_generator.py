
from reportlab.pdfgen import canvas
import os
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph , Frame , Table , TableStyle



school = 'ABC Public School'
school_data = ['Affiliated to CBSE',
               'Near Science Centre , Rajnagar , Raichok - 12'  ]


def runPDF(roll_no):
    c = canvas.Canvas("{}.pdf".format(roll_no),bottomup=0)
    def drawSchoolData():
        c.setFont("Helvetica", 24)
        # c.drawString(200, 790, "{}".format(school))
        c.drawString(200, 50, "{}".format(school))
        c.setFont("Helvetica", 12)
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.alignment = 1
        story1 = []
        for i in range(len(school_data)):
            lineText = school_data[i]
            P = Paragraph(lineText, style)
            story1.append(P)
        f1 = Frame(20, 55, 550, 50, leftPadding=3, bottomPadding=2, rightPadding=3, topPadding=2,showBoundary=0)
        f1.addFromList(story1, c)

    def drawStudentData():
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        student_name = Paragraph('Student Name : Sachin Kumar', style)
        parent_name = Paragraph('Parent Name : Raju Kumar', style)
        class_sec = Paragraph('Class : 10-C', style)
        roll_no = Paragraph('Roll No : 1', style)
        promotion = Paragraph('Promotion : No', style)
        class_teacher = Paragraph('Class Teacher : Mr. Suresh Sharma', style)
        table_data = [
            [student_name, parent_name],
            [class_sec, roll_no],
            [promotion, class_teacher]
        ]
        table_data.reverse()
        t_style = TableStyle([('BOX',(0,0),(-1,-1),2,colors.black),
                              ('INNERGRID', (0,0), (-1,-1), 0.50, colors.indigo),
                              ('VALIGN',(0,0),(-1,-1),'MIDDLE')])
        table = Table(table_data, colWidths=[255, 255] , rowHeights=[50,50,50] ,  style=t_style)
        story = [table]
        f2 = Frame(20, 125, 550, 175, leftPadding=1, bottomPadding=2, rightPadding=1, topPadding=2,showBoundary=0)
        c.setStrokeColorRGB( 255, 0, 0)
        f2.addFromList(story, c)
    
    def drawMarksData():
        styleSheet = getSampleStyleSheet()
        style = styleSheet['BodyText']
        style.alignment = 1
        sub1 = Paragraph('Subject 1', style)
        sub1_mark = Paragraph('70', style)
        sub1_highest = Paragraph('100', style)
        sub2 = Paragraph('Subject 2', style)
        sub2_mark = Paragraph('80', style)
        sub2_highest = Paragraph('100', style)
        sub3 = Paragraph('Subject 3', style)
        sub3_mark = Paragraph('90', style)
        sub3_highest = Paragraph('100', style)
        table_data = [
            [Paragraph('',style), Paragraph('Marks Obtained',style), Paragraph('Highest Marks',style)],
            [sub1, sub1_mark, sub1_highest],
            [sub2, sub2_mark, sub2_highest],
            [sub3, sub3_mark, sub3_highest]
        ]
        table_data.reverse()
        t_style = TableStyle([('BOX',(0,0),(-1,-1),2,colors.black),
                            ('INNERGRID', (0,0), (-1,-1), 0.50, colors.indigo),
                            ('VALIGN',(0,0),(-1,-1),'MIDDLE')])
        table = Table(table_data ,colWidths=[170,170,170] , rowHeights=[100,100,100,100] ,   style=t_style)
    
        story = [table]
        f3 = Frame(20, 325, 550, 420, leftPadding=1, bottomPadding=2, rightPadding=1, topPadding=2,showBoundary=0)
        f3.addFromList(story, c)

    def drawMargin():
        c.setStrokeColorRGB(0, 0, 250)
        c.setLineWidth(2)
        c.roundRect(20, 20, 550, 770, 15)
    drawMargin()
    drawSchoolData()
    drawStudentData()
    drawMarksData()
    print("success")
    c.showPage()
    c.save()

def delete_file(roll_no):
    try:
        os.remove("{}".format(roll_no))
    except OSError:
        pass

# delete_file(1)
# runPDF(1)

