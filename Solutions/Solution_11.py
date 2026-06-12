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
