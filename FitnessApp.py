class Users:

    def __init__(self,age=None, weight=None, height=None, gender=None):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

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

def main():
    print("Witaj w aplikacji Xxx!")
    print("Aplikacja pomoże Ci zaplanować dietę oraz osiągnąć wymarzoną sylwetkę")

    user = Users()

    nazwa_uzytkownika = user.create_user_name()
    age = user.age_control()
    weight = user.weight_control()
    height = user.height_control()
    gender = user.gender_control()


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

if __name__ == "__main__":
    main()
