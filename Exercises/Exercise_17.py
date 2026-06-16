"""Exercise 17. Merging Lists with Parity Filtering
Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list."""

"Attempt 1"

def list_merge(List_1, List_2):
    
    list_merged = [] #Creating an empty list to insert the merged results
    
    #List_1 we want all the odd numbers
    for i in List_1:
        if i % 2 == 1:
            list_merged.append(i) #filter out the odd numbers from list_1 and add them into the empty merged list 
            
    #Now we want all the even numbers from list_2
    for j in List_2:
        if j % 2 == 0 :
            list_merged.append(j)
            
    print(list_merged)
