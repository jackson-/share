# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-01 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=132, null=True)),
                ('eighth_price', models.FloatField()),
                ('quarter_price', models.FloatField()),
                ('half_price', models.FloatField()),
                ('ounce_price', models.FloatField()),
                ('link', models.URLField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=132)),
                ('description', models.CharField(max_length=255, null=True)),
                ('pricing', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('delivery_minimum', models.IntegerField(default=0)),
                ('delivery_fee', models.IntegerField(default=0)),
                ('est_wait_begin', models.IntegerField(default=50)),
                ('est_wait_end', models.IntegerField(default=60)),
            ],
        ),
    ]
