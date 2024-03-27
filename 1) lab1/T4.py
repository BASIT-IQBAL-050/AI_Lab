string = input("Enter the String: ")
delete = int(input("Enter the number of characters you want to delete: "))

# Option 1: Print without removing from original string
print("Approach no 01:")
print(string[delete:])

# Option 2: Create a new string with characters removed
print("\nApproach No 02:")
new_string = string[delete:]
print(new_string)

# Option 3: Reassign string with removed characters (if desired)
print("\nApproach No 03:")
string = string[delete:]  # Reassigning to modify the original string
print(string)
