# Generated by Django 3.1.2 on 2020-11-01 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='name',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
