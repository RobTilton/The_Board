# Generated by Django 4.2.5 on 2023-10-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_number',
            field=models.IntegerField(default=0, max_length=10, unique=True),
        ),
    ]
