def are_anagrams(str1, str2):
    normalized_str1 = ''.join(sorted(filter(str.isalnum, str1.lower())))
    normalized_str2 = ''.join(sorted(filter(str.isalnum, str2.lower())))


    return normalized_str1 == normalized_str2

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Anagram Checker Examples ---")

    # Example 1: Basic anagrams
    s1_a = "listen"
    s2_a = "silent"
    print(f"'{s1_a}' and '{s2_a}' are anagrams: {are_anagrams(s1_a, s2_a)}") # Expected: True
