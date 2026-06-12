

fruits = ["apple", "banana", "orange", "strawberry", "papaya"]

# Take new fruit from the user
new_fruit = input("Add new fruit:")

#Add the new fruit into the list
fruits.append(new_fruit)

# Remove the second fruit (index 1)
fruits.pop(1)

# Show final list
print(fruits)
