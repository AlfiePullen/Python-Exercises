"Exercise 7. List Manipulation: Add and Remove"
"Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1)."
"Exercise Purpose: This exercise teaches “Dynamic Collection Management.” Lists are rarely static; being able to modify, expand, and prune them is essential for handling data like shopping carts, user lists, or inventory systems."
        
"Attempt 1"

fruits = ["apple", "banana", "orange", "strawberry", "papaya"]

# Take new fruit from the user
new_fruit = input("Add new fruit:")

#Add the new fruit into the list
fruits.append(new_fruit)

# Remove the second fruit (index 1)
fruits.pop(1)

# Show final list
print(fruits)
