from db_connect import read_db_config, connect

class book:
    db_config = read_db_config()
    con = MySQLConnector(**db_config)
    c = con.cursor()
    def __init__(self, id, author, name, publication, available):
        self.id = id
        self.author = author
        self.name = name
        self.publication = publication
        self.available = available

    def insert_book(self):

