import mysql.connector
from mysql.connector import MySQLConnection, Error
from db.db_connect import read_db_config, connect
from datetime import date, timedelta

class book:

    def __init__(self):
        db_config = read_db_config()
        self.con = MySQLConnection(**db_config)
        self.c = self.con.cursor()

    def __del__(self):
       # self.c.close()
       # self.con.close()
        print("Connection closed.")

    def insert_book(self, author, name, publication):
        query = """INSERT INTO book(author, book_nam, publication, available)
                    VALUES(%s, %s, %s, true)"""

        try:
            self.c.execute(query, (author, name, publication))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()
        return False

    def update_book(self, author, publication, book_name, book_id):
        query = """UPDATE book
                    SET author = %s, publication = %s, book_nam = %s
                    WHERE book_id = %s"""

        try:
            self.c.execute(query, (author, publication, book_name, book_id))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

    def delete_book(self, id):
        query = """DELETE FROM book WHERE book_id = %s"""

        try:
            self.c.execute(query, (id,))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

    def update_availability(self, book_id, availability):
        query = """UPDATE book
                    SET available = %s
                    WHERE book_id = %s"""
        try:
            self.c.execute(query, (availability,book_id))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

    def get_available_books(self):
        print("----List of books currently available for rent----")
        print("___________________________________________________")
        print(["Book ID", "Author", "Book Name", "Publication"])
        print("___________________________________________________")
        query = """SELECT book_id, author, book_nam, publication FROM book 
                WHERE available = 1"""

        try:
            self.c.execute(query)
            rows = self.c.fetchall()
            for row in rows:
                print(list(row))
            self.con.commit()

        except Error as e:
            print(e)

class librarian:
    def __init__(self):
        db_config = read_db_config()
        self.con = MySQLConnection(**db_config)
        self.c = self.con.cursor()

    def create_librarian(self, name, email, phone, password):
        query = """INSERT INTO librarian(libr_name, libr_email, libr_phone, libr_password)
                            VALUES(%s, %s, %s, %s)"""

        try:
            self.c.execute(query, (name, email, phone, password))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()
        return False

    def authentic_librarian(self, email, password):
        query = """SELECT libr_id FROM librarian WHERE libr_email = %s AND libr_password = %s"""

        try:
            self.c.execute(query, (email, password))
            row = self.c.fetchall()
            #print(row)
            #print(len(row))
            if len(row) == 1:
                return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

class user:
    def __init__(self):
        db_config = read_db_config()
        self.con = MySQLConnection(**db_config)
        self.c = self.con.cursor()

    def create_user(self, name, phone, password):
        query = """INSERT INTO users(user_name, user_phone, user_password)
                    VALUES(%s, %s, %s)"""

        try:
            self.c.execute(query, (name, phone, password))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

    def auth_user(self, uname, password):
        query = """SELECT user_id FROM users WHERE user_name = %s AND user_password = %s"""

        try:
            self.c.execute(query, (uname, password))
            rows = self.c.fetchall()
            for row in rows:
                return row[0]

        except Error as e:
            print(e)
            self.con.rollback()

        return 0

    def update_user(self, userid, name, phone, password):
        ## TODO: check implementaion of individual attributes update
        query = """UPDATE users
                            SET user_name = %s, user_phone = %s, user_password = %s
                            WHERE user_id = %s"""

        try:
            self.c.execute(query, (name, phone, password, userid))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()
        return False

    def delete_user(self, userid):
        query = """DELETE FROM users WHERE user_id = %s"""

        try:
            self.c.execute(query,(userid,))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False


