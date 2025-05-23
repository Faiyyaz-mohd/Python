from collections import Counter

def word_frequency(paragraph):
    # Normalize the paragraph by converting to lowercase and removing punctuation
    words = paragraph.lower().split()
    # Count the frequency of each word
    frequencies = Counter(words)
    return frequencies

# Input paragraph from the user
paragraph = input("Enter a paragraph: ")

# Calculate word frequencies
frequencies = word_frequency(paragraph)

# Display the results
print("Word frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
