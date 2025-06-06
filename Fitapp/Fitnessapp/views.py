from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrainingForm
from .models import Trainings, Users, Meals
from django.utils import timezone


def menu(request):
    return render(request, 'menu/menu.html')

def add_meal(request):
    if request.method == 'POST':
        user = Users.objects.get(id=1)
        meal_type = request.POST.get('meal_type')
        name = request.POST.get('name')
        calories = request.POST.get('calories')

        Meals(
            user=user,meal_type=meal_type,name=name,calories=calories
        ).save()

        return render(request, 'add_meal/add_meal.html', {})

    return render(request, 'add_meal/add_meal.html', {})

def list_meals(request):
    return render(request, 'list_meals/list_meals.html')

def view_data(request):
    return render(request, 'view_data/view_data.html')

def edit_data(request):
    return render(request, 'edit_data/edit_data.html')

def delete_meal(request):
    return render(request, 'delete_meal/delete_meal.html')

def count_calories(request):
    return render(request, 'count_calories/count_calories.html')



def add_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = Users.objects.get(id=1)
            training.calories_burned = training.activity_type.calories_per_minute * training.duration
            training.creation_date = request.POST.get('creation_date')  # Możesz dodać czas utworzenia
            training.save()
            return render(request, 'training_confirmation/training_confirmation.html', {'training': training})
    else:
        form = TrainingForm()

    return render(request, 'add_training/add_training.html', {'form': form})


def training_list(request):
    if 'date' in request.GET:
        date_str = request.GET['date']
        date = timezone.datetime.strptime(date_str, "%Y-%m-%d")
        trainings = Trainings.objects.filter(date__date=date).order_by('-date')
    else:
        trainings = Trainings.objects.all().order_by('-date')
    return render(request, 'training_list/training_list.html', {'trainings': trainings})


def delete_training(request, training_id):
    training = get_object_or_404(Trainings, id=training_id)
    if request.method == "POST":
        training.delete()
        return redirect('training_list')
    return redirect('training_list')

