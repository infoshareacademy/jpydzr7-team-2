# forms.py
from django import forms
from .models import Trainings, SActivityType
from django.utils import timezone

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
        today = timezone.now().date()  # Pobierz dzisiejszą datę
        self.fields['date'].widget.attrs['max'] = today
