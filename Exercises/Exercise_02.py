#Ex_02
# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

#Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

#Attempt 1: 

for i in range(1,10):
    print("Current Number:", i, "Previous Number:", i-1, "Sum:", i+i-1)
    
#The above code is incomplete because we have not defined the 0th index. This will cause errors in larger projects as when we enlarge sample sizes, calculations may be thrown off.  
    
#Attempt 2:

for i in range(1,10):
    previous_number = 0
    print("Current Number:", i, "Previous Number:", i-1, "Sum:", i+i-1)
    previous_number = i 
