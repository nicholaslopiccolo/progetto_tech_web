# Generated by Django 4.1 on 2022-08-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
