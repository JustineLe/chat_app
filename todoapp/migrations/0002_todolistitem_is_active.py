# Generated by Django 4.0.3 on 2022-03-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
