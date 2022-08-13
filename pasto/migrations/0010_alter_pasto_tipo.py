# Generated by Django 4.1 on 2022-08-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasto', '0009_alter_pasto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasto',
            name='tipo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'colazione'), (2, 'pranzo'), (3, 'snack'), (4, 'cena')], default=1),
        ),
    ]