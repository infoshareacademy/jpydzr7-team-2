from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrainingForm, UserRegistrationForm, MealForm
from .models import Trainings, Users, Meals, SActivityType
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hashowanie hasła
            user.save()
            return redirect('login')  # przekieruj do logowania lub innej strony
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # first_name
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login/login.html', {'error': 'Błędne dane logowania'})

    return render(request, 'login/login.html')

def menu(request):
    return render(request, 'menu/menu.html')

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return render(request, 'meal_confirmation/meal_confirmation.html', {'meal': meal})
    else:
        form = MealForm()

    return render(request, 'add_meal/add_meal.html', {'form': form})

def list_meals(request):
    if not request.user.is_authenticated:
        return redirect('login')

    meals = Meals.objects.filter(user=request.user, is_deleted=False)

    if 'date' in request.GET:
        date_str = request.GET['date']
        try:
            date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
            meals = meals.filter(creation_date__date=date)
        except ValueError:
            pass

    meals = meals.order_by('-date')

    return render(request, 'list_meals/list_meals.html', {'meals': meals})

def view_data(request):
    return render(request, 'view_data/view_data.html')

@login_required
def my_account_view(request):
    user = request.user
    edit_mode = request.GET.get('edit') == '1'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dane zostały zaktualizowane.')
            return redirect('my_account')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
        'edit_mode': edit_mode
    }
    return render(request, 'my_account_view/my_account_view.html', context)

def delete_meal(request, meal_id):
    meal = get_object_or_404(Meals, id=meal_id, is_deleted=False)

    if request.method == "POST":
        meal.is_deleted = True
        meal.save()
        return redirect('list_meals')
    return redirect('list_meals')

def count_calories(request):
    return render(request, 'count_calories/count_calories.html')

def add_training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.calories_burned = training.activity_type.calories_per_minute * training.duration
            training.save()
            return render(request, 'training_confirmation/training_confirmation.html', {'training': training})
    else:
        form = TrainingForm()

    return render(request, 'add_training/add_training.html', {'form': form})


def training_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    trainings = Trainings.objects.filter(user=request.user, is_deleted=False)

    if 'date' in request.GET:
        date_str = request.GET['date']
        try:
            date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
            trainings = trainings.filter(date__date=date)
        except ValueError:
            pass

    activity_type_id = request.GET.get('activity_type_id')
    if activity_type_id:
        trainings = trainings.filter(activity_type_id=activity_type_id)

    trainings = trainings.order_by('-date')

    activity_types = SActivityType.objects.all()

    return render(request, 'training_list/training_list.html', {
        'trainings': trainings,
        'activity_types': activity_types,
        'selected_type_id': activity_type_id
    })


def delete_training(request, training_id):
    training = get_object_or_404(Trainings, id=training_id, is_deleted=False)
    if request.method == "POST":
        training.is_deleted = True
        training.save()
        return redirect('training_list')
    return redirect('training_list')

def logout_view(request):
    logout(request)
    return redirect('login')

