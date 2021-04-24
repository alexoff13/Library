from __future__ import annotations

from Library import Library, Book, Author, Visitor, Librarian

library = Library({
    Book('Я собака', Author('Диоген')): 5,
    Book('Фитнес в изоляторе', Author('Чарльз Бронсон')): 10,
    Book('Mein Kampf', Author('Адольф Гитлер')): 1000000000000000000000000000,
    Book('Капитал', Author('Карл Маркс')): 1,
})
librarian = Librarian(library)
visitor = Visitor('Иванов Иван', librarian)
library.add_visitor(visitor)

books = visitor.get_books_from_author('адольф гитлер')
book2 = visitor.get_book_from_name('капитал')
print(*books, book2, sep='\n')
