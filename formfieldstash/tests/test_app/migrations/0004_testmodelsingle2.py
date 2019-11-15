# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-15 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20191114_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelSingle2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.CharField(blank=True, choices=[('', 'Empty'), ('horse', 'Horse'), ('bear', 'Bear'), ('octopus', 'Octopus')], max_length=20, verbose_name='Selection')),
                ('horse', models.CharField(blank=True, max_length=20)),
                ('bear', models.CharField(blank=True, max_length=20)),
                ('octopus', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
