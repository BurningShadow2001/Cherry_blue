# Generated by Django 3.1.2 on 2020-11-15 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_patient_descriptiom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
