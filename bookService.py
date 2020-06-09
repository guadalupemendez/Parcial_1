from repository import Repository


class BookService():
    def add_book(self, book):
        lastKey = -1
        for key in Repository.booksList:
            lastKey = key
        lastKey += 1
        Repository.booksList[lastKey] = book._dict_
        return lastKey

    def update_book(self, bookKey, book_update):
        itsIn = False
        for books in Repository.booksList:
            if books == bookKey:
                itsIn = True
                break
        if itsIn:
            Repository.booksList[bookKey] = book_update._dict_
        else:
            raise ValueError

    def assign_book(self, book_id, member_legajo):
        itsIn = False
        for books in Repository.booksList:
            if books == book_id:
                itsIn = True
                break
        if itsIn:
            Repository.booksList[book_id]['_memberLegajo'] = member_legajo
        else:
            raise ValueError

    def delete_book(self, book_id):
        itsIn = False
        for books in Repository.booksList:
            if books == book_id:
                itsIn = True
                break
        if itsIn:
            del Repository.booksList[book_id]
        else:
            raise ValueError
