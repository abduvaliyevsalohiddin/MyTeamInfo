from django.db import models
from coreApp.models import *


class Services(CoreModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


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


class RegisterTeam(CoreModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Partners(CoreModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners')

    def __str__(self):
        return self.name
