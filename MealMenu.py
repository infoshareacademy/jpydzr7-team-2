class Meal:
    def __init__(self, name, meal_type, calories):
        self.name = name
        self.meal_type = meal_type
        self.calories = calories

    def __str__(self):
        return f"{self.name} - {self.calories} kcal ({self.meal_type})"


class MealTracker:
    def __init__(self):
        self.meals = []
        self.allowed_meal_types = ["Śniadanie", "Lunch", "Obiad", "Przekąska", "Kolacja"]

    def add_meal(self):
        name = input("Podaj nazwę posiłku: ")

        while True:
            meal_type = input("Wybierz typ posiłku (Śniadanie, Lunch, Obiad, Przekąska, Kolacja): ")
            if meal_type in self.allowed_meal_types:
                break
            else:
                print("Nieprawidłowy typ posiłku. Spróbuj ponownie.")

        while True:
            try:
                calories = int(input("Podaj ilość kalorii: "))
                break
            except ValueError:
                print("Proszę wpisać tylko cyfry.")

        new_meal = Meal(name, meal_type, calories)
        self.meals.append(new_meal)
        print(f"Posiłek '{name}' został dodany.")

    def choose_meal(self):
        if not self.meals:
            print("Brak dostępnych posiłków.")
            return

        print("Dostępne posiłki:")
        for i, meal in enumerate(self.meals, start=1):
            print(f"{i}. {meal}")


def main():
    tracker = MealTracker()

    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj posiłek")
        print("2. Wybierz posiłek")
        print("3. Wyjdź")

        choice = input("Wybór: ")

        if choice == '1':
            tracker.add_meal()
        elif choice == '2':
            tracker.choose_meal()
        elif choice == '3':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()