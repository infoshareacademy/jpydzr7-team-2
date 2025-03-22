from training_log import TrainingLog
from MealMenu import MealTracker
import json


def main_menu(user_name):
    training_log = TrainingLog(user_name)
    meal_tracker = MealTracker(user_name)  # Tworzymy instancję MealTracker

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

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            handle_choice(choice, training_log, meal_tracker)  # Przekazujemy meal_tracker
        elif choice == '11':
            print("Zamykam program...")
            break
        else:
            print("Błąd: Proszę wybrać poprawną opcję (1-11).")

def handle_choice(choice, training_log, meal_tracker):  # Dodajemy meal_tracker
    if choice == '1':
        meal_tracker.add_meal()  # Wywołujemy metodę na obiekcie meal_tracker
    elif choice == '2':
        meal_tracker.choose_meal()
    elif choice == '3':
        training_log.add_training()
    elif choice == '4':
        training_log.choose_training()
    elif choice == '5':
        meal_tracker.display_meals_summary()
    elif choice == '6':
        training_log.show_trainings()
    elif choice == '7':
        print("Funkcja wyświetlania danych w trakcie implementacji")
    elif choice == '8':
        print("Funkcja edycji posiłków w trakcie implementacji")
    elif choice == '9':
        print("Funkcja edycji treningów w trakcie implementacji")
    elif choice == '10':
        meal_tracker.display_meals_summary()

if __name__ == "__main__":
    user_name = input("Podaj swoje imię: ")  # Pobierz imię od użytkownika
    main_menu(user_name)  # Przekaż user_name do funkcji
