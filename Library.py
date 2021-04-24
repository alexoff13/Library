from __future__ import annotations


class Book:
    def __init__(self, name: str, author: Author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f'{self.__name} : {self.author.name}'

class Author:
    def __init__(self, name: str, books: list[Book] = None):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


class Librarian:
    def __init__(self, library: Library):
        self.__library = library

    def __try_get_book(self, book) -> bool:
        try:
            self.__library.get_book(book)
            return True
        except Exception:
            return False

    def __check_visitor(self, visitor: Visitor):
        if visitor not in self.__library.visitors:
            return False
        return True

    def get_books_from_author(self, visitor: Visitor, author: str):
        if not self.__check_visitor(visitor):
            return None

        books = list()
        for book in self.__library.books:
            if book.author.name.lower() == author:
                if self.__try_get_book(book):
                    books.append(book)
        return books

    def get_book_from_name(self, visitor: Visitor, name):
        if not self.__check_visitor(visitor):
            return None
        for book in self.__library.books.keys():
            if book.name.lower() == name:
                if self.__try_get_book(book):
                    return book
        return None

    def get_book(self, visitor: Visitor, name: str, author: str):
        if not self.__check_visitor(visitor):
            return None
        for book in self.__library.books.keys():
            if book.author.name.lower() == author and book.name.lower() == name:
                if self.__try_get_book(book):
                    return book


class Visitor:
    def __init__(self, name: str, librarian: Librarian):
        self.__librarian = librarian
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_books_from_author(self, author: str) -> list[Book]:
        return self.__librarian.get_books_from_author(self, author.lower())

    def get_book_from_name(self, name: str) -> Book:
        return self.__librarian.get_book_from_name(self, name.lower())

    def get_book(self, name: str, author: str):
        return self.__librarian.get_book(self, name.lower(), author.lower())


class Library:
    def __init__(self, books: dict[Book, int], ):
        self.__visitors = list()
        self.__books = books

    @property
    def books(self) -> dict[Book, int]:
        return self.__books

    @property
    def visitors(self) -> list[Visitor]:
        return self.__visitors

    def add_visitor(self, visitor: Visitor) -> None:
        self.__visitors.append(visitor)

    def add_book(self, book: Book, count: int):
        count = count if count >= 0 else 0
        if book not in self.__books.keys():
            self.__books[book] = count
        else:
            self.__books[book] += count

    def get_book(self, book) -> None:
        if book not in self.__books.keys():
            raise Exception('Такой книги нет в библиотеке!')
        if self.__books[book] <= 0:
            raise Exception('Эти книги закончились!')
        self.__books[book] -= 1

    def return_book(self, book):
        if book not in self.__books.keys():
            raise Exception('Такой книги нет в библиотеке!')
        self.__books[book] += 1
