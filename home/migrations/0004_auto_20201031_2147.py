# Generated by Django 3.1.2 on 2020-10-31 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='age',
        ),
        migrations.AddField(
            model_name='doctor',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
