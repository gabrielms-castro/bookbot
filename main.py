import string

def read_file(path):    
    with open(path, "r") as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    number_of_words = len(book.split())
    return number_of_words


def to_lower(book):
    lowered_book = book.lower()
    return lowered_book

def count_characters(book):
    letters_dict = {char: 0 for char in string.ascii_lowercase}
    
    lowered_book = to_lower(book)
    
    for char in lowered_book:
        if char in letters_dict:
            letters_dict[char] += 1
    
    letters_list = [{"letter": key, "num": value} for key, value in letters_dict.items()]
    return letters_list


def sort_on(dict):
    return dict["num"]

def loop_through_letters(book):
    number_of_characters = count_characters(book)
    number_of_characters.sort(reverse=True, key=sort_on)
    
    info = [f"The '{dict['letter']}' character was found {dict['num']} times" for dict in number_of_characters]
    return info

def report(path, book):
    number_of_words = count_words(book)
    character_info = loop_through_letters(book)

    report = f"""
    --- Begin report of {path} ---
    {number_of_words} words found in the document
    
    """
    report += "\n".join(character_info)
    report += f"\n--- End report ---"
    return report
    
def main():
    path = "books/frankenstein.txt"
    book = read_file(path)
    print(report(path, book))
    
if __name__ == "__main__":
    main()
    