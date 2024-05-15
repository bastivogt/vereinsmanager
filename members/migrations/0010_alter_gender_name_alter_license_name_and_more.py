# Generated by Django 5.0.6 on 2024-05-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_remove_member_adult_with_child_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]