
def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
   

main()