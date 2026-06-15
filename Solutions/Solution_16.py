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
