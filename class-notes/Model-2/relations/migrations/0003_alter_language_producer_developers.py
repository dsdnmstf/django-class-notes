# Generated by Django 4.0.4 on 2022-05-05 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_frameworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='producer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='relations.creator'),
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('framework', models.ManyToManyField(to='relations.frameworks')),
            ],
        ),
    ]
