# Generated by Django 3.1.2 on 2020-10-28 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20201027_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='form',
        ),
    ]