import math #importing math library for round function

print("Enter the gross income")
grossincome = float(input())
grossrounded = round(grossincome)#rounds the gross income to nearest integer

print("Enter the number of dependents")
dependents = int(input())

taxableincome = grossrounded - 10000 - (3000 * dependents)
tax = taxableincome * 20/100 

print("Income Tax is %i." %tax)
print(grossrounded)
