from django.db import models


class Tips(models.Model):
    IMPORTANCEOPTIONS = [('I', 'Important'), ('R', 'Relevant'),
                         ('U', 'Unimportant')]
    title = models.CharField(max_length=100)
    tipType = models.CharField(max_length=25)
    importance = models.CharField(max_length=1, choices=IMPORTANCEOPTIONS)
    warning = models.CharField(max_length=100)


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    stepNum = models.IntegerField()
    utensils = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=30)
