# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Meals(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    meal_type = models.ForeignKey('SMeals', models.DO_NOTHING, db_column='meal_type')
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Meals'


class Trainings(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    activity_type = models.ForeignKey('SActivityType', models.DO_NOTHING, db_column='activity_type')
    duration = models.IntegerField()
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Trainings'


class UserBmiHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    bmi_value = models.FloatField()
    category = models.CharField(max_length=9)
    creation_date = models.DateTimeField()

    class Meta:
        db_table = 'User_bmi_history'


class UserManager(BaseUserManager):
    def create_user(self, first_name, age, password=None, **extra_fields):
        if not first_name:
            raise ValueError('Użytkownik musi mieć imię')
        user = self.model(first_name=first_name, age=age, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, age, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(first_name, age, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, unique=True)  # Używamy jako login
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.IntegerField()
    gender = models.CharField(max_length=1)
    status = models.CharField(max_length=10, default='active')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['age']

    class Meta:
        db_table = 'Users'


class SActivityType(models.Model):
    code = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    calories_per_minute = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 's_activity_type'

    def __str__(self):
        return self.name

class SMeals(models.Model):
    code = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

    class Meta:
            db_table = 's_meals'

    def __str__(self):
        return self.name