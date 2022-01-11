#Program to show SID, name,Gender,Course,CGPA all in one list

print("Enter the student ID")
sid = int(input())

print("Enter the Student Name")
name = str(input())

print("Enter Gender 'F' for female , 'M' for male,  'U' for unknown")
gen=str(input())

print("Enter Course Name")
course = str(input())

print("Enter CGPA")
cgpa = float(input())

student = [sid,name,gen,course,cgpa]
print (student)
