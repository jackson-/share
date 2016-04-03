# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-03 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=132, null=True)),
                ('current_total', models.FloatField()),
                ('price', models.FloatField()),
                ('customers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Item')),
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
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Store'),
        ),
    ]
