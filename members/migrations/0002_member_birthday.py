# Generated by Django 5.0.6 on 2024-05-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
