import csv
import sys
"""
1. Write a snippet to get details of the book from user.
Details are name, author, year, and genre.
"""
"""
2. Refactor all input code into a function called `get_input()` and print the value.
"""

"""
2.1 Make `get_input` function to return multiple values.
"""

"""
3. Get user input to continue the input for one more book.
If the user enters `y` ask details for one more book and
for `n` exit the program.
While exiting the program print all the book details.
"""

"""
4. When user inputs `n`, user has given two books details.
Let's store two books in a list and each book details in a tuple.
While exiting the program print all the book details.
"""
"""
5. Convert the program to collect as many book user wants.
While exiting the program print all the book details.
"""
"""
6. While exiting the program store the information to a file named
'book_store.csv'.
"""

"""
7. When the program starts read the entered book details from the text file.
Print total records read from the file.
"""
"""
8. After reading all the records from the files, create a variable
`books_by_year` which stores list of books released in a particular year.
var = {'1918': [('a', '', ''), ()], '2008': [(), ()]}
"""

"""
9. Add support to command line arguments.
Allowed command line arguments are `new`, `print`
If none of the above arguments are passed program should error out.
If the input is `new`, ask list of questions for creating new book.
If the input is `print`, print all the existing book details.
"""

books = []


def get_input():
    print('Welcome to book store')
    name = input('Book name: ')
    author = input('Author: ')
    year = input('Year: ')
    genre = input('Genre: ')
    return (name, author, year, genre)


def print_book(book):
    print("Name: {}, Author: {}, Year: {}, Genre: {}".format(
        book[0], book[1], book[2], book[3]))


def main():
    books = [['The Animal farm', 'George Orwell', '1947', 'Satire'],
             ['The Outliers', 'Malcom Gladwell', '2008', 'Non-fiction'],
             ['War and Peace', 'Leo Tolstoy', '1918', 'Novel']]
    if 'new' in sys.argv:
        book = get_input()
        print(book)
    elif 'print' in sys.argv:
        print(books)
    else:
        print('Argument is invaid')


def save_books(books):
    with open('book_store.csv', 'w') as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow(book)


def read_books():
    with open('book_store.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            books.append(line)

read_books()
main()

"""
10. Create a class `Book` with the attributes `name, author, year, and
genre`.
"""

"""
11. Refactor the program to store the book details as an object rather than
tuple.
"""

"""
12. Add a method `to_csv` in the book class which will
return comma separated values.
"""

"""
13. While entering new book detail, check the book exists are not.
Update the existing book.
"""
