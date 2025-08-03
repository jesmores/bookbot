from stats import get_num_words, get_character_counts, get_sorted_character_list
import sys

def get_book_text(book_path):
    """
    Reads the content of a book file and returns it as a string.
    
    :param book_path: Path to the book file.
    :return: Content of the book file as a string.
    """
    book_text = ""
    with open(book_path) as book_file:
        book_text = book_file.read()
    return book_text


def main():
    """
    Main function
    """
    if (len(sys.argv)) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_counts = get_character_counts(text)
    sorted_char_list = get_sorted_character_list(char_counts)
    
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_path} ...")
    print(f"----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print(f"----------- Character Count -----------")
    for entry in sorted_char_list:
        char = entry['char']
        count = entry['num']
        if (char.isalpha()):
            print(f"{char}: {count}")

main()
