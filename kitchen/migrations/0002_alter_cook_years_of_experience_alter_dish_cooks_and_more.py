# Generated by Django 4.1.7 on 2023-03-28 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='cooks',
            field=models.ManyToManyField(blank=True, related_name='dishes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='kitchen.dishtype'),
        ),
    ]
