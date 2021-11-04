import uuid
import time, math

class Book:
    def __init__(self, bookName, bookGenre, bookPrice):
        self.bookName = bookName
        self.bookGenre = bookGenre
        self.bookPrice = bookPrice
        self.bookId = 'B-' + uuid.uuid4().hex
        self.isTaken = False
        self.dateOfIssue = None
        self.issuedTo = None


class LibraryManagement:
    def __init__(self, libraryName):
        self.libraryName = libraryName
        self.librarianName = None
        self.totalCustomers = 0
        self.totalBooks = 0
        self.bookRecord = []
        self.customerRecord = []

    def depositBook(self, book):
        bookDict = {
            'book_id': book.bookId,
            'book_name': book.bookName,
            'book_price': book.bookPrice
        }

        self.bookRecord.append(bookDict)
        self.totalBooks = self.totalBooks + 1
        return book.bookId

    def registerCustomer(self, customer):
        customerDict = {
            'customer_id': customer.customerId,
            'customer_name': customer.customerName,
        }

        self.customerRecord.append(customerDict)
        self.totalCustomers = self.totalCustomers + 1
        return customer.customerId


class Customer:
    def __init__(self, customerName):
        self.customerName = customerName
        self.customerId = 'C-' + uuid.uuid4().hex
        self.issuedBooks = []
        self.lastCheckin = None
        self.isFeesPayed = False

    def payFees(self, librarian, amount):
        if librarian.approvePayment(self.isFeesPayed, amount) is True:
            self.isFeesPayed = True
            librarian.issueInvoice(self)
            return  True
        else:
            return  False


class Librarian:
    def __init__(self, librarianName, salary):
        self.librarianName = librarianName
        self.salary = salary
        self.librarianId = 'L-' + uuid.uuid4().hex

    def issueBook(self, book, customer):
        book.issuedTo = customer.customerId
        book.isTaken = True
        issueTime = math.floor(time.time() * 1000)
        customer.lastCheckin = issueTime
        book.dateOfIssue = issueTime
        customer.issuedBooks.append(book.bookId)
        return book.bookId

    def depositBook(self, book, customer):
        book.issuedTo = None
        book.isTaken = None
        book.dateOfIssue = None
        customer.issuedBooks.remove(book.bookId)
        return book.bookId

    def approvePayment(self,isFeesPayed, amount):
        if isFeesPayed == False and amount == '100':
            return True
        else:
            return False

    def issueInvoice(self, customer):
        print(f'INVOICE: CUST ID: {customer.customerId} CUST NAME: {customer.customerName} FEES PAYED')
        return



