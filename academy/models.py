from django.db import models


class TokenAdmin(models.Model):
    name = models.CharField(max_length=230, unique=True)
    full_text = models.TextField(max_length=60, unique=True)
    date = models.DateTimeField('Дата публик', unique_for_date=True)


class TokenProxy(models.Model):
    name = models.CharField(max_length=200, unique=True)
    full_text = models.TextField(max_length=70, unique=True)
    date = models.DateTimeField('Дата публик', unique_for_date=True)
