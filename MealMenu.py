import json


class Meal:
    def __init__(self, name, meal_type, calories):
        self.name = name
        self.meal_type = meal_type
        self.calories = calories

    def __str__(self):
        return f"{self.name} - {self.calories} kcal ({self.meal_type})"

    def to_dict(self):
        return {
            "name": self.name,
            "meal_type": self.meal_type,
            "calories": self.calories
        }

    @classmethod
    def from_dict(cls, meal_data):
        """Konwertuje dane z formatu słownika na obiekt Meal."""
        return cls(meal_data["name"], meal_data["meal_type"], meal_data["calories"])


class MealTracker:
    def __init__(self, user_name):
        self.meals = []
        self.allowed_meal_types = ["Śniadanie", "Lunch", "Obiad", "Przekąska", "Kolacja"]
        self.filename = f"{user_name}_meals.json"
        self.load_meals()  # Ładujemy posiłki z pliku podczas tworzenia obiektu

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
        self.save_meals()

    def save_meals(self):
        """Zapisuje posiłki do pliku JSON."""
        with open(self.filename, 'w') as file:
            data = {
                "meals": [meal.to_dict() for meal in self.meals]
            }
            json.dump(data, file, indent=4)

    def load_meals(self):
        """Ładuje posiłki z pliku JSON."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                # Zakładając, że każdy posiłek jest słownikiem, który można przekonwertować na obiekt Meal
                self.meals = [Meal.from_dict(meal_data) for meal_data in data.get("meals", [])]
        except FileNotFoundError:
            print(f"Plik {self.filename} nie został znaleziony. Utworzymy nowy plik.")
        except json.JSONDecodeError:
            print(f"Plik {self.filename} jest uszkodzony lub zawiera nieprawidłowe dane.")

    def choose_meal(self):
        if not self.meals:
            print("Brak dostępnych posiłków.")
            return

        print("Dostępne posiłki:")
        for i, meal in enumerate(self.meals, start=1):
            print(f"{i}. {meal}")

    def display_meals_summary(self):
        """Wyświetla podsumowanie posiłków."""
        if not self.meals:
            print("Brak dodanych posiłków.")
            return

        print("Podsumowanie posiłków:")
        for meal in self.meals:
            print(f"Posiłek: {meal.name}")
            print(f"Typ: {meal.meal_type}")
            print(f"Kalorie: {meal.calories}")
            print("-" * 20)
