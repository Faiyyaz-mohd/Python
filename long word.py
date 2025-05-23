def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Find the longest word
    longest_word = max(words, key=len)
    return longest_word

# Input sentence from the user
sentence = input("Enter a sentence: ")

# Find and print the longest word
longest_word = find_longest_word(sentence)
print(f"The longest word is: {longest_word}")
