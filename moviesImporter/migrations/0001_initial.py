# Generated by Django 2.2.1 on 2019-08-24 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('genre_1', models.CharField(max_length=255)),
                ('genre_2', models.CharField(max_length=255)),
                ('genre_3', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('director_1', models.CharField(max_length=255)),
                ('director_2', models.CharField(max_length=255)),
                ('director_3', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
            ],
        ),
    ]