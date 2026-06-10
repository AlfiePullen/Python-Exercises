# Exercise 1 

# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

#Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

#Attempt 1

def ex_01(x,y):
    if x*y <= 1000:
        return x*y
    else:
        return x+y

#Test (a)

print(ex_01(20, 30))
print(ex_01(45,57))
print(ex_01(500, 2)) #Testing the extreme cases: if x*y = 1000, it returns the product. 
print(ex_01(1001, 1)) #Similarly, if x*y > 1000, the function returns the sum.
