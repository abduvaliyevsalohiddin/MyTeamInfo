from django.db import models
from coreApp.models import *


class Services(CoreModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MyTeam(CoreModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myTeam')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class UsAbout(CoreModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='usAbout')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


DIRECTION_CHOICES = [
    ('Onlayn do\'kon', 'Onlayn do\'kon'),
    ('Consulting', 'Consulting'),
    ('O\'quv markaz', 'O\'quv markaz'),
    ('Onlayn sotuv (kurs vhk)', 'Onlayn sotuv (kurs vhk)'),
    ('Universitet maktab', 'Universitet maktab'),
    ('Mebel (sotish va ishlab chiqarish)', 'Mebel (sotish va ishlab chiqarish)'),
    ('Ishlab chiqarish', 'Ishlab chiqarish'),
    ('Xizmat ko\'rsatish', 'Xizmat ko\'rsatish'),
    ('Tur firma', 'Tur firma'),
    ('Sotuv oflayn', 'Sotuv oflayn'),

]


class RegisterTeam(CoreModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    direction = models.CharField(max_length=100, choices=DIRECTION_CHOICES, default='Onlayn do\'kon')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
