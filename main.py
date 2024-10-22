def read_books(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(book):
    book_words = book.split()
    return len(book_words)

def count_characters(book):
    book_lowercase = book.lower()
    character_count_dictionary = {}
    for character in book_lowercase:
        if character in character_count_dictionary:
            character_count_dictionary[character] += 1
        else: 
            character_count_dictionary[character] = 1
    return character_count_dictionary

def print_report(path_to_file):
    print(f"--- Begin report of {path_to_file} ---")
    book = read_books(path_to_file)
    
    word_count = count_words(book)
    print(f"{word_count} words found in the document")

    print()
    print()

    character_dictionary = count_characters(book)

     # Sort the character_dictionary by count in decreasing order
    sorted_characters = sorted(character_dictionary.items(), key=lambda x: x[1], reverse=True)

    for character, count in sorted_characters:
        if character.isalpha() == True:
            print(f"The '{character}' was found {count} times")

    print("--- End report ---")
    
def main():
    print_report("books/frankenstein.txt")

if __name__ == "__main__":
    main()