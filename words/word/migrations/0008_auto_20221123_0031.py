# Generated by Django 3.2.14 on 2022-11-22 15:31

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0007_failword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bigo',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth',
            field=birthday.fields.BirthdayField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
