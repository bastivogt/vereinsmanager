# Generated by Django 5.0.6 on 2024-05-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(),
        ),
    ]
