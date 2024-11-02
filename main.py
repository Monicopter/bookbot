def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    alphabet_count = get_alpha_count(text)
    book_report(wordcount, alphabet_count)

#Finds file through provided path and returns file to variable 'text' in main()
def get_book_text(path):
    with open(path) as f:
        return f.read()

#sorts through the book and counts words using the blank spaces between strings  
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

    return char_count

def book_report(wordcount, alphabet_count):

    # Converts the alphabet_count dictionary into a key/value tuple then sorts 
    # through it by frequency count in descending order
    alphabet_count_sorted = sorted(alphabet_count.items(), key = lambda item: item[1], reverse = True)

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{wordcount} words found in the document. \n")

    #Loops through sorted tuple and prints each character stat on a new line
    for char, count in alphabet_count_sorted:
        print(f"The '{char}' character was found {count} times.")
    print("--- End report ---")

main()