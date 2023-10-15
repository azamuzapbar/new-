from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    name = models.CharField('Имя', max_length=200, )
    last_name = models.CharField('Фамилия', max_length=300)
    date_of_birth = models.DateField('Дата рождения')
    class_of_course = models.CharField('Класс обучения', max_length=300)
    phone_number = PhoneNumberField('Номер телефона')
    email = models.EmailField('почта')
