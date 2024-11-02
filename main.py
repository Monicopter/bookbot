def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    alphabet_count = get_alpha_count(text)
    print(text)
    print(f"This text contains {wordcount} words.")
    print(alphabet_count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_wordcount(text):
    wordcount = len(text.split())
    return wordcount

def get_alpha_count(text):
    char_count = {}
    for char in text:
        #converts each character to lower case for ease of counting
        lower_case = char.lower()

        # Checks if the char is alphabetical, if it is then it checks the 
        # dictionary char_count for an existing entry, if it doesn't exist
        # it will create a new entry for the character and initialize to 1
        # if the entry exists withing the dictionary it will simply increment by 1
        if lower_case.isalpha():
            char_count[lower_case] = char_count.get(lower_case, 0) + 1

    # sorts the dictionary char_count so that the character appear in alphabetical 
    # order in a new dictionary
    sorted_dict = dict(sorted(char_count.items()))

    return sorted_dict


main()