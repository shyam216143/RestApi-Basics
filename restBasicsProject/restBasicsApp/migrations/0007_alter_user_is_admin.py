# Generated by Django 4.1 on 2022-09-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restBasicsApp', '0006_rename_myuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
