from random import choices
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT
    return '{0}/{1}'.format(instance.owner.username, filename)

# Create your models here.
class Pasto(models.Model):
    kcal=models.PositiveIntegerField()
    descrizione=models.TextField(max_length=1024)
    foto=models.ImageField(upload_to=user_directory_path)

    TIPI_DI_PASTO=((1,'colazione'),(2,'pranzo'),(3,'snack'),(4,'cena'))
    tipo = models.PositiveSmallIntegerField(choices=TIPI_DI_PASTO, default=1, blank=False,null=False)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    REQUIRED_FIELDS=['kcal','descrizione','tipo','date','owner']

    def tipo_verbose(self):
        return dict(Pasto.TIPI_DI_PASTO)[self.tipo]

class Commento(models.Model):
    commento=models.TextField(max_length=512, null=False, blank=False)
    likes=models.PositiveIntegerField(default=0)
    pasto=models.ForeignKey(Pasto,on_delete=models.CASCADE,null=True)
    reply=models.ForeignKey('Commento',on_delete=models.CASCADE,null=True, related_name='+')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
