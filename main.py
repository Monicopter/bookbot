from stats import get_wordcount, get_alpha_count
#from stats import get_alpha_count

#Finds file through provided path and returns file to variable 'text' in main()
def get_book_text(path):
    with open(path) as f:
        return f.read()



# def book_report(wordcount, alphabet_count):

#     # Converts the alphabet_count dictionary into a key/value tuple then sorts 
#     # through it by frequency count in descending order
#     alphabet_count_sorted = sorted(alphabet_count.items(), key = lambda item: item[1], reverse = True)

#     print("============ BOOKBOT ============\n")
#     print(f"Analyzing book found at {book_path}...\n")

#     print("--- Begin report of books/frankenstein.txt ---\n")
#     print(f"{wordcount} words found in the document. \n")

#     #Loops through sorted tuple and prints each character stat on a new line
#     for char, count in alphabet_count_sorted:
#         print(f"The '{char}' character was found {count} times.")
#     print("--- End report ---")

########################################################################################################
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    alphabet_count = get_alpha_count(text)
    #book_report(wordcount, alphabet_count)

    
    # Converts the alphabet_count dictionary into a key/value tuple then sorts 
    # through it by frequency count in descending order
    alphabet_count_sorted = sorted(alphabet_count.items(), key = lambda item: item[1], reverse = True)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {wordcount} total words\n")
    print("--------- Character Count -------\n")

    #Loops through sorted tuple and prints each character stat on a new line
    for char, count in alphabet_count_sorted:
        print(f"{char}: {count}")
    print("============= END ===============")

main()