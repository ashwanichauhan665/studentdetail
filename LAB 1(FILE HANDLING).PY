                                               #ASSIGNMENT-1

#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # 'end' argument prevents adding an extra newline
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

read_file_line_by_line("ABC.txt")

#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
def count_words_in_file(filename):
    try:
        word_count = 0
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split line into words based on whitespace
                word_count += len(words)
        print(f"Total number of words in {filename}: {word_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

count_words_in_file("ABC.txt")

#3. Write a function in Python to count uppercase character in a text file “ABC.txt”
def count_uppercase_characters(filename):
    try:
        uppercase_count = 0
        with open(filename, 'r') as file:
            for line in file:
                uppercase_count += sum(1 for char in line if char.isupper())
        print(f"Total number of uppercase characters in {filename}: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

count_uppercase_characters("ABC.txt")



#4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

Content="my name is TAMANNA .i persuing btech"
with open("story.txt", "w") as file:
    file.write(Content)

def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

display_words("story.txt")
