"""Exercise 15. Nested Loops for Pattern Generation
Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.

Exercise Purpose: Pattern printing is a classic way to learn “Nested Loops.” You coordinate an outer loop for rows and an inner loop for columns or repetitions. This improves spatial logic and control over output formatting."""

"Attempt 1:"

for i in range(1,6):
    print(i, end="")
    
#Output:
    
#12345

#We need to print each i in the range on seperate lines
#We also need to print each i, i times.

"Attempt 2"

for i in range(1,6):
    for j in range(i):
        print(i, end=" ") # end=" " keeps it on the same line
    # New line after each row
    print("\n")
        
#NOTE: \n is the new line character
