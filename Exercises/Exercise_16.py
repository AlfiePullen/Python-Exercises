"""Exercise 16. Numerical Palindrome Check
Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently."""

"Attempt 1"

number = int(input("Enter a number: "))

original = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10 #We use // which is integer division since we dont want to keep the remainder 

if original == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")
