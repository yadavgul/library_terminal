
class library:

    def start_menu(self):
        print("---------------------------------------")
        print("         Welcome to Library!            ")
        print("---------------------------------------")
        print("1 -> Librarian Menu")
        print("2 -> User Menu")
        print("3 -> Quit")
        option = eval(input("Select an option: "))
        if not(option in range(1,4)):
            print("Incorrect input")
            self.start_menu()
        return option

    def librarian_menu(self):
        print("------------------------------------")
        print("          Librarian Menu            ")
        print("------------------------------------")
        print("1 -> New Registration")
        print("2 -> Login")
        print("3 -> Quit")
        option = eval(input("Select an option: "))
        if not(option in range(1,4)):
            print("Incorrect input")
            self.librarian_menu()
        return option

    def librarian_new_registration(self):
        name = input("Enter full name: ")
        email = input("Enter login email: ")
        phone_no = input("Enter phone no.: ")
        # TODO: Implemetation of password verification and masking
        password = input("Enter password: ")
        return (name, email, phone_no, password)

    def librarian_login(self):
        email = input("Enter login email: ")
        password = input("Enter password: ")
        return (email, password)

    def librarian_functions(self):
        print("--------------------------------------------")
        print("         Welcome to Librarian Options!      ")
        print("--------------------------------------------")
        print("1 -> Add Book")
        print("2 -> Update Book Details")
        print("3 -> Delete Book")
        print("4 -> Delete User")
        print("5 -> Quit")
        option = eval(input("Select an option: "))
        if not(option in range(1,6)):
            print("Incorrect input")
            self.librarian_functions()
        return option

    def book_details(self):
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        book_publication = input("Enter book publication: ")
        return(book_name, book_author, book_publication)

    def update_book(self):
        book_id = eval(input("Enter book ID to update book details: "))
        (book_name, book_author, book_publication) = self.book_details()
        return(book_id, book_name, book_author, book_publication)

    def delete_book(self):
        book_id = eval(input("Enter book ID to delete book: "))
        return book_id

    def delete_user(self):
        user_id = eval(input("Enter user ID to delete user: "))
        return user_id


