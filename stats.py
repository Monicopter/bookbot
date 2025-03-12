
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
        # if the entry exists within the dictionary it will simply increment by 1
        if lower_case.isalpha():
            char_count[lower_case] = char_count.get(lower_case, 0) + 1

    return char_count