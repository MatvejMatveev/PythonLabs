import csv
import xml.etree.ElementTree as ET
import random

def read_table(data):
    with open(data, mode="r", encoding="windows-1251") as file:
        csv_table = csv.reader(file, delimiter= ";")
        table = list(csv_table)
    return table

#Задание 1
def task_1(data):
    table = read_table(data)[1:]
    task_1 = sum(1 for line in table if len(line[1]) > 30)
    print(task_1)

#task_1("books.csv")

#Задание 2
def find_books_by_authors(data):
    table = read_table(data)[1:]
    while True:
        user_author = input("Введите интересующего вас автора: ").lower().strip()
        count = 0
        for line in table:
            price = float(line[7])
            table_author = line[4].lower().strip()
            if set(user_author.split()).issubset(set(table_author.split())) and price < 150:
                print(line[1] + " " + line[4])
                count += 1
        if count == 0:
            print("Такого автора нет")

#find_books_by_authors("books.csv")    
    
#Задание 3
def generate_bibliography_links(data):
    table = read_table(data)[1:]
    table_150 = [line for line in table if float(line[7]) < 150]
    random_lines = random.sample(table_150, 20)
    with open('bibliography.txt', 'w', encoding='utf-8') as file:
        for i, line in enumerate(random_lines):
            author = line[4].strip()
            title = line[1]
            year = line[6].strip().split()[0]
            link = f"{i+1} {author}. {title} - {year}\n"
            file.write(link)

#generate_bibliography_links("books.csv")

#Задание 4
def parse_xml(data):
    tree = ET.parse(data)
    root = tree.getroot()

    books = dict()

    for book in root.findall("book"):
        title = book.find("title").text
        price = float(book.find("price").text)
        books[title] = price

    print(books)

#parse_xml("books.xml")

#Задание 5
def unique_genres(data):
    table = read_table(data)[1:]
    unique_genres = []

    for line in table:
        genres = line[-1].split("#")
        for genre in genres:
            if len(genre) > 0 and genre not in unique_genres:
                unique_genres.append(genre.strip())

    for genre in unique_genres:
        print(genre)

#unique_genres("books.csv")

#Задание 6
def top_20_books(data):
    table = read_table(data)[1:]
    table = sorted(table, key = lambda line: int(line[-5]), reverse = True)
    for line in table[:20]:
        print(f"{line[1].strip()} {line[-5]}")
    
top_20_books("books.csv")

