from stats import get_num_words, char_count, sort_char_count
import sys

def get_book_test(fp):
    with open(fp) as f:
        book_content = f.read()

        count = get_num_words(book_content)
        letter_count = char_count(book_content)
        sorted = sort_char_count(letter_count)
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("----------- Character Count ----------")
        for key, val in sorted.items():
            print(f"{key}: {val}")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_test(sys.argv[1])


if __name__ == "__main__":
    main()
