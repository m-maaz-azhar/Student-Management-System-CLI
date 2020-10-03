import csv
from tabulate import tabulate
studentsList = []
with open("file.csv","r",newline="") as dataFile:
    reader = csv.reader(dataFile)
    for row in reader:
        studentsList.append(row)
print('''
========================================================
                Student Management System
========================================================
''')
print('''
╒═══════════════════════════════════════╕
            INSTRUCTIONS
╘═══════════════════════════════════════╛
-------------------------------------------

    |  Press 1 to Search Student     |
    |  Press 2 to Add Student        |
    |  Press 3 to Delete Student     |
    |  Press 4 to see Students List  |
    |  Press 5 to Exit               |

-------------------------------------------
''')
while True:
    action = input("Please Enter a Value to Perform an Action [1/5] : ")
    if action== "1":
        rollNum = input("Please Input Student Roll Number: ")
        for i in range(len(studentsList)):
            try:
                if studentsList[i][1] == rollNum:
                    print(''' 
                            ┏━  ============  ━┓
                                STUDENT DATA
                            ┗━  ============  ━┛
                    ''')
                    print('╒══════════════════╕')
                    print("   Name: " + studentsList[i][0])
                    print("   Roll No: " + studentsList[i][1])
                    print("   Age: " + studentsList[i][2])
                    print("   Class: " + studentsList[i][3])
                    print("   Section: " + studentsList[i][4])
                    print('╘══════════════════╛')
                    break
            except:
                    print('''
                             ╒════════════════════════════════╕
                              Please Enter a Valid Roll Number
                             ╘════════════════════════════════╛
                    ''')
    elif action == "2":
        student = []
        print('''       
                            ┏━  ================  ━┓
                                ADDING A STUDENT
                            ┗━  ================  ━┛
                        ''')
        student.append(input("Please Enter Student Name: "))
        student.append(input("Please Input Student Roll Number: "))
        student.append(input("Please Enter Student Age: "))
        student.append(input("Please Enter Student Class: "))
        student.append(input("Please Enter Student Section: "))
        studentsList.append(student)
        print('''
        ╒══════════════════════════╕
         Student Added Successfully
        ╘══════════════════════════╛
        ''')
    elif action == "3":
        rollNum = input("Please Input Student Roll Number: ")
        for i in range(len(studentsList)):
            if studentsList[i][1] == rollNum:
                del studentsList[i]
                print('''
                ╒════════════════════════════╕
                 Student Removed Successfully
                ╘════════════════════════════╛
                ''')
                break
    elif action == "4":
        print('''       
                        ┏━  ===============  ━┓
                             STUDENTS LIST
                        ┗━  ===============  ━┛
----------------------------------------------------------------
        ''')
        print(tabulate(studentsList, headers=['| Name |','| Roll No |','| Age |','| Class |','| Section |']))    
        print('''
----------------------------------------------------------------
        ''')
    elif action == "5":
        with open("file.csv","w",newline="") as dataFile:
            writer = csv.writer(dataFile,delimiter=",")
            for i in range(len(studentsList)):
                writer.writerow(studentsList[i])
        exit()
    else:
        print("Input a Valid Action Number")