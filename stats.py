def get_num_words(book):
    number_of_words = len(book.split())
    return number_of_words

def count_characters_dict(book):
    chars = {}
    for char in book:
        lowered_char = char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1 
        else:
            chars[lowered_char] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list