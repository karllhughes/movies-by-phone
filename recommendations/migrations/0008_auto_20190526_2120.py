# Generated by Django 2.2.1 on 2019-05-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0007_auto_20190526_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='context',
            field=models.TextField(blank=True, default=''),
        ),
    ]
