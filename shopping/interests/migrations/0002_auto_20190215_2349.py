# Generated by Django 2.1.5 on 2019-02-15 23:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='registered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
