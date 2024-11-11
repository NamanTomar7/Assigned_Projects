import pymysql
import random

# Establishing the Connection with DataBase
connection= pymysql.connect(host="localhost", user="root", password="Naman@123", database="college")
print(connection)
mycursor= connection.cursor()

# Create a new table in DataBase
# studentDetails="create table if not exists StudentDetails(StudentName text,FathersName text,RollNo int(11) NOT NULL AUTO_INCREMENT,Course text,Section text, Batch text, Email text, Address text,Attendance int,FeesPending int, PRIMARY KEY (RollNo))"
# mycursor.execute(studentDetails)
# connection.commit()

# Create a new column in Database
# mycursor.execute("ALTER TABLE StudentDetails ADD COLUMN StudentID int")
# mycursor.execute("ALTER TABLE StudentDetails ADD COLUMN Password VARCHAR(100)")

#Delete Column in DataBase
# dropCol = "ALTER TABLE StudentDetails DROP COLUMN FeesPending;"
# mycursor.execute(dropCol)
# connection.commit()

# #Drop table in Database
# droptask="drop table StudentDetails"
# mycursor.execute(droptask)
# connection.commit()

# Delete Row in database
# deleteTask="delete from studentDetails where RollNo= '1'"
# mycursor.execute(deleteTask)
# connection.commit()

# #Update the task in DataBase
# updateTask="Update studentDetails set Password='Naman@123' where RollNo='4'"
# mycursor.execute(updateTask)
# connection.commit()

global ChooseCourse
global totalFee
totalfee=0

def attendance():
    
    roll=int(input("Enter Your Roll number: "))
    showAttendance="SELECT Attendance FROM studentDetails WHERE RollNo ={}"
    mycursor.execute(showAttendance.format(roll))
    Result=mycursor.fetchone()
    
    try:
        Att=Result[0]
    except TypeError:
        print("Roll Number doesn't exist")  
        exit()

    Att=Result[0]
    connection.commit()
    showName="SELECT StudentName FROM studentDetails WHERE RollNo={}"
    mycursor.execute(showName.format(roll))
    Result1=mycursor.fetchone()
    Name=Result1[0]
    connection.commit()
    print("Name - ",Name,"\nAttendance-", Att,"%")
    

def addmission(total,Course):
    attendance= random.randint(65,100)
    uniqueID=random.randint(10000,20000)
    sec="B"
    batch="2023-26"
    Fee=int(input("Enter Fees amount to be deposited(50000 minimum Criteria): "))
    
    if Fee>total:
        print("\nThe Amount you want to Deposit is more than Required")
        exit()
    
    if Fee<=49999:
        print("\nMinimum Fee Criteria doesn't fullfil")
        exit()
    
    FeesPending=total-Fee
    InsertDetails="insert into studentDetails (StudentName, FathersName,Course,Section,Batch,Email,Address,Attendance,FeesPending,StudentID,Password) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(input("Enter Student name: "),input("Enter Father's Name: "),Course,sec,batch, input("Enter Email: "),input("Enter Address: "),attendance,FeesPending,uniqueID,input("Create Your Password: "))       
    mycursor.execute(InsertDetails)
    connection.commit()


def course():
    print("\t\t\t\t\tSelect course to get details:- \n")
    print("1.BCA\n2.BBA\n3.MBA\n4.MCA\n")
    ch2=int(input("-->"))

    if ch2==1:
        ChooseCourse="BCA"
        print(" Course Name - \tBCA\n Duration -\t3Years\n Fees -\t1.4L")
        totalFee=140000
        print("\nAre you interested to take addmission ?\nPress 1 if yes else any key if no:- \n")
        ch3=int(input("-->"))
        if ch3==1:
            addmission(totalFee,ChooseCourse)
        else:
            pass    
    elif ch2==2:
        ChooseCourse="BBA"
        print(" Course Name - \tBBA\n Duration -\t3Years\n Fees - \t80k")
        totalFee=80000
        print("\nAre you interested to take addmission ?\nPress 1 if yes else any key if no:- \n")
        ch3=int(input("-->"))
        if ch3==1:
            addmission(totalFee,ChooseCourse)
        else:
            pass
    elif ch2==3:
        ChooseCourse="MBA"
        print(" Course Name - \tMBA\n Duration -\t2Years\n Fees - \t1.3L")
        totalFee=130000
        print("\nAre you interested to take addmission ?\nPress 1 if yes else any key if no:- \n")
        ch3=int(input("-->"))
        if ch3==1:
            addmission(totalFee,ChooseCourse)
        else:
            pass
    elif ch2==4:
        ChooseCourse="MCA"
        print(" Course Name - \tMCA\n Duration -\t2Years\n Fees - \t1.5L")
        totalFee=150000
        print("\nAre you interested to take addmission ?\nPress 1 if yes else any key if no:- \n")
        ch3=int(input("-->"))
        if ch3==1:
            addmission(totalFee,ChooseCourse)
        else:
            pass
    else:
        print("Invalid Choice")
        pass

