
class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
        
    def displayAvaibleBooks(self):
        print("Books available in this library are: ")
        for items in self.books:
            print("  * " + items)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued '{bookName}' book. Please keep it safe and return it on time. ")
            self.books.remove(bookName)
        else:
            print("Sorry! Your requested book is occupied/not available. ")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for submitting the book. Have a good day. ")

class Student():

    def requestBook(self):
        self.bookName = input("Enter the book name you want to borrow: ")
        return self.bookName

    def returnBook(self):
        self.bookName = input("Enter the book name you want to return: ")
        return self.bookName

if __name__ == "__main__":
   cityLibrary = Library(["Never Split The Difference", "Drive", "Atomic Habits"
, "How to win friends and influence people", "Python", "CPP", "DJANGO", "Java", "JavaScript", "Clrs"])
   student = Student()

   while(True):
    welcomeMsg = '''
    ******Welcome to City Library******
    Please choose an option:
    1. List of all Books
    2. Issue a Book
    3. Add/Return a Book
    4. Exit LMS(Library Management System)
    '''
    print(welcomeMsg)
    try:
        a = int(input("Choose any option: "))

        if a == 1:
            cityLibrary.displayAvaibleBooks()
        elif a == 2:
            cityLibrary.borrowBook(student.requestBook())
        elif a == 3:
            cityLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing this system. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
    except Exception as e:
        print(f"error: {e}")
