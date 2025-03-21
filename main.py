from stats import count_words, count_character, freq_sorter
import sys

def get_book_text(file_path) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        file_path = sys.argv[1] 

    book_contents = get_book_text(file_path=file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    print("----------- Word Count ----------")
    num_words = count_words(book_contents)
    print(f"Found {num_words} total words.")
    
    print("--------- Character Count -------")
    frequencies = count_character(book_contents)
    frequencies_list = freq_sorter(frequencies)

    for elem in frequencies_list:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["frequency"]}")
    
    print("============= END ===============")

    
main()