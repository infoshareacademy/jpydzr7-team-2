import sqlite3


def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        print("Zalogowano pomyślnie!")
    else:
        print("Błędna nazwa użytkownika lub hasło.")


if __name__ == "__main__":
    username = input("Wprowadź nazwę użytkownika: ")
    password = input("Wprowadź hasło: ")
    login(username, password)
