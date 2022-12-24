"""This assignment I mainly use a list of lists to store the information of books. Ask user their choice by menu,
and then do the corresponding operation.
Name: Donglin Li
Date started: 2022/12/14
GitHub URL: https://github.com/DonglinLiJCU/assignment-1-DonglinLiJCU-public
"""


def main():
    """..."""
    books = []
    print("Reading Tracker 1.0 - by Donglin Li")
    book_cnt = load_books(books)
    print(f"{book_cnt} books loaded")
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_books(books)
        elif choice == "A":
            books.append(add_book())
        elif choice == "M":
            books = mark_as_completed(books)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>> ").upper()
    write_to_file(books)
    print(f"{len(books)} books saved to books.csv")
    print("So many books, so little time. Donglin Li")


def load_books(books):
    with open("books.csv", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            parts = line.split(',')
            books.append([parts[0], parts[1], parts[2], parts[3]])
    return len(books)


def display_menu():
    print("Menu:")
    print("L - List books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")


def list_books(books):
    r_book_cnt = 0
    r_book_pages = 0
    for i in range(len(books)):
        if books[i][3] == 'c':
            print(f" {i + 1}. {books[i][0]:<40}by {books[i][1]:<20} {books[i][2]} pages")
        else:
            print(f"*{i + 1}. {books[i][0]:<40}by {books[i][1]:<20} {books[i][2]} pages")
            r_book_cnt += 1
            r_book_pages += int(books[i][2])
    if r_book_cnt == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You need to read {r_book_pages} pages in {r_book_cnt} books.")


def add_book():
    title = input("Title: ")
    while title == "":
        print("Input can not be blank")
        title = input("Title: ")
    author = input("Author: ")
    while author == "":
        print("Input can not be blank")
        author = input("Author: ")
    pages = input("Pages: ")
    while not pages.isdigit():
        if pages[0] == '-' and pages[1:].isdigit():
            print("Number must be > 0")
        else:
            print("Invalid input; enter a valid number")
        pages = input("Pages: ")
    while int(pages) <= 0:
        print("Number must be > 0")
        pages = input("Pages: ")
    print(f"{title} by {author}, ({pages} pages) added to Reading Tracker")
    return [title, author, int(pages), 'r']


def mark_as_completed(books):
    r_book_cnt = 0
    for book in books:
        if book[3] == 'r':
            r_book_cnt += 1
    if r_book_cnt == 0:
        print("No required books")
    else:
        list_books(books)
        print("Enter the number of a book to mark as completed")
        choice = input(">>> ")
        while not choice.isdigit():
            if choice[0] == '-' and choice[1:].isdigit():
                print("Number must be > 0")
            else:
                print("Invalid input; enter a valid number")
            choice = input(">>> ")
        while int(choice) <= 0:
            print("Number must be > 0")
            choice = input(">>> ")
        while int(choice) > len(books):
            print("Invalid book number")
            choice = input(">>> ")
        if books[int(choice) - 1][3] == 'c':
            print("That book is already completed")
        else:
            books[int(choice) - 1][3] = 'c'
            print(f"{books[int(choice) - 1][0]} by {books[int(choice) - 1][1]} completed!")
    return books


def write_to_file(books):
    with open("books.csv", 'w') as file:
        for book in books:
            file.write(f"{book[0]},{book[1]},{book[2]},{book[3]}\n")


if __name__ == '__main__':
    main()
