# Generated by Django 4.1 on 2022-08-14 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pasto', '0010_alter_pasto_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pasto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pasto.pasto')),
            ],
        ),
        migrations.CreateModel(
            name='LikeCommento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True)),
                ('commento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pasto.commento')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
