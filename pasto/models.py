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

    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    REQUIRED_FIELDS=['kcal','descrizione','tipo','date','owner']

    def likes(self):
        return len(LikePasto.objects.filter(pasto=self))

    def tipo_verbose(self):
        return dict(Pasto.TIPI_DI_PASTO)[self.tipo]

    def gen_tree_commenti(self):
        self.commenti= []
        qs_commenti = Commento.objects.filter(pasto=self,reply=None)

        def gen_tree(qs,cm):
            for commento in qs:
                cm.append([commento,[]])
                qs_new = Commento.objects.filter(pasto=commento.pasto,reply=commento)
                if len(qs_new)>0:
                    gen_tree(qs_new,cm[-1][1])

        gen_tree(qs_commenti,self.commenti)
        
        return self.commenti


class Commento(models.Model):
    commento=models.TextField(max_length=512, null=False, blank=False)
    likes=models.PositiveIntegerField(default=0)
    dislikes=models.PositiveIntegerField(default=0)
    pasto=models.ForeignKey(Pasto,on_delete=models.CASCADE,null=True)
    reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True, related_name='+')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def likes(self):
        return len(LikeCommento.objects.filter(commento=self))

class LikeCommento(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    commento = models.ForeignKey(Commento,on_delete=models.CASCADE,null=True, related_name='+')

    REQUIRED_FIELD = ['like','owner','commento']

class LikePasto(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    pasto = models.ForeignKey(Pasto,on_delete=models.CASCADE,null=True, related_name='+')

    REQUIRED_FIELD = ['like','owner','commento']