class book_rental:
    def __init__(self):
        db_config = read_db_config()
        self.con = MySQLConnection(**db_config)
        self.c = self.con.cursor()

    def insert_record(self, book_id, user_id, rented_date, due_date):
        query = """INSERT INTO rented_books(book_id, user_id, rented_date, due_date)
                    VALUES(%s, %s, %s, %s)"""

        try:
            self.c.execute(query, (book_id, user_id, rented_date, due_date))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()

        return False

    def update_on_return(self, book_id, user_id, returned_date, fee):
        query = """UPDATE rented_books
                    SET returned_date = %s, fee = %s
                    WHERE book_id = %s AND user_id = %s"""

        try:
            self.c.execute(query, (returned_date, fee, book_id, user_id))
            self.con.commit()
            return True

        except Error as e:
            print(e)
            self.con.rollback()
            return False

    def rented_books(self, user_id):
        print("---------------List of books rented by you ----------------")
        print("___________________________________________________________")
        print(["Book ID", "Author", "Book Name", "Publication", "Due Date"])
        print("___________________________________________________________")
        query = """SELECT b.book_id, b.author, b.book_nam, b.publication, DATE_FORMAT(rb.due_date, "%Y-%m-%d")
                    FROM book b
                    inner join rented_books rb
                    on b.book_id = rb.book_id
                    AND rb.user_id = %s
                    AND rb.returned_date is null"""
        try:
            self.c.execute(query, (user_id,))
            rows = self.c.fetchall()
            for row in rows:
                print(list(row))

        except Error as e:
            print(e)

    def rent_a_book(self, user_id, book_id):
        now = date.today()
        due = now + timedelta(days = 14)
        if(self.insert_record(book_id, user_id, now, due)):
            b = book()
            b.update_availability(book_id, 0)
            return (True, due)
        return (False, null)

    def return_book(self, user_id, book_id):
        return_date = date.today()
        due_date = None
        query = """SELECT rb.due_date
                            FROM book b
                            inner join rented_books rb
                            on b.book_id = %s
                            AND rb.user_id = %s
                            AND rb.returned_date is null"""
        try:
            self.c.execute(query, (book_id, user_id))
            rows = self.c.fetchall()
            for row in rows:
                due_date = row[0]
            self.con.commit()

        except Error as e:
            print(e)

        if(due_date != None):
            overdue_days = (return_date - due_date).days
            if (overdue_days <= 14):
                fee = 0
            elif (overdue_days <= 20):
                fee = 20
            else:
                fee = self.calc_fee(overdue_days - 20)

        if(self.update_on_return(book_id, user_id, return_date, fee)):
            b = book()
            b.update_availability(book_id, 1)
            return (True, fee)
        return (False, None)


    def calc_fee(self, overdue_days):
        fee = 20
        increment = 5
        base = 20
        while overdue_days > 0:
            fee = fee + base + increment
            overdue_days -= 5
            increment += 5
        return fee


    def overdue_books(self, user_id):
        print("---------------List of overdue books --------------------")
        print("_________________________________________________________")
        try:
            if user_id == 0:
                print(["User ID", "Book ID", "Book Name", "Due Date", "Overdue days"])
                query = """SELECT rb.user_id, rb.book_id, b.book_nam,
                                  DATE_FORMAT(rb.due_date,"%Y-%m-%d"), DATEDIFF(current_date, rb.due_date) 
                        FROM book b
                           inner join rented_books rb
                           on b.book_id = rb.book_id
                           AND rb.returned_date is null
                           AND current_date > rb.due_date"""
                self.c.execute(query)
            else:
                print(["Book ID", "Book Name", "Due Date", "Overdue days"])
                query = """SELECT rb.book_id, b.book_nam, DATE_FORMAT(rb.due_date,"%Y-%m-%d"),
                                  DATEDIFF(current_date, rb.due_date) 
                        FROM book b
                           inner join rented_books rb
                           on b.book_id = rb.book_id
                           AND rb.user_id = %s
                           AND rb.returned_date is null
                           AND current_date > rb.due_date"""
                self.c.execute(query, (user_id,))

            print("_______________________________________________________")

            rows = self.c.fetchall()
            for row in rows:
                print(list(row))

        except Error as e:
            print(e)
