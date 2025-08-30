from stats import get_num_words, count_character_instances

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = get_num_words
    print(f"{num_words} words found in the document")
    character_instances = count_character_instances(contents)
    print(character_instances)
main()