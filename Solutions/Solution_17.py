
def list_merge(List_1, List_2):
    
    list_merged = [] #Creating an empty list to insert the merged results
    
    #List_1 we want all the odd numbers
    for i in List_1:
        if i % 2 == 1:
            list_merged.append(i)
            
    #Now we want all the even numbers from list_2
    for j in List_2:
        if j % 2 == 0 :
            list_merged.append(j)
            
    print(list_merged)
