#Python Assignment


#Question1
#Program to take the average of 3 numbers given by the user
i=0 #Counter Variable for taking Numbers from user
sum=0 #Variable for counting the sum of the Numbers Entered By User
while(i<3):
 print("Input Number %i." %(i+1))#Gives the command to user for input Number each time loop is run
 a=int(input())
 sum=sum+a
 i=i+1#increment

avg = sum/3.00
print("The average of above 3 numbers is %f." %avg)



#Question2
#Program to take gross income and number of dependents from the user and calculate the income tax
import math #importing math library for round function
standeduction = 10000 #Value of standard deduction in dollars
dependentdeduc = 3000 #Value of dependent deduction in dollars

print("Enter the gross income")
grossincome = float(input())  #Gross income in dollars
grossrounded = round(grossincome)#rounds the gross income to nearest integer

print("Enter the number of dependents")
dependents = int(input())

taxableincome = grossrounded - standeduction - (dependentdeduc * dependents)
tax = taxableincome * 20/100 

if(tax>0):
 print("Income Tax is $%i." %tax)
else:
 tax=0
 print("Tax Exempted ,Income tax is $0")



#Question3
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




#Question4
#Program to sort the marks of 5 different students
i=0
marks=[] #creating the list of student marks

while(i<5):
 print("Enter the marks of student %i." %(i+1))
 a=int(input())
 marks.append(a) #For adding marks of respective students to the list as the loop goes on
 i=i+1 
 
marks.sort() #For Sorting the marks list
print(marks)




#Question5a
#Program to display the list after removing black element 
print("The Initial list is")
color = ["Red","Green","White","Black","Pink","Yellow"] #Creating list
print(color)
print("The final list after removing element Black From the above list is ")
color.remove("Black")   #Removing element black from the list
print(color)            #printing final list




#Question5b
#Program to replace black and pink in the list with purple
color = ["Red","Green","White","Black","Pink","Yellow"]    #Initial list
print("The Initial list is")
print(color)
color[4]="Purple" ; color.remove("Black")  #Replacing pink with purple and removing black
print("The final list after replacing black and pink with purple is")
print(color)         #Printing final list

