# Generated by Django 5.0.6 on 2024-06-27 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='characterBook',
            new_name='character_book',
        ),
    ]