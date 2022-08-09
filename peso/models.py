from django.db import models

# Create your models here.


class Commento(models.Model):
    pass

class peso(models.Model):
    peso = models.PositiveIntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    commenti = Commento()