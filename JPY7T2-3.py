def oblicz_bmi(waga, wzrost_cm, plec):

    # Przeliczamy wzrost na metry
    wzrost = wzrost_cm / 100
    bmi = waga / (wzrost ** 2)

    # Określenie kategorii BMI
    if bmi < 18.5:
        kategoria = "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        kategoria = "W normie"
    elif 25 <= bmi < 29.9:
        kategoria = "Nadwaga"
    else:
        kategoria = "Otyłość"

    return bmi, kategoria


def wyswietl_dane(waga, wzrost_cm, plec):
    """
    Funkcja wyświetla dane użytkownika oraz wyliczone BMI i kategorię.
    """
    bmi, kategoria = oblicz_bmi(waga, wzrost_cm, plec)

    # Wyświetlenie wyników
    print("Moje dane:")
    print(f"Płeć: {plec.capitalize()}")
    print(f"Waga: {waga} kg")
    print(f"Wzrost: {wzrost_cm} cm")
    print(f"Twoje BMI: {bmi:.2f}")
    print(f"Kategoria: {kategoria}")


# Przykład użycia

# Wprowadzenie danych przez użytkownika
waga = float(input("Podaj swoją wagę w kg: "))
wzrost_cm = int(input("Podaj swój wzrost w centymetrach: "))
plec = input("Podaj swoją płeć (kobieta/mężczyzna): ").lower()

# Wyświetlenie wyników
wyswietl_dane(waga, wzrost_cm, plec)