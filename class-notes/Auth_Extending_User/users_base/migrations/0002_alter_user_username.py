# Generated by Django 3.2.8 on 2022-05-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]