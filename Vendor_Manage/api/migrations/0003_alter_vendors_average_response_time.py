# Generated by Django 4.1.1 on 2024-05-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_vendors_average_response_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='average_response_time',
            field=models.FloatField(),
        ),
    ]
