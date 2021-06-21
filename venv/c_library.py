from model_lib.m_library import book, librarian, user, book_rental
from view_lib import view_library
from view_lib import view_user
from model_lib import m_library
import os


if __name__ == '__main__':
    lib = view_library.library()
    usr = view_user.user()
    librarian_obj = m_library.librarian()
    book_obj = m_library.book()
    user_obj = m_library.user()
    rent_obj = m_library.book_rental()
    while True:
        option = lib.start_menu()
        if option == 1:
            option = lib.librarian_menu()
            if option == 1:
                (name, email, phone_no, password)=lib.librarian_new_registration()
                if (librarian_obj.create_librarian(name, email, phone_no, password)):
                    print("Registration Successful")
                else:
                    print("Registration failed...")
            elif option == 2:
                (uname, password) = lib.librarian_login()
                rent_obj.overdue_books(0)
                if (librarian_obj.authentic_librarian(uname, password)):
                    while True:
                        option = lib.librarian_functions()
                        if option == 1:
                            (book_name, book_author, book_publication) = lib.book_details()
                            if (book_obj.insert_book(book_author, book_name, book_publication)):
                                print("Book added successfully...\n")
                            else:
                                print("Book could not be added...")
                        elif option == 2:
                            (book_id, book_name, book_author, book_publication) = lib.update_book()
                            if(book_obj.update_book(book_author, book_publication, book_name, book_id)):
                                print("Book details updated...")
                            else:
                                print("Book not updated...")
                        elif option == 3:
                            if(book_obj.delete_book(lib.delete_book())):
                                print("Book deleted...")
                            else:
                                print("Book could not be deleted...")
                        elif option == 4:
                             if(user_obj.delete_user(lib.delete_user())):
                                 print("User deleted...")
                             else:
                                 print("User deletion failed...")
                        else:
                            quit(0)
            else:
                quit(0)

        elif option == 2:
            option = usr.user_menu()
            if option == 1:
                (user_name, user_phone_no, password) = usr.user_new_registration()
                if(user_obj.create_user(user_name, user_phone_no, password)):
                    print("User registered successfully...")
                else:
                    print("User registration failed...")
            elif option == 2:
                (login_name, password) = usr.user_login()
                user_id = user_obj.auth_user(login_name, password)
                if (user_id != 0):
                    rent_obj.overdue_books(user_id)
                    while True:
                        option = usr.user_functions()
                        if option == 1:
                            (user_name, user_phone_no, password) = usr.update_details(user_id)
                            if(user_obj.update_user(user_id, user_name, user_phone_no, password)):
                                print("User details updated...")
                            else:
                                print("Update failed...")
                        elif option == 2:
                            book_obj.get_available_books()
                        elif option == 3:
                            rent_obj.rented_books(user_id)
                        elif option == 4:
                            book_id = usr.rent_return_book()
                            (updated, due_date) = rent_obj.rent_a_book(user_id, book_id)
                            if(updated):
                                print(f"Due date to return the book is: {due_date}")
                            else:
                                print("Not able to rent this book...")
                        elif option == 5:
                            book_id = usr.rent_return_book()
                            (returned, fee) = rent_obj.return_book(user_id, book_id)
                            if returned:
                                print(f"Your late fee is {fee}")
                            else:
                                print("Error while returning book. Contact admin.")
                        else:
                            quit(0)
                else:
                    print("Login failed...Invalid username or password")
        else:
            break
















