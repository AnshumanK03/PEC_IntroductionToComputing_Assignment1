import math  #importing math library for round function
standeduction = 10000   #Value of standard deduction in dollars
dependentdeduc = 3000   #Value of dependent deduction in dollars

print("Enter the gross income")
grossincome = float(input())
grossrounded = round(grossincome)  #rounds the gross income to nearest integer

print("Enter the number of dependents")
dependents = int(input())

taxableincome = grossrounded - standeduction - (dependentdeduc * dependents) #Calculatng the taxable income
tax = taxableincome * 20/100 

if tax>0 :
 print("Income Tax is $%i." %tax)
else:
  tax=0
  print("Income Tax exempted, Tax is $0")
