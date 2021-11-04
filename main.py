from models import *

library = LibraryManagement('Central Library')

librarian = Librarian('John', '10000')
customer1 = Customer('Steve')
book1 = Book('Math-1', 'Education', '100')

library.librarianName = librarian.librarianName

library.registerCustomer(customer1)
library.depositBook(book1)

librarian.issueBook(book1, customer1)

print(book1.isTaken)

librarian.depositBook(book1, customer1)
print(book1.isTaken)

result = customer1.payFees(librarian, '100')


