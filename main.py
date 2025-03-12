from stats import get_wordcount, get_alpha_count
import sys

#Finds file through provided path and returns file to variable 'text' in main()
def get_book_text(path):
    with open(path) as f:
        return f.read()

########################################################################################################
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    alphabet_count = get_alpha_count(text)

    # Converts the alphabet_count dictionary into a key/value tuple then sorts 
    # through it by frequency count in descending order
    alphabet_count_sorted = sorted(alphabet_count.items(), key = lambda item: item[1], reverse = True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")

    #Loops through sorted tuple and prints each character stat on a new line
    for char, count in alphabet_count_sorted:
        print(f"{char}: {count}")
    print("============= END ===============")

main()