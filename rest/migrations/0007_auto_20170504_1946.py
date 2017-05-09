# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_auto_20170504_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rest.Symbol', to_field='name'),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]