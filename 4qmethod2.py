i=0
marks=[] #creating the list of student marks

while(i<5):
 print("Enter the marks of student %i." %(i+1))
 a=int(input())
 marks.append(a) #For adding marks of respective students to the list as the loop goes on
 i=i+1 
 
marks.sort() #For Sorting the marks list
print(marks)

