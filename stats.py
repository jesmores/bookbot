def get_num_words(text):
    """
    Count the number of words in a string
    """
    return len(text.split())


def get_character_counts(text):
    """
    Count the number of each character in a string.
    :param text: The input string.
    :return: A dictionary with characters as keys and their counts as values.
    """
    character_counts = {}
    lower_text = text.lower()  # Convert text to lowercase for case-insensitive counting
    for char in lower_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def get_sorted_character_list(chdict):
    """
    Given a dictionary of character counts, return a list of dictionaries
    of the form {'char': char, 'num': count} sorted by count in descending
    order
    """
    sorted_chars = sorted(chdict.items(), key=lambda item: item[1], reverse=True)
    return [{'char': char, 'num': count} for char, count in sorted_chars]