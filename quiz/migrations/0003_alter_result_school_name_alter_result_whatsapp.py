# Generated by Django 5.0.7 on 2024-07-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_result_school_name_result_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='school_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='whatsapp',
            field=models.CharField(max_length=20),
        ),
    ]
