"""Exercise 13. Filtering Lists with Conditional Logic
Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

Exercise Purpose: This exercise teaches the use of the modulo operator (%) and loop filtering. In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria."""

"Attempt 1"

def list_filter(number_list):
    blank_list = [] #Blank list to add all the desired results
    for i in number_list:
        if i%5==0:#Using % we can find the remainder of a number
            blank_list.append(i)
    return blank_list
    
"Test"

#In [1]: list_filter([1,2,3,4,5,6,7,10,15])
#Out[1]: [5]
