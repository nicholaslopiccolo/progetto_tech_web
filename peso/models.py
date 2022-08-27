from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Peso(models.Model):
    peso = models.FloatField(validators=[MinValueValidator(0.0)],null=False)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    REQUIRED_FIELDS = ['peso','date','owner']