from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    name = models.CharField('Имя', max_length=200, )
    last_name = models.CharField('Фамилия', max_length=300)
    subject_of_course = models.CharField('Предмет обучения', max_length=300)
    phone_number = PhoneNumberField('Номер телефона')
    email = models.EmailField('почта')
