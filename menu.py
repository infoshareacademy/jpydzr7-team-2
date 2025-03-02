def main_menu():
    while True:
        print("\nMenu FitApp:")
        print("1. Dodaj posiłek")
        print("2. Wybierz posiłek z listy")
        print("3. Dodaj trening")
        print("4. Wybierz trening z listy")
        print("5. Wyświetl listę posiłków")
        print("6. Wyświetl listę treningów")
        print("7. Wyświetl moje dane")
        print("8. Edytuj posiłek")
        print("9. Edytuj trening")
        print("10. Zlicz kalorie i pokaż ile jeszcze mogę przyjąć nowych")
        print("11. Zamknij program")

        choice = input("Wybierz opcję (1-11): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                handle_choice(choice)
            elif choice == '11':
                print("Zamykam program...")
                save_data()
                break
        else:
            print("Błąd: Proszę wybrać poprawną opcję (1-11).")

def handle_choice(choice):
    if choice == '1':
        add_meal()
    elif choice == '2':
        choose_meal()
    elif choice == '3':
        add_training()
    elif choice == '4':
        choose_training()
    elif choice == '5':
        show_meals()
    elif choice == '6':
        show_training()
    elif choice == '7':
        user_data()
    elif choice == '8':
        edit_meal()
    elif choice == '9':
        edit_training()
    elif choice == '10':
        count_calories()

def add_meal():
    print("Dodawanie posiłku...")

def choose_meal():
    print("Wybieranie posiłku...")

def add_training():
    print("Dodawanie treningu...")

def choose_training():
    print("Wybieranie treningu...")

def show_meals():
    print("Wyświetlanie listy posiłków...")

def show_training():
    print("Wyświetlanie listy treningów...")

def user_data():
    print("Wyświetlanie danych użytkownika...")

def edit_meal():
    print("Edycja posiłku...")

def edit_training():
    print("Edycja treningu...")

def count_calories():
    print("Zliczanie kalorii...")

def save_data():
    print("Zapisywanie danych użytkownika...")

if __name__ == "__main__":
    main_menu()