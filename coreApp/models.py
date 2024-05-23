from django.db import models


class CoreModel(models.Model):
    creat_data = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
