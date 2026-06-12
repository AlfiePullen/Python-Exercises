"Exercise 6. Calculating Factorial with a Loop"
"Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop."
"Exercise Purpose: This exercise explores “Mathematical Accumulation.” A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing."

"Attempt 1"

def factorial(n):
    result = 1 #Define the variable to begin the loop. 
               #We choose 1 as the value as multiplying by 0 will not calculate
    while n>0: #Loop proceeds until n=1
        result = result * n #multiply the variabel by each n in the loop
        n=n-1 #For each n, we go to the next result down
    return result

print( factorial(0))
