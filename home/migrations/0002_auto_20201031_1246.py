# Generated by Django 3.1.2 on 2020-10-31 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contact_Us',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='desc',
            new_name='description',
        ),
    ]
