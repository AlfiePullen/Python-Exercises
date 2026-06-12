"Exercise 8. String Reversal"
"Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”)."
"Exercise Purpose: This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences, and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 lines of code in other languages."

"Attempt 1"

string = input("Type a word:")

#Reversing the string using slicing. The [::-1] represents how many characters in the string to jump each time, thus using -1 as the jump makes the string start from the -1th index.
new_string = string[::-1]

print("original word:", string)
print("Reversed word:", new_string)
