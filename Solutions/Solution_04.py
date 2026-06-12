def remove_chars(word,n):
    print('Original string:', word)
    print("Now removing the first", n, "characters from the given string")
    x = word[n:] #Start at index n and take every character from there to the end of the string.
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
