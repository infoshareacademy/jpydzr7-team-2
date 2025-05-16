from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('add_training/', views.add_training, name='add_training'),
    path('list_meals/', views.list_meals, name='list_meals'),
    path('trainings/', views.training_list, name='training_list'),
    path('view_data/', views.view_data, name='view_data'),
    path('edit_data/', views.edit_data, name='edit_data'),
    path('delete_meal/', views.delete_meal, name='delete_meal'),
    path('delete_training//<int:training_id>/', views.delete_training, name='delete_training'),
    path('count_calories/', views.count_calories, name='count_calories'),
]