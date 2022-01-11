i=0
marks=[]  #Creating a list for marks
student[] #for displaying names of students
while(i<5): #Loop for entering marks input by the user
 
 print("Enter the marks of student %i." %(i+1))
 a=int(input())
 marks.append(a)#Function to add marks of students in the list
 i=i+1 

#Algorithm for sorting
k=0
while(k<5):
 j=0;
 while(j<5):
  while(marks[j]>marks[k]):
   a=marks[j]
   b=marks[k]
   marks[j]=b
   marks[k]=a
  j=j+1
 k=k+1 
 
print(marks)

