def analyze_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    line_count = len(lines)
    word_count = 0
    char_count = 0
    
    for line in lines:
        word_count += len(line.split())
        char_count += len(line)
    
    print(f"Lines in the file: {line_count}")
    print(f"Total words found: {word_count}")
    print(f"Characters (including spaces): {char_count}")

if __name__ == "__main__":
    file_name = input("Enter the path to your text file: ")
    analyze_file(file_name)
