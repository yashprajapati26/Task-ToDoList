# Generated by Django 3.2.12 on 2022-02-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todolist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(),
        ),
    ]