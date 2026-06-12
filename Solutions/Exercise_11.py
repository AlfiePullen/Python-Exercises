"""Exercise 11. Removing Duplicates from a List
Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

Exercise Purpose: This exercise teaches “Data De-duplication.” In real-world data science, datasets are often “messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data."""
 
data = input("Input a list:") #Cannot use input as this converts the list into a string

# Set conversion removes duplicates automatically
unique_data = list(set(data))

print(f"Unique List: {unique_data}")

"Attempt 2"

# .split(",") converts the input string into a list using comma as the separator
data = input("Input a list (comma-separated): ").split(",")

# Create an empty list to store only unique items (no duplicates)
unique_data = []

# Loop through each item in the input list
for item in data:
    
    # Remove any extra spaces around the item (e.g. " apple" → "apple")
    item = item.strip()

    # Check if the item is NOT already in the unique list
    if item not in unique_data:
        
        # If it's not there, add it to the unique list
        unique_data.append(item)

# Print the final list with duplicates removed
print("Unique List:", unique_data)
