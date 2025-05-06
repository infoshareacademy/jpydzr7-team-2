# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Meals(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    meal_type = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    creation_date = models.DateTimeField()

    class Meta:
        db_table = 'Meals'


class Trainings(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    activity_type = models.ForeignKey('SActivityType', models.DO_NOTHING, db_column='activity_type')
    duration = models.IntegerField()
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    is_deleted = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField()

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


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()
    password = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.IntegerField()
    gender = models.CharField(max_length=1)
    status = models.CharField(max_length=10)
    creation_date = models.DateTimeField()
    modification_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Users'


class SActivityType(models.Model):
    code = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    calories_per_minute = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 's_activity_type'
