"Exercise 4: Remove first n characters from a string"
"Write a Python code to remove characters from a string from 0 to n and return a new string."

"----------------------------------------------------------------------------------------------------"
#Given Code
#def remove_chars(word, n):

#print("Removing characters from a string")
#print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

#print(remove_chars("pynative", 2)) 
# output 'native' 
"----------------------------------------------------------------------------------------------------"

#Attempt 1 

def remove_chars(word,n):
    print('Original string:', word)
    print("Now removing the first", n, "characters from the given string")
    x = word[n:]
    return x

print( remove_chars("Amalie", 3))

#Attempt 2.1: using this with inputs

word = input("Input a string:")
n = input("Input the amount of charachters you would like to remove from your string:")
def remove_chars2(word,n):
    print('Original string:', word)
    print("Now removing the first", n, "characters from the given string")
    x = word[n:]
    return x
print(x)

#Attempt 2.2:
word = input("Input a string: ")
n = int(input("Input the number of characters you would like to remove from your string: "))

def remove_chars2(word, n):
    print('Original string:', word)
    
    print("Now removing the first", n, "character(s) from the given string")
    x = word[n:]
    return x

result = remove_chars2(word, n)

print("Modified string:", result)
