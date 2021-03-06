# Generated by Django 3.0.8 on 2020-07-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0003_auto_20200717_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_pay', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.Department')),
            ],
            options={
                'db_table': 'teams',
            },
        ),
    ]
