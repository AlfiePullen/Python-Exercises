#Ex_03
#Practice Problem: Display only those characters which are present at an even index number in given string.

#Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.

#Attempt 1:

def Ex_03(x):
    for i in range(1, len(x)): #The range starts at index 1 rather 0
        if i%2==0: #For all i in the range, if i modulo 2 is equal to 0, then this will return all characters at even indexes.
            return i
        
#Test

print(Ex_03("pineapple"))

#Output

#2

# return i exits the function immediately on the first match instead of processing the whole string.

#Attempt 2: 
    
def Ex_03(x):
    for i in range(len(x)): #len(x) of a string will start from the 0th index until the len(x)-1th index
        if i%2==0:
            print(x[i])
            
#Test

print(Ex_03("pineapple"))

#Return
#p
#n
#a
#p
#e
#None  #We want to avoid this output.

#Attempt 3:
    
def Ex_03(x):
    result = ""               # Create an empty string to store the
                              # characters found at even indexes.

    for i in range(len(x)):
        if i % 2 == 0:
            result += x[i]    # Add (concatenate) the character at
                              # index i to the end of the result string.

    return result             # Send the completed string back to
                              # wherever the function was called.
"---------------------------------------------------------------------------------------------------------------------------"
"Alternative Method"
"---------------------------------------------------------------------------------------------------------------------------"
# Practise using the Input function before attempt at code 
# take three values from user
name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)
"---------------------------------------------------------------------------------------------------------------------------"

#Attempt 1
word = input("Enter string: ")

size = len(word)
return size #This is where this code fails as we are using the return function in the wrong place 
                #The return function should be used when defining a function and in the place we are not creating a function
            
#Attempt 2 
word = input("Enter a word: ")    #this code successfully returns the length of the word we input

size = len(word)
print("length of word is:", size)

# Now we want to use a similar idea in the code above, to only return the characters of an even index. 
# In the above example this would be L,I

#Attempt 3
word = input("Enter a string:")
print("Original string", word)
size = len(word)
print("Printing only even index chars")

for i in range(0,size-1,2): #Iterating each letter and selecting each even index. This is done by selecting the first letter, and using a step of 2, so only go up in even intervals
    print("index[", i, "]", word[i])
print(Ex_03("Pineapple"))      # Print the value returned by the function.
               
