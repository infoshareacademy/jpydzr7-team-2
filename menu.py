from training_log import TrainingLog

def main_menu():
    user_name = "Pawel"
    training_log = TrainingLog(user_name)

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
                handle_choice(choice, training_log)  # Przekazujemy obiekt do funkcji
            elif choice == '11':
                print("Zamykam program...")
                save_data()
                break
        else:
            print("Błąd: Proszę wybrać poprawną opcję (1-11).")

def handle_choice(choice, training_log):  # Dodajemy parametr training_log
    if choice == '1':
        add_meal()
    elif choice == '2':
        choose_meal()
    elif choice == '3':
        training_log.add_training()  # Wywołanie metody na obiekcie training_log
    elif choice == '4':
        training_log.choose_training()  # Wywołanie metody na obiekcie training_log
    elif choice == '5':
        show_meals()
    elif choice == '6':
        training_log.show_trainings()  # Wywołanie metody na obiekcie training_log
    elif choice == '7':
        user_data()
    elif choice == '8':
        edit_meal()
    elif choice == '9':
        training_log.edit_training()  # Wywołanie metody na obiekcie training_log
    elif choice == '10':
        count_calories()

if __name__ == "__main__":
    main_menu()