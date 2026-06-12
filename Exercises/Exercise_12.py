"""Exercise 12. List Comparison and Boolean Logic

Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks."""
 
def list_compare(number_list):
    print("Given list:", number_list)
    
    first_num = number_list[0]
    last_num = number_list[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
