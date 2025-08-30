import sys
from stats import get_num_words, count_character_instances, sort_character_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    character_instances = count_character_instances(contents)
    counts = sort_character_counts(character_instances)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in counts:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
                
                
main()