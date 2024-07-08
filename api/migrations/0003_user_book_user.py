# Generated by Django 5.0.6 on 2024-07-08 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_characterbook_character_character_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
