# Generated by Django 4.1.5 on 2023-01-19 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recettes',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='recettes',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='recettes',
            name='video',
        ),
    ]
