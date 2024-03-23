# Generated by Django 4.0.10 on 2024-03-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]