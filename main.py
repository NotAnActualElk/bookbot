def main():
    with open("books/frankenstein.txt") as get_book_text:
        book_contents = get_book_text.read()
        print(book_contents)

main()