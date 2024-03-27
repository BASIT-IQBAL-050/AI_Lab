def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Create arrays to store character counts
    count1 = [0] * 256  # Assuming ASCII characters
    count2 = [0] * 256

    # Increment count for each character in str1
    for char in str1:
        count1[ord(char)] += 1

    # Increment count for each character in str2
    for char in str2:
        count2[ord(char)] += 1

    # Compare character counts
    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True

# Test the function
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True
