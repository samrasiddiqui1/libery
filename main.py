import json
import os

dataFile = 'library.txt'

def loadlibrary():
    if os.path.exists(dataFile):
        with open(dataFile, 'r') as file:
            return json.load(file)
    return []

def savelibrary():
    with open(dataFile, 'w') as file:
        json.dump(library, file)

def addbook():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_input = input("Have you read the book? (yes/no): ").lower()

    read = read_input == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    savelibrary()
    print(f"✅ Book added successfully!")

def removebook():
    title = input("Enter the title of the book to remove: ")
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        savelibrary()
        print(f"✅ Title '{title}' removed successfully.")
    else:
        print(f"❌ Book '{title}' not found in the library.")

def searchlibrary():
    search_fields = ['title', 'author', 'genre']
    search_field = input("Search your book by (title/author/genre): ").lower()
    
    if search_field not in search_fields:
        print("❌ Invalid search field. Please choose title, author, or genre.")
        return
    
    search_term = input(f"Enter the {search_field}: ").lower()
    results = [book for book in library if search_term in book[search_field].lower()]
    
    if results:
        print("\n📖 Search Results:")
        for book in results:
            status = "Read" if book['read'] else 'Unread'
            print(f"- {book['title']} by {book['author']} ({book['year']}), {book['genre']} - {status}")
    else:
        print(f"❌ No books found matching '{search_term}' in {search_field}.")

def displayallbooks():
    if not library:
        print("The library is empty.")
        return
    print("\n📚 All Books in Library:")
    for book in library:
        status = "Read" if book['read'] else 'Unread'
        print(f"- {book['title']} by {book['author']} ({book['year']}), {book['genre']} - {status}")

def displaystatistics():
    total = len(library)
    read = sum(book['read'] for book in library)
    percentage = (read / total * 100) if total > 0 else 0
    print(f"\n📊 Library Statistics:")
    print(f"Total Books: {total}")
    print(f"Read Books: {read}")
    print(f"Unread Books: {total - read}")
    print(f"Read Percentage: {percentage:.1f}%")

def main():
    global library
    library = loadlibrary()

    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search the Library")
        print("4. Display All Books")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            addbook()
        elif choice == '2':
            removebook()
        elif choice == '3':
            searchlibrary()
        elif choice == '4':
            displayallbooks()
        elif choice == '5':
            displaystatistics()
        elif choice == '6':
            print("👋 Exiting the Library Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select a number between 1-6.")

if __name__ == "__main__":
    main()