# Generated by Django 4.0.10 on 2024-03-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('pages', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
