i=0 #Counter Variable for taking Numbers from user
sum=0 #Variable for counting the sum of the Numbers Entered By User
while(i<3):
 print("Input Number %i." %(i+1))#Gives the command to user for input Number each time loop is run
 a=int(input())
 sum=sum+a
 i=i+1#increment

avg = sum/3.00
print("The average of above 3 numbers is %f." %avg)
