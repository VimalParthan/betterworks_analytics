# Generated by Django 3.0.8 on 2020-07-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('objective', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
