sentance = input("Write a sentance:")

num_vowel = 0

#Converts all capitals into lowercase using .lower
for i in sentance.lower():
    if i in "aeiou":
        num_vowel += 1
print("There are", num_vowel, "vowels in this sentance" )
