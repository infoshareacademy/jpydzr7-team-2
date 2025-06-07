# forms.py
from django import forms
from .models import Trainings, SActivityType, Users, Meals, SMeals
from django.utils import timezone


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'age', 'weight', 'height', 'gender']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'age': 'Wiek',
            'weight': 'Waga',
            'height': 'Wzrost',
            'gender': 'Płeć',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Hasła nie są takie same")

        return cleaned_data


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Trainings
        fields = ['activity_type', 'duration', 'date']

    activity_type = forms.ModelChoiceField(queryset=SActivityType.objects.all(), label="Aktywność", empty_label="Wybierz aktywność")

    duration = forms.IntegerField(min_value=1, label="Czas trwania w minutach")

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data treningu",
        initial=timezone.now().date(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        today = timezone.now().date()
        self.fields['date'].widget.attrs['max'] = today

class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['meal_type', 'name', 'calories', 'date']

    meal_type = forms.ModelChoiceField(
        queryset=SMeals.objects.all(),
        label="Typ posiłku",
        empty_label="Wybierz typ posiłku"
    )

    name = forms.CharField(
        label="Opis posiłku",
        max_length=100,
        required=True
    )

    calories = forms.IntegerField(
        label="Kalorie",
        min_value=0,
        required=True
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data treningu",
        initial=timezone.now().date(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        today = timezone.now().date()
        self.fields['date'].widget.attrs['max'] = today
