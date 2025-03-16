class Meal:
    def __init__(self, name, meal_type, calories):
        self.name = name
        self.meal_type = meal_type
        self.calories = calories

    def __str__(self):
        return f"{self.name} - {self.calories} kcal ({self.meal_type})"


class MealTracker:
    def __init__(self, daily_calorie_limit):
        self.meals = []
        self.allowed_meal_types = ["Śniadanie", "Lunch", "Obiad", "Przekąska", "Kolacja"]
        self.daily_calorie_limit = daily_calorie_limit

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

    def display_meals_summary(self):
        if not self.meals:
            print("Brak dodanych posiłków.")
            return

        total_calories = sum(meal.calories for meal in self.meals)
        remaining_calories = self.daily_calorie_limit - total_calories

        print("\nPodsumowanie posiłków:")
        for meal in self.meals:
            print(meal)
        print(f"Suma kalorii: {total_calories} kcal")
        print(f"Pozostałe kalorie do spożycia: {remaining_calories} kcal")


def main():
    daily_calorie_limit = int(input("Podaj dzienny limit kalorii: "))
    tracker = MealTracker(daily_calorie_limit)

    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj posiłek")
        print("2. Wybierz posiłek")
        print("3. Wyświetl podsumowanie posiłków")
        print("4. Wyjdź")

        choice = input("Wybór: ")

        if choice == '1':
            tracker.add_meal()
        elif choice == '2':
            tracker.choose_meal()
        elif choice == '3':
            tracker.display_meals_summary()
        elif choice == '4':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()