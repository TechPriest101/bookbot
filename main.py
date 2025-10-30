from stats import get_words_count, get_characters_count, sorted_list_of_dictionaries
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        words_count = get_words_count(text)
        char_count = get_characters_count(text)
        char_count_sorted = sorted_list_of_dictionaries(char_count)
        print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
        print(f"----------- Word Count ----------\nFound {words_count} total words")
        print("--------- Character Count -------")
        for char_num_pair in char_count_sorted:
            if char_num_pair['char'].isalpha():
                print(f"{char_num_pair['char']}: {char_num_pair['num']}")
        print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
