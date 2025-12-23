import csv

books = []
with open('1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        row['Year'] = int(row['Year'])
        row['Pages'] = int(row['Pages'])
        row['Price'] = int(row['Price'])
        books.append(row)

def print_content(books):
    print("Содержимое файла:")
    print("=" * 60)
    for book in books:
        for key, value in book.items():
            print(f"{key} → {value}")
        print("-" * 60)

def find_oldest_newest_book(books):
    oldest = min(books, key=lambda x: x['Year'])
    newest = max(books, key=lambda x: x['Year'])
    print(f"Самая старая книга: {oldest['Title']} ({oldest['Year']})")
    print(f"Самая новая книга: {newest['Title']} ({newest['Year']})")

def calculate_total_pages(books):
    total = sum(book['Pages'] for book in books)
    print(f"Общее количество страниц: {total}")
    return total

def calculate_average_price(books):
    avg = sum(book['Price'] for book in books) / len(books)
    print(f"Средняя цена книги: {avg:.2f} руб.")
    return avg

def count_books_by_genre(books):
    genres = {}
    for book in books:
        genre = book['Genre']
        genres[genre] = genres.get(genre, 0) + 1
    
    print("Количество книг по жанрам:")
    for genre, count in genres.items():
        print(f"  {genre}: {count}")
    return genres

print_content(books)
print("\n" + "=" * 60)
find_oldest_newest_book(books)
print()
calculate_total_pages(books)
calculate_average_price(books)
print()
count_books_by_genre(books)
