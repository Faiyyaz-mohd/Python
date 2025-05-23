from collections import Counter

def character_frequency(string):
    # Remove spaces from the string
    string = string.replace(" ", "")
    # Count the frequency of each character
    frequencies = Counter(string)
    return frequencies

# Input string from the user
input_string = input("Enter a string: ")

# Calculate character frequencies
frequencies = character_frequency(input_string)

# Display the results
print("Character frequencies:")
for char, count in frequencies.items():
    print(f"{char}: {count}")
