# Generated by Django 2.2.1 on 2019-05-22 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190514_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='year_of_birth',
            new_name='date_of_birth',
        ),
    ]
