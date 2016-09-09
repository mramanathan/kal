import csv

# print("hello world")
# print('Welcome to GITAM', 10)

# I am a variable
name = 'Python'

# print(name)
name = 'GITAM'

# print(name)
# unicode
# int
name = 'Linux'
age = 25
# print(name, age)

# print('My name is {} and age is {}'.format(name, age))
# print('My name is %s and age is %d' % (name, age))

# Arthimetic operations
a = 2
b = 3

# Subtraction
res = a - b

# print(res)
# print(a + b)
# print(int('23'))

# division
a = 4
b = 2
res = a / b

# print(int(res))
# print(float(1))

# multiplication
a = 2
b = 3.0
res = a * b

# print(res)
# raised to 2
# print(2 ** 20)

# Multi line string
"""this is multi line comment.
Interpreter doesn't print this line.
Let's check
"""

email = """
Hi {}
   How are you?
""".format(name)

# print(email)
# Methods
upcase = name.upper()

# print(upcase)
# print(name)
# print(name.lower())
# print(name.title())

# Get input from user
# name = input('Say me your name: ')
# print('How you doing {}?'.format(name))
# a = input('a:')
# b = input('b:')
# print(int(a) + int(b))

# print('welcome' * 3)
# Functions -- building block

# Square
def square(no):
    return no * no

# print(square(2))
# res = square(no=23)
# print(res)

# Cube
# def cube(no=2):
#     return square(no) * no

# print(cube(8))
# print(cube())

# delimiter
# def delimiter():
#     print('-' * 80)

# print(delimiter())

# Data structure
# Tuple -- Immutable data structure
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday')

# print(weekdays)
# delimiter()
# Print first weekday
# print(weekdays[0])
# print second weekday
# print(weekdays[1])
# print last weekday
# print(weekdays[-1])
# print(weekdays[-2])
# print all working days

# Modify first weekday to 'Jo'

# weekdays[0] = 'Jo'

# List -- Mutable data structure
collection = ['Lang', 23, 1989, 34.90]

# print(collection)
# Replace 3rd item
collection[2] = 'Python'

# print(collection)
# Add a new item at the end
collection.append('Telugu')

# print(collection)                        
# Find an element in the list
# print(collection.index(23))
# print(collection.index('foo'))
collection.append(weekdays)

# print(collection)
# print(collection[-1][-1])

# for Loop
# for item in collection:
#     print(item)

# While loop
# count = len(collection)
# print(count)
# index = 0
# while index < count:
#     print(collection[index])
#     index += 1

# nos = [1, 2, 3, 4]
# for no in nos:
#     if no % 2 == 0:
#         print(no, 'even')
#     else:
#         print(no, 'odd')
# File handling

# Write list of movies to file
file = open('movies.txt', 'w')
file.write('The Secret World of Pets\n')
file.write('Big Fat Giant\n')
file.close()

# Read list of movies from the file.

# file = open('movies.txt', 'r')
# for line in file:
#     print(line)
# file.close()
# Read file as context manager
# with open('movies.txt', 'r') as file:
#     for line in file:
#         print(line)

# Standard library - CSV
with open('movies.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Roja', '1996'])
    writer.writerow(['Sagara Sangamam', '1983'])

# delimiter()
with open('movies.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        # print(line)
        pass

# Write list of name and profession to csv file

# Read list of names from csv file

# Command line arguments
import sys
print(sys.argv)
if 'read' in sys.argv:
    print('you passed read argument', sys.argv[-1])

# Dictionary
rating = {'The God Father': 9.8, 'The Secret World of Pets': 9, 'Langs': ['Python'], 'GITAM': 10}
# print(rating['Langs'])
for key, val in rating.items():
    if key == 'Langs':
        rating[key].append('python')
# Add a new item
rating['PyCon'] = 2016
print('PyCon' in rating)
print(rating)

# Print key and value
#

# Get key and values

# Create a class called Person with attributes `first_name`, `last_name`
# `age`

class Person:
    def __init__(self, first_name, year_of_birth,
                 last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __repr__(self):
        return "Person(first_name={}, last_name={}, year_of_birth={})".format(self.first_name, self.last_name, self.year_of_birth)

    def age(self):
        return 2016 - self.year_of_birth


ram = Person('Ram', 1973, 'M')
siva = Person(last_name='Kumar', first_name='Siva',
              year_of_birth=1984)

print(ram.first_name, ram.last_name)
print(ram)
print(siva.first_name, siva.last_name)
print(siva.age())

# Change attribute value
siva.first_name = 'Siva Subramaniam'
print(siva.first_name)
