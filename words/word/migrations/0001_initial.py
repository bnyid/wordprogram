# Generated by Django 3.2.14 on 2022-08-02 08:39

import birthday.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('birth_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birth', birthday.fields.BirthdayField(null=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('bigo', models.TextField(max_length=300)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sclasss', models.ManyToManyField(related_name='std_class', to='word.Sclass')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, null=True)),
                ('day', models.IntegerField(null=True)),
                ('word_eng', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('test_date', birthday.fields.BirthdayField(null=True)),
                ('start_day', models.IntegerField(null=True)),
                ('end_day', models.IntegerField(null=True)),
                ('book_name', models.CharField(max_length=50, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('fail_words', models.ManyToManyField(null=True, related_name='fail_word', to='word.Word')),
                ('stduent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='std_test', to='word.student')),
                ('test_words', models.ManyToManyField(null=True, related_name='test_word', to='word.Word')),
            ],
        ),
    ]
