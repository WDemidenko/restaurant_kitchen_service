# Generated by Django 4.1.7 on 2023-03-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_alter_cook_years_of_experience_alter_dish_cooks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='first_name',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='cook',
            name='last_name',
            field=models.CharField(max_length=65),
        ),
    ]
