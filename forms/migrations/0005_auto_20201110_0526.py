# Generated by Django 2.2.10 on 2020-11-10 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0004_remove_answer_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='without_login',
            field=models.BooleanField(default=True),
        ),
    ]