def SubmitFees():
    CheckRoll=int(input("Enter Your Roll Number: "))
    query = "SELECT FeesPending FROM studentdetails WHERE RollNo = %s"
    mycursor.execute(query, (CheckRoll))
    result = mycursor.fetchone()

    try:
        CurrentPending= result[0]
    except TypeError:
        print("\nEntered Roll Number doesn't exists")
        exit()
        
    CurrentPending= result[0]
    
    if CurrentPending==0:
        print("You don't have any Fee Pendning")
        SubmitFees()
    
    print("Your pending Fees Amount is ", CurrentPending)
    Amount=int(input("Enter the amount to deposit: "))
    
    if Amount>CurrentPending:
        print("\nAmount is larger than the Fee Pending")
        SubmitFees()
    
    UpdatedValue= CurrentPending-Amount
    update_query = "UPDATE studentdetails SET FeesPending = %s WHERE RollNo = %s"
    mycursor.execute(update_query, (UpdatedValue, CheckRoll))
    connection.commit()
    print("\t\tAmount of",Amount,"Deposited SuccesFully")

def login():
    
    CheckRoll=input("Enter Your Roll Number: ")
    query = "SELECT StudentID FROM studentdetails WHERE RollNo = %s"
    mycursor.execute(query, (CheckRoll))
    result = mycursor.fetchone()
    
    try:
        ID=result[0]
    except TypeError:
        print("\nEntered Roll Number Doesn't Exist")
        exit()    
    
    ID=result[0]
    print("Login ID - ",ID)
    CheckPass=input("Enter Your Password:")
    query2="SELECT Password FROM studentDetails WHERE RollNo=%s"
    mycursor.execute(query2,(CheckRoll))
    result1=mycursor.fetchone()
    Password=result1[0]
    
    if CheckPass==Password:
        print("\n\t\t\t\tLogin Succesfull")
        print("\n\t\t\tChoose the Column You want to make change in:- ")
        print("\n1. Student Name\n2. Father's Name\n3. Section\n4. Email\n5. Address\n")
        ch3=int(input("-->"))
        if ch3==1:
            UpdatedData=input("Enter Name to be updated: ")
            updateTask="Update studentDetails set StudentName=%s where RollNo=%s"
            mycursor.execute(updateTask,(UpdatedData,CheckRoll,))
            connection.commit()
        elif ch3==2:
            UpdatedData=input("Enter Father's Name to be updated: ")
            updateTask="Update studentDetails set FathersName=%s where RollNo=%s"
            mycursor.execute(updateTask,(UpdatedData,CheckRoll))
            connection.commit()
        elif ch3==3:
            UpdatedData=input("Enter Section to be Changed: ")
            updateTask="Update studentDetails set Section=%s where RollNo=%s"
            mycursor.execute(updateTask,(UpdatedData,CheckRoll))
            connection.commit()
        elif ch3==4:
            UpdatedData=input("Enter Email to be updated: ")
            updateTask="Update studentDetails set Email=%s where RollNo=%s"
            mycursor.execute(updateTask,(UpdatedData,CheckRoll))
            connection.commit()
        elif ch3==5:
            UpdatedData=input("Enter Address to be updated: ")
            updateTask="Update studentDetails set Address=%s where RollNo=%s"
            mycursor.execute(updateTask,(UpdatedData,CheckRoll))
            connection.commit()                                                            
        else:
            print("\nInvalid Choice")
            exit()
    else:
        print("\nPassword is Incorrect")
        pass            

def Home():
    
    while True:
        print("\t\t\t\t\tWelcome To ITS\n")
        print("\t\t\tChoose Operation to Perform:- \n")
        print("\t\t\t1. New Admission\n")
        print("\t\t\t2. View Course Details\n")
        print("\t\t\t3. Submit Fees\n")
        print("\t\t\t4. View Student Attendance\n")
        print("\t\t\t5. Update Student details(VIA student unique id login)\n")
        print("\t\t\t6. Exit\n")
        
        ch=int(input("\t\t\t-->"))

        if ch==1:
            print("\n\tChoose the course you want to take addmission in:- ")
            print("1.BCA\n2.BBA\n3.MBA\n4.MCA")
            course1=int(input("-->"))
            if course1==1:
                ChooseCourse="BCA"
                totalFee=140000
                print("Total Fess=", totalFee)
            elif course1==2:
                ChooseCourse="BBA"
                totalFee=80000
                print("Total Fees=", totalFee)
            elif course1==3:
                ChooseCourse="MBA"
                totalFee=130000
                print("Total Fees=", totalFee)
            elif course1==4:
                ChooseCourse="MCA"
                totalFee=150000
                print("Total Fees=", totalFee)
            else:
                print("\nInvalid Choice")
                break                
            addmission(totalFee,ChooseCourse)
        elif ch==2:
            course()
        elif ch==3:
            SubmitFees()
        elif ch==4:
            attendance()
        elif ch==5:
            login()    
        elif ch==6:
            mycursor.close()            
            break
        else:
            print("\nInvalid Choice")

Home()
