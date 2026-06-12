"""Exercise 9. Vowel Frequency Counter
Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters."""

"Attempt 1"

sentance = input("Write a sentance:")

#We use this variable to act as a counter for each vowel in the string
num_vowel = 0 

for i in len(sentance): #This does not work as len(sentance) is a numerical value, which you cant loop through
    if i == "a", "e", "i", "o", "u":#Incorrect syntax
        num_vowel += 1
    return num_vowel #No function used so the return function cannot produce an output

"Attempt 2"

sentance = input("Write a sentance:")

num_vowel = 0

for i in sentance:
    if i in "aeiou":
        num_vowel += 1
print("There are", num_vowel, "vowels in this sentance" )

"Test:"

#The program fails to count capital letters, thus we must convery each character in the string into lowercase letters 
    
"Attempt 3"

sentance = input("Write a sentance:")

num_vowel = 0

#Converts all capitals into lowercase using .lower
for i in sentance.lower():
    if i in "aeiou":
        num_vowel += 1
print("There are", num_vowel, "vowels in this sentance" )
