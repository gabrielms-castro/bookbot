import sys

from stats import (
    count_characters_dict, 
    get_num_words, 
    chars_dict_to_sorted_list
)

def get_book_text(book_filepath):    
    with open(book_filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def print_report(book_filepath, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")    


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exiting program with status code 1
    
    book_filepath = sys.argv[1] # using command line second argument as the book filepath    
    book = get_book_text(book_filepath=book_filepath)
    num_words = get_num_words(book)
    chars_dict = count_characters_dict(book)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_filepath=book_filepath, num_words=num_words, chars_sorted_list=chars_sorted_list)

if __name__ == "__main__":
    main()
    