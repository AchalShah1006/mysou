# Generated by Django 3.1.6 on 2021-03-21 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_clubs_placements_resources'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clubs',
        ),
        migrations.DeleteModel(
            name='Placements',
        ),
        migrations.DeleteModel(
            name='Resources',
        ),
    ]
