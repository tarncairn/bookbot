
def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def get_num_words(contents):
    num_words = len(contents.split())
    return num_words

def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = get_num_words
    print(f"{num_words} words found in the document")

main()