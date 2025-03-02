import json
import os
from datetime import datetime
from user import User  # Importujemy klasę User

class Training:
    def __init__(self, activity, duration, calories_burned, date=None):
        self.activity = activity
        self.duration = duration  # czas trwania w minutach
        self.calories_burned = calories_burned  # spalone kalorie
        # Ustawiamy domyślną datę na dzisiaj w formacie YYYY-MM-DD, jeśli nie podano
        self.date = date if date else datetime.today().strftime('%Y-%m-%d')

    def __str__(self):
        return f"Data: {self.date}, Aktywność: {self.activity}, Czas: {self.duration} min, Spalone kalorie: {self.calories_burned} kcal"

    def to_dict(self):
        return {
            "activity": self.activity,
            "duration": self.duration,
            "calories_burned": self.calories_burned,
            "date": self.date
        }

class TrainingLog:
    def __init__(self, user_name):
        self.trainings = []
        self.user = None
        self.activities = {
            "Bieganie": 12,  # Kalorie spalane na minutę
            "Spacer": 4,
            "Siłownia": 8,
            "Jazda na rowerze": 8,
            "Pływanie": 15,
            "Fitness": 9,
            "Gra w squasha": 17
        }
        self.filename = f"{user_name}.json"  # Ustawiamy nazwę pliku na podstawie imienia użytkownika
        self.load_trainings()

    def load_trainings(self):
        """Wczytuje treningi i dane użytkownika z pliku JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.trainings = [Training(**item) for item in data['trainings']]
                self.user = User(**data['user']) if data['user'] else None

    def save_trainings(self):
        """Zapisuje treningi i dane użytkownika do pliku JSON."""
        with open(self.filename, 'w') as file:
            json.dump({
                "trainings": [training.to_dict() for training in self.trainings],
                "user": self.user.to_dict() if self.user else None
            }, file, indent=4)

    def add_user_info(self, name, age, gender):
        """Dodaje informacje o użytkowniku."""
        self.user = User(name, age, gender)
        self.save_trainings()  # Zapisz dane użytkownika po ich wprowadzeniu

    def display_activities(self):
        print("\nDostępne aktywności:")
        for index, activity in enumerate(self.activities.keys(), start=1):
            print(f"{index}. {activity}")

    def add_training(self):
        self.display_activities()
        choice = int(input("\nWybierz numer aktywności: ")) - 1

        if choice < 0 or choice >= len(self.activities):
            print("\nNieprawidłowy wybór. Spróbuj ponownie.")
            return

        activity = list(self.activities.keys())[choice]
        duration = int(input("\nPodaj czas trwania aktywności (w minutach): "))

        # Pobranie daty treningu, domyślnie dzisiaj w formacie YYYY-MM-DD
        while True:
            date_input = input(f"Podaj datę treningu (enter dla dzisiaj: {datetime.today().strftime('%Y-%m-%d')}): ")
            date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

            # Upewniamy się, że data jest w formacie YYYY-MM-DD i że nie jest w przyszłości
            try:
                entered_date = datetime.strptime(date, '%Y-%m-%d')

                if entered_date > datetime.today():
                    print("Nie możesz wprowadzić przyszłej daty. Spróbuj ponownie.")
                    continue  # Jeśli data jest w przyszłości, prośmy ponownie

                break  # Jeżeli data jest poprawna i nie jest w przyszłości, kończymy pętlę
            except ValueError:
                print("Nieprawidłowy format daty. Wprowadź datę w formacie YYYY-MM-DD.")

        # Obliczanie spalonych kalorii
        calories_per_minute = self.activities[activity]
        calories_burned = calories_per_minute * duration

        # Tworzenie nowego treningu z podaną lub domyślną datą
        new_training = Training(activity, duration, calories_burned, date)
        self.trainings.append(new_training)
        print(f"\nDodano trening: {new_training}")

        self.save_trainings()  # Zapisz treningi po ich dodaniu

    def show_trainings(self):
        """Wyświetlanie treningów z określonego dnia"""
        # Pobranie daty do wyświetlenia treningów, domyślnie dzisiaj
        while True:
            date_input = input(f"Podaj datę treningu do wyświetlenia (enter dla dzisiaj: {datetime.today().strftime('%Y-%m-%d')}): ")
            date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

            # Upewniamy się, że data jest w formacie YYYY-MM-DD
            try:
                entered_date = datetime.strptime(date, '%Y-%m-%d')

                if entered_date > datetime.today():
                    print("Nie możesz wprowadzić przyszłej daty. Spróbuj ponownie.")
                    continue  # Jeśli data jest w przyszłości, prośmy ponownie

                break  # Jeżeli data jest poprawna i nie jest w przyszłości, kończymy pętlę
            except ValueError:
                print("Nieprawidłowy format daty. Spróbuj ponownie wprowadzić datę w formacie YYYY-MM-DD.")

        # Filtrujemy treningi, aby pokazać tylko te z wybranej daty
        trainings_on_date = [training for training in self.trainings if training.date == date]

        if not trainings_on_date:
            print(f"Brak treningów z dnia {date}.")
            return

        print(f"\nTreningi z dnia {date}:")
        for index, training in enumerate(trainings_on_date, start=1):
            print(f"\n{index}. {training}")

    def remove_training(self):
        """Usuwanie treningu"""
        # Pobieramy datę treningu, domyślnie dzisiaj
        while True:
            date_input = input(f"Z którego dnia chcesz usunąć trening (enter dla dzisiaj: {datetime.today().strftime('%Y-%m-%d')}): ")
            date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

            # Upewniamy się, że data jest w formacie YYYY-MM-DD
            try:
                entered_date = datetime.strptime(date, '%Y-%m-%d')

                if entered_date > datetime.today():
                    print("Nie możesz wprowadzić przyszłej daty. Spróbuj ponownie.")
                    continue  # Jeśli data jest w przyszłości, prośmy ponownie

                break  # Jeżeli data jest poprawna i nie jest w przyszłości, kończymy pętlę
            except ValueError:
                print("Nieprawidłowy format daty. Wprowadź datę w formacie YYYY-MM-DD.")

        # Filtrowanie treningów z wybranego dnia
        trainings_on_date = [training for training in self.trainings if training.date == date]

        if not trainings_on_date:
            print(f"Brak treningów z dnia {date}.")
            return

        # Wyświetlanie dostępnych treningów z wybranego dnia
        print(f"\nDostępne treningi do usunięcia z dnia {date}:")
        for index, training in enumerate(trainings_on_date, start=1):
            print(f"\n{index}. {training}")

        while True:
            try:
                index_to_remove = input(f"Podaj numer treningu do usunięcia (lub 'exit' aby wyjść): ").strip().lower()

                if index_to_remove == 'exit':
                    print("Anulowano usuwanie treningu.")
                    break

                index_to_remove = int(index_to_remove) - 1

                if index_to_remove < 0 or index_to_remove >= len(trainings_on_date):
                    print("Nieprawidłowy wybór, spróbuj ponownie.")
                    continue

                # Usuwanie treningu
                self.trainings.remove(trainings_on_date[index_to_remove])
                print(f"Trening usunięty: {trainings_on_date[index_to_remove]}")
                self.save_trainings()
                break
            except ValueError:
                print("Proszę podać poprawny numer lub 'exit' aby wyjść.")
