import json
from menu import main_menu
from training_log import TrainingLog


class Users:
    users_dict_file = 'users_dict.json'  # słownik, który będzie przechowywał zarejestrowanych użytkowników

    def __init__(self, user_name=None, age=None, weight=None, height=None, gender=None):
        self.user_name = user_name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

    def __str__(self):
        return self.user_name

    def create_user_name(self):
        while True:
            user_name = input("Podaj nazwę użytkownika: ")
            if user_name.isalnum():  # sprawdzenie, czy nazwa zawiera tylko litery i cyfry
                return user_name
            else:
                print("Niepoprawna nazwa użytkownika. Użyj tylko liter i cyfr.")

    def age_control(self):
        while True:
            try:
                age = int(input("Podaj swój wiek: "))
                if age > 0:
                    return age
                else:
                    print("Wiek musi być liczbą większą niż 0.")
            except ValueError:
                print("Niepoprawny format.")

    def weight_control(self):
        while True:
            try:
                weight = float(input("Podaj swoją wagę w kg: "))
                if weight > 0:
                    return weight
                else:
                    print("Waga musi być liczbą większą niż 0.")
            except ValueError:
                print("Niepoprawny format.")

    def height_control(self):
        while True:
            try:
                height = float(input("Podaj swój wzrost w cm: "))
                if height > 0:
                    return height
                else:
                    print("Wzrost musi być liczbą większą niż 0.")
            except ValueError:
                print("Niepoprawny format.")

    def gender_control(self):
        while True:
            gender = input("Podaj swoją płeć (K/M): ").upper()
            if gender == 'K' or gender == 'M':
                return gender
            else:
                print("Niepoprawnby format.")

    def calculate_bmi(self, weight, height):
        height_m = height / 100  # przekształcenie wzrostu z cm na metry
        bmi = weight / (height_m ** 2)
        return bmi

    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Niedowaga"
        elif 18.5 <= bmi < 24.9:
            return "W normie"
        elif 25 <= bmi < 29.9:
            return "Nadwaga"
        else:
            return "Otyłość"

    def kcal(self, gender):
        if gender == 'K':
            return 1800
        else:
            return 2200

    @classmethod
    def load_users(cls):
        try:
            with open(cls.users_dict_file, "r") as file:
                users_dict = json.load(file)
                return users_dict
        except FileNotFoundError:
            return {}  # Jeśli plik nie istnieje to zwróci nam pusty słownik

    @classmethod
    def save_users(cls):
        with open(cls.users_dict_file, "w") as file:
            json.dump(cls.users_dict, file, indent=4)

    @classmethod
    def check_user_exists(cls, user_name):  # sprawdza czy użytkownik istnieje w bazie danych
        return user_name in cls.users_dict

    @classmethod
    def register_user(cls, user_name, age, weight, height, gender):
        new_user = Users(user_name, age, weight, height, gender)
        # Tworzymy instancję TrainingLog i zapisujemy użytkownika
        training_log = TrainingLog(user_name)
        training_log.user = new_user  # Zapiszemy użytkownika w TrainingLog
        training_log.save_trainings()  # Zapisujemy wszystkie dane (treningi i użytkownika)

        # Dodajemy nowego użytkownika do słownika i zapisujemy
        cls.users_dict[user_name] = new_user.__dict__
        cls.save_users()  # Zapisz słownik użytkowników do pliku
        print(f"Użytkownik {user_name} został zarejestrowany")

    @classmethod
    def edit_user_data(cls, user_name):
        if user_name in cls.users_dict:
            user_data = cls.users_dict[user_name]
            print(f"Aktualne dane użytkownika {user_name}: ")
            print(f"Wiek: {user_data['age']}")
            print(f"Waga: {user_data['weight']}")
            print(f"Wzrost: {user_data['height']}")
            print(f"Płeć: {user_data['gender']}")

            # Edytowanie danych
            user_data['age'] = int(input("Podaj aktualny wiek: "))
            user_data['weight'] = float(input("Podaj aktualną wagę: "))
            user_data['height'] = float(input("Podaj aktualny wzrost: "))

            cls.save_users()
            print(f"Dane użytkownika {user_name} zostały zaktualizowane")
        else:
            print(f"Użytkownik o nazwie {user_name} nie istnieje :(")


Users.users_dict = Users.load_users()  # Inicjalizacja bazy użytkowników


def create_new_user() -> bool:
    print("Witaj w aplikacji FitApp!")
    print("Aplikacja pomoże Ci zaplanować dietę oraz osiągnąć wymarzoną sylwetkę")
    try:
        user = Users()

        nazwa_uzytkownika = user.create_user_name()
        age = user.age_control()
        weight = user.weight_control()
        height = user.height_control()
        gender = user.gender_control()

        Users.register_user(nazwa_uzytkownika, age, weight, height, gender)

        bmi = user.calculate_bmi(weight, height)
        category = user.bmi_category(bmi)
        daily_kcal = user.kcal(gender)

        print("\nPodsumowanie wprowadzonych danych:")
        print(f"Nazwa użytkownika: {nazwa_uzytkownika}")
        print(f"Wiek: {age} lat")
        print(f"Waga: {weight} kg")
        print(f"Wzrost: {height} cm")
        print(f"Płeć: {'Kobieta' if gender == 'K' else 'Mężczyzna'}")
        print(f"Twoje BMI: {bmi:.2f} - {category}")
        print(f"Twoja dzienna ilość kalorii: {daily_kcal} kcal")
        return True
    except Exception as ex:
        print(ex)
        return False


def login():
    user_name = input("Podaj nazwę użytkownika: ")

    if Users.check_user_exists(user_name):
        print(f"Witaj ponownie {user_name} :)")
        main_menu(user_name)
    else:
        print(f"Użytkownik {user_name} nie istnieje. Stwórz nowe konto")
        user_created = create_new_user()  # Jeżeli użytkownik nie istnieje
        if user_created:
            main_menu(user_name)


if __name__ == "__main__":
    login()
