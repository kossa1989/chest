import sqlite3
from Hashconf import key_from_pass


basename = "database.db"

conn = sqlite3.connect(basename)
c = conn.cursor()


class Account:
    def __init__(self):
        q1 = input ("Chcesz dodać konto? (Tak/Nie)")
        if str.lower(q1) == "tak":
            self.insert_account()
        elif str.lower(q1) == "nie":
            pass
        while str.lower(q1) not in ("tak", "nie"):
            q1 = input("Nie odpowiedzialeś na pytanie. Zadam je jeszcze raz. Czy Chcesz dodać konto? (Tak/Nie)")
            if str.lower(q1) == "tak":
                self.insert_account()
            elif str.lower(q1) == "nie":
                break

    def insert_account(self):
        self.account = str(input("podaj opis do konta: "))
        self.login = str(input("Podaj nazwę konta: "))
        self.password = str(input("Podaj hasło: "))
        self.note = str(input('Uwagi: '))
        print("To jest Twoje konto: ", self.account, self.login, self.password + 'uwagi: '+ self.note)
        c.execute("INSERT INTO accounts (account_name, login, password, note) values (?,?,?,?)", (self.account,
        self.login, self.password, self.note))
        conn.commit()

    def select_account(self):
        pass


##Baza SQLite
def db_create():
    c.connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS accounts(
                id integer primary key,
                account_name text,
                login text,
                password text,
                note text
            );""")
    conn.commit()


def update_account():
    c.connection.cursor()
    search_account = input(str.lower('Podaj jakie konto chcesz edytować? '))
    print(search_account)
    search = c.execute("SELECT * FROM accounts WHERE account_name=?", (search_account,)) ##UWAGA NA PRZECINEK!
    x = search.fetchall()

    # c.execute("UPDATE accounts SET account_name = ?, login =?, password=?, note=?", ())
    conn.commit()


def db_delete_table():
        with conn:
            conn.execute("DROP Table accounts")


def create_keyfile():
    obj1 = key_from_pass()


#db_delete_table()
db_create()
a = Account()
update_account()


conn.close()
#c.close()


#db_delete_table()
#db_create()