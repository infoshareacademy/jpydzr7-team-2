from training_log import TrainingLog
from MealMenu import MealTracker


def main_menu(user_name):
    training_log = TrainingLog(user_name)
    meal_tracker = MealTracker(user_name)  # Tworzymy instancję MealTracker

    while True:
        print("\nMenu FitApp:")
        print("1. Dodaj posiłek")
        print("2. Wybierz posiłek z listy")
        print("3. Dodaj trening")
        print("4. Wyświetl listę posiłków")
        print("5. Wyświetl listę treningów")
        print("6. Wyświetl moje dane")
        print("7. Edytuj posiłek")
        print("8. Usuń trening")
        print("9. Zlicz kalorie i pokaż ile jeszcze mogę przyjąć nowych")
        print("10. Zamknij program")

        choice = input("Wybierz opcję (1-11): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            handle_choice(choice, training_log, meal_tracker, user_name)  # Przekazujemy user_name
        elif choice == '10':
            print("Zamykam program...")
            break
        else:
            print("Błąd: Proszę wybrać poprawną opcję (1-11).")


def handle_choice(choice, training_log, meal_tracker, user_name):  # Dodajemy user_name
    if choice == '1':
        meal_tracker.add_meal()  # Wywołujemy metodę na obiekcie meal_tracker
    elif choice == '2':
        meal_tracker.choose_meal()
    elif choice == '3':
        training_log.add_training()
    elif choice == '4':
        meal_tracker.display_meals_summary()
    elif choice == '5':
        training_log.show_trainings()
    elif choice == '6':
        # Wyświetlamy dane użytkownika
        display_user_data(user_name)
    elif choice == '7':
        print("Funkcja edycji posiłków w trakcie implementacji")
    elif choice == '8':
        training_log.remove_training()
    elif choice == '9':
        meal_tracker.display_meals_summary()


def display_user_data(user_name):
    from FitnessApp import Users
    users_dict = Users.load_users()

    if user_name in users_dict:
        user_data = users_dict[user_name]
        print("\nDane użytkownika:")
        print(f"Nazwa użytkownika: {user_data['user_name']}")
        print(f"Wiek: {user_data['age']} lat")
        print(f"Waga: {user_data['weight']} kg")
        print(f"Wzrost: {user_data['height']} cm")
        print(f"Płeć: {'Kobieta' if user_data['gender'] == 'K' else 'Mężczyzna'}")
        # Obliczamy BMI
        bmi = (user_data['weight']) / ((user_data['height'] / 100) ** 2)
        print(f"Twoje BMI: {bmi:.2f}")
        # Możesz dodać więcej szczegółów, np. dzienne zapotrzebowanie na kalorie
        kcal = 1800 if user_data['gender'] == 'K' else 2200
        print(f"Twoja dzienna ilość kalorii: {kcal} kcal")
    else:
        print(f"Użytkownik {user_name} nie istnieje w bazie.")


if __name__ == "__main__":
    user_name = input("Podaj swoje imię: ")  # Pobierz imię od użytkownika
    main_menu(user_name)  # Przekaż user_name do funkcji