
class user:
    def user_menu(self):
        print("--------------------------------")
        print("           User Menu            ")
        print("--------------------------------")
        print("1 -> New Registration")
        print("2 -> Login")
        print("3 -> Quit")
        option = eval(input("Select an option: "))
        if not (option in range(1, 4)):
            print("Incorrect input")
            self.user_menu()
        return option

    def user_new_registration(self):
        user_name = input("Enter user name: ")
        user_phone_no = input("Enter phone no.: ")
        password = input("Enter password: ")
        return (user_name, user_phone_no, password)

    def user_login(self):
        login_name = input("Enter login name: ")
        password = input("Enter password: ")
        return (login_name, password)

    def user_functions(self):
        print("-----------------------------------")
        print("    Welcome to User Menu!          ")
        print("-----------------------------------")
        print("1 -> Update User Details")
        print("2 -> View Available Books")
        print("3 -> View Rented Books")
        print("4 -> Rent a Book")
        print("5 -> Return a Book")
        print("6 -> Quit")
        option = eval(input("Select an option: "))
        if not(option in range(1,7)):
            print("Incorrect input")
            self.user_functions()
        return option

    def update_details(self, user_id):
        # user_id = eval(input("Enter User ID to update user details: "))
        (user_name, user_phone_no, password) = self.user_new_registration()
        return(user_name, user_phone_no, password)

    def rent_return_book(self):
        book_id = eval(input("Enter book_id to rent/return a book: "))
        return book_id

