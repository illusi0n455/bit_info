# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0016_auto_20170507_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin',
            options={'ordering': ['-update_date']},
        ),
    ]
