import sys

from stats import word_count
from stats import char_count
from stats import sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    
    text = get_book_text(sys.argv[1])
    w_count = word_count(text)
    c_count = char_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    charlist = sort_chars(c_count)
    for char in charlist:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as book:
        return book.read()
    

main()