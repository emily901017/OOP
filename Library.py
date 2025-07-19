# 3. 圖書館書籍管理
# 需求：

# 設計 Book 類別，包含：

# 書名、作者、ISBN、是否被借出

# 設計一個 Library 類別，能夠：

# 加入書籍

# 借出與歸還書籍

# 查詢特定書籍是否可借
# 目標：練習管理集合（list）與封裝操作。


class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"{book.title} 已成功借出"
        return f"{title} 不可借出或已被借出"  #在沒找到匹配書的情況下，book 可能不是要找的那本
    
    def return_book(self,title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"{book.title} 已成功歸還"
        return f"{title} 不可歸還或尚未借出"
    
    def is_book_available(self,title):
        for book in self.books:
            if book.title == title:
                return f"{book.title} 可借"
        return f"{title} 不在書庫中" #book.title會報錯，因為 book 在那時可能不存在
    
library_system = Library()
book1 = Book("天龍八部","金庸",12345678)
book2 = Book("神鵰俠侶","金庸",24681357)

library_system.add_book(book1)
library_system.add_book(book2)

print(library_system.borrow_book("天龍八部"))
print(library_system.borrow_book("天龍八部"))
print(library_system.return_book("天龍八部"))
print(library_system.return_book("天龍八部"))
print(library_system.is_book_available("天龍八部"))
print(library_system.is_book_available("神鵰俠侶"))
print(library_system.is_book_available("貓戰士"))


      
    
    


        
        
        