# Generated by Django 2.2.1 on 2019-05-26 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0005_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrustedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('original_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='recommendations.User')),
                ('trusted_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trusted_user', to='recommendations.User')),
            ],
        ),
    ]
